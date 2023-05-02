import pgzrun
from enum import Enum
import sys
mod = sys.modules['__main__']  # fix dynamic references unresolved

# screen size
WIDTH = 1920
HEIGHT = 1080


# aliens settings
class Direction(Enum):
    RIGHT = 1,
    LEFT = 2


AlienDirection = Direction.RIGHT
AlienSpeed = 2
AlienComeDownSpeed = 10

# init aliens array
aliens = []
for y in range(0, 4):  # 4 rows
    for x in range(0, 10):  # 10 columns
        aliens.append(mod.Actor('alienship', (x * 150 + 100, y * 120 + 100)))


def draw():
    mod.screen.clear()
    for alien in aliens:  # draw each alien in array
        alien.draw()


def update():
    move_aliens()


def move_aliens():
    global AlienDirection, AlienSpeed, AlienComeDownSpeed
    directionchange = False

    for alien in aliens:
        match AlienDirection:  # move aliens
            case Direction.LEFT:
                alien.left -= AlienSpeed
            case Direction.RIGHT:
                alien.left += AlienSpeed
        if alien.left > WIDTH - 150:  # check bounds
            AlienDirection = Direction.LEFT
            directionchange = True
            break
        elif alien.left < 0:
            AlienDirection = Direction.RIGHT
            directionchange = True
            break
    if directionchange:  # alien move down if direction change
        for alien in aliens:
            alien.top += AlienComeDownSpeed


pgzrun.go()
