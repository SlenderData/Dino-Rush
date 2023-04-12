import os

SCREENSIZE = (1200, 600)

FPS = 60

AUDIO_PATHS = {
    'die': os.path.join(os.getcwd(), 'resources/audios/die.wav'),
    'jump': os.path.join(os.getcwd(), 'resources/audios/jump.wav'),
    'point': os.path.join(os.getcwd(), 'resources/audios/point.wav')
}
IMAGE_PATHS = {
    'cacti': [
        os.path.join(os.getcwd(), 'resources/images/cacti-big.svg'),
        os.path.join(os.getcwd(), 'resources/images/cacti-small.svg')
    ],
    'cloud': os.path.join(os.getcwd(), 'resources/images/cloud.svg'),
    'dino': [
        os.path.join(os.getcwd(), 'resources/images/dino.svg'),
        os.path.join(os.getcwd(), 'resources/images/dino_ducking.svg')
    ],
    'ground': os.path.join(os.getcwd(), 'resources/images/ground-4x.svg'),
    'ptera': os.path.join(os.getcwd(), 'resources/images/ptera.svg'),
    'replay': os.path.join(os.getcwd(), 'resources/images/replay.svg')
}
FONT_PATHS = {
    'joystix': os.path.join(os.getcwd(), 'resources/fonts/JoystixMonospace-Regular.ttf')
}

BACKGROUND_COLOR = (235, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
