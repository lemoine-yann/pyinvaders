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
AlienComeDownSpeed = 20

# init aliens array
aliens = []
for y in range(0, 4):  # 4 rows
    for x in range(0, 10):  # 10 columns
        aliens.append(mod.Actor('alienship', (x * 150 + 100, y * 120 + 100)))


# player settings
PlayerX = WIDTH / 2  # middle of screen
PlayerY = HEIGHT - 80  # bottom of screen
PlayerSpeed = 10

# init player
player = mod.Actor('playership', (PlayerX, PlayerY))


# rocket settings
RocketSpeed = 15
PlayerCanShoot = True
DelayBetweenRocket = 0.5

# init rockets
rockets = []
for i in range(0, 3):  # 3 rockets available
    newrocket = mod.Actor('rocket')
    newrocket.left = -1000
    newrocket.top = -1000
    rockets.append(newrocket)  # -1000,-1000 mean disabled


def draw():
    mod.screen.clear()
    for alien in aliens:  # draw each alien in array
        alien.draw()
    for rocket in rockets:  # draw each active rockets
        if rocket.left != -1000 and rocket.top != -1000:
            rocket.draw()
    player.draw()  # draw player


def update():
    move_aliens()
    manage_rockets()
    manage_player()


def manage_rockets():
    global PlayerCanShoot, DelayBetweenRocket

    if PlayerCanShoot and mod.keyboard.space:  # new shot requested
        for rocket in rockets:
            if rocket.left == -1000 and rocket.top == -1000:  # check if one rocket is available
                rocket.center = player.center
                rocket.bottom = player.top
                PlayerCanShoot = False
                mod.clock.schedule_unique(active_rockets, DelayBetweenRocket)  # active delay between rockets
                break
    for rocket in rockets:  # move active rockets
        if rocket.left != -1000 and rocket.top != - 1000:
            rocket.top -= RocketSpeed
            if rocket.bottom < 0:  # check bounds
                rocket.left = -1000
                rocket.top = -1000


def active_rockets():
    global PlayerCanShoot
    PlayerCanShoot = True


def manage_player():
    if mod.keyboard.left:  # move ship
        player.left -= PlayerSpeed
    elif mod.keyboard.right:
        player.left += PlayerSpeed
    if player.left > WIDTH - player.width:  # check bounds
        player.left = WIDTH - player.width
    elif player.left < 0:
        player.left = 0


def move_aliens():
    global AlienDirection, AlienSpeed, AlienComeDownSpeed
    directionchange = False

    for alien in aliens:
        match AlienDirection:  # move aliens
            case Direction.LEFT:
                alien.left -= AlienSpeed
            case Direction.RIGHT:
                alien.left += AlienSpeed
        if alien.left > WIDTH - alien.width:  # check bounds
            AlienDirection = Direction.LEFT
            directionchange = True
        elif alien.left < 0:
            AlienDirection = Direction.RIGHT
            directionchange = True
    if directionchange:  # alien move down if direction change
        for alien in aliens:
            alien.top += AlienComeDownSpeed


pgzrun.go()
