import pyxel
import math
import pytweening

class TimedValue():
    def __init__(self, v=0, duration=30, f='easeOutElastic', offset=0, delay=0, p=None, autoreset=False, inverted=False, bounce=False):
        """
        d: duration (in frames).
        f: easing function name. Look them up at http://easings.net.
        offset: start from a non-zero value.
        p: instance of TimedValue to copy parameters from.
        delay: start after this many frames
        """
    
        if p:
            self.buildFromPeer(p)
        else:
            self.v = v
            self.duration = duration
            self.function = getattr(pytweening, f)
            self.offset = offset
            self.autoreset = autoreset
            self.inverted = inverted
            self.bounce = bounce
            self.delay = delay

        self.reset()
        
        self.FORWARD = True
        self.BACK = not self.FORWARD

        self.dir = self.FORWARD
        self.lastBounceTime = -1

    def buildFromPeer(self, p):
        self.v = p.v
        self.duration = p.duration
        self.function = p.function
        self.offset = p.offset
        self.autoreset = p.autoreset
        self.inverted = p.inverted
        self.bounce = p.bounce
        self.delay = p.delay

    def value(self):
        if pyxel.frame_count < self.delayedBirthTime: return self.offset

        progress = (pyxel.frame_count - self.delayedBirthTime) / self.duration

        if self.bounce:
            p = self.bouncingProgress(progress)
        else:
            p = self.normalProgress(progress)

        return self.offset + (self.v - self.offset) * self.function(p)

    def normalProgress(self, p):
        if p >= 1:
            if self.autoreset:
                self.reset()
                p = 0
            else:
                p = 1

        if self.inverted:
            p = 1 - p

        return p

    def bouncingProgress(self, p):
        if p < 1: return p
        pp = math.floor(p)
        if pp % 2 == 1:
            r = 1 - (p - pp)
        else:
            r = p - pp
        return r

    def setValue(self, newVal):
        """
        Change the target value. Can be called at any time.
        """
        self.v = newVal

    def reset(self):
        """
        Reset the birth time, effectively restarting the interpolation.
        """
        self.birthTime = pyxel.frame_count
        self.delayedBirthTime = self.birthTime + self.delay

#################################################################################

class TimedBool():
    def __init__(self, delay=30, autoreset=False):
        """
        delay: delay before which the value becomes True (in frames).
        """
        self.birthTime = pyxel.frame_count
        self.delay = delay
        self.autoreset = autoreset

    def reset(self, delay=0):
        """
        Reset the birth time, effectively restarting the countdown.
        delay: new delay
        """
        if delay > 0:
            self.delay = delay
        self.birthTime = pyxel.frame_count

    def value(self):
        if pyxel.frame_count > self.birthTime + self.delay:
            if self.autoreset: self.reset()
            return True
        return False

    def true(self):
        return self.value()

    def false(self):
        return not self.value()

    def elapsed(self):
        return self.value()

    def up(self):
        return self.value()

