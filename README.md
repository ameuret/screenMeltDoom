## Screen Melt

A quick code lab to explore the use of custom palettes in the [Pyxel game engine](https://github.com/kitao/pyxel).

![Demo](demo.gif )

### Upshot

Palette customization applies globally. Only the palette set last through `pyxel.colors.from_list(self.palette)` is active.

Per Canvas (Image) palettes are not supported. `pyxel.image(0).colors.from_list(self.palette)` is illegal.

According to [Merwork@Discord](https://discord.com/channels/697925198992900106/697925198992900109/937466912798040104), the `pal` call can be used to manipulate the palette multiple times inside a single frame. Just for swapping though...

## Install

This project uses [Poetry](https://python-poetry.org "At last Python has more or less caught up with modernity about dependency management"), so all you have to do is install Poetry and run `poetry install` in this project directory.

## Run

In order to completely isolate your environment, you should run this project under Poetry's managed environment:

Either in a separate shell spawned by Poetry:

```
poetry shell
python main.py
```

Or directly through the run command: `poetry run python main.py`

