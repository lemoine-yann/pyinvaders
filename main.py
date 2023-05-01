import pgzrun
import sys
mod = sys.modules['__main__']  # fix dynamic references unresolved

WIDTH = 800
HEIGHT = 600


def draw():
    mod.screen.clear()
    mod.screen.draw.circle((400, 300), 30, 'white')


pgzrun.go()
