import pyxel
from random import randint
import tweening

class Game:
    def __init__(self):
        self.step = 0
        pyxel.init(128, 128, fps=60)
        colsLeft = 128
        self.width = []

        self.texts = ["The screen melt is an effect",
                      "seen when Doom changes scene,",
                      "for example, when starting or",
                      "exiting a level. The screen",
                      "appears to 'melt' away to the",
                      "new screen."]
        self.textOff = tweening.TimedValue(128, duration=60, f="easeInBounce", delay=50, inverted=True, autoreset=False)
        self.timeToHelp = tweening.TimedBool(300)

        while colsLeft > 0:
            curSliceW = 1000000000
            while curSliceW > colsLeft:
                curSliceW = randint(1,1)
            self.width.append(curSliceW)
            colsLeft -= curSliceW

        # Uncomment one of the following for various effects
        self.offs = [tweening.TimedValue(192, duration=60, delay=randint(30, 45), f="linear") for x in range(128)]
        # self.offs = [tweening.TimedValue(192, duration=randint(60,100), f="easeInOutQuart") for x in range(128)]
        # self.offs = [tweening.TimedValue(192, duration=randint(60,90), f="easeInCubic") for x in range(128)]
        # self.offs = [tweening.TimedValue(192, duration=randint(50,60), f="easeInOutQuart") for x in range(128)]
        # self.offs = [tweening.TimedValue(192, duration=randint(50,60), delay=randint(30,60), f="easeInOutQuart") for x in range(128)]
        # self.offs = [tweening.TimedValue(192, 60, delay=randint(0,20), f="easeInBack") for x in range(128)]

        # self.offs = [tweening.TimedValue(192, duration=randint(60,160), f="easeInCubic") for x in range(128)]
        # self.offs = [tweening.TimedValue(192, 40, delay=randint(0,10), f="easeInBounce", inverted=True) for x in range(128)]
        # self.offs = [tweening.TimedValue(192, duration=randint(50,60), delay=randint(0,10), f="easeInBack", inverted=True) for x in range(128)]

        self.imgPalette = [0x000066, 0x0101B0, 0x04041E, 0x635436,
                           0x990000, 0x993230, 0x9E9E61, 0xAC662B,
                           0xB500B5, 0xCC0000, 0xCC3311, 0xCE9966,
                           0xD1991F, 0xD1C5D8, 0xDCCD66, 0xFEED99]
        pyxel.colors.from_list(self.imgPalette)

        pyxel.image(0).load(0, 0, "DOOM128-16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            for o in self.offs: o.reset()
            self.textOff.reset()
            self.timeToHelp.reset()

    def draw(self):
        pyxel.cls(2)
        for ti in range(len(self.texts)):
            pyxel.text(5+self.textOff.value(), 48 + 6*ti, self.texts[ti], 12)

        curX = 0
        for i in range(len(self.width)):
            if self.offs[i].value() > 128:
                curX += self.width[i]
                continue
            pyxel.blt(curX, self.offs[i].value(), 0, curX, 0, self.width[i], 128)
            curX += self.width[i]

        # for i in range(16):
        #     pyxel.rect(8*i, 120, 8, 8, i)
        if self.timeToHelp.true():
            pyxel.text(16, 110, "Press Backspace to reset", 12)


Game()
