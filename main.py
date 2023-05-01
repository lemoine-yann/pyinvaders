import pgzrun
import sys
mod = sys.modules['__main__']  # fix dynamic references unresolved

# screen size
WIDTH = 1920
HEIGHT = 1080

# init aliens array
aliens = []
for y in range(0, 4):  # 4 rows
    for x in range(0, 10):  # 10 columns
        aliens.append(mod.Actor('alienship', (x * 150 + 100, y * 100 + 100)))


def draw():
    mod.screen.clear()
    for alien in aliens:  # draw each alien in array
        alien.draw()


def update():
    for alien in aliens:  # move aliens
        alien.left += 2
        if alien.left > WIDTH:
            alien.right = 0


pgzrun.go()
