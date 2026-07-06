import os

# ----------------------------
# Window
# ----------------------------
WIDTH = 800
HEIGHT = 600
TITLE = "Snake Game Pro"

FPS = 10

# ----------------------------
# Grid
# ----------------------------
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# ----------------------------
# Colors
# ----------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 120, 255)
YELLOW = (255, 255, 0)

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSETS = os.path.join(BASE_DIR, "assets")
SOUNDS = os.path.join(BASE_DIR, "sounds")

# Images
BACKGROUND_IMAGE = os.path.join(ASSETS, "background.png")
SNAKE_HEAD_IMAGE = os.path.join(ASSETS, "snake_head.png")
SNAKE_BODY_IMAGE = os.path.join(ASSETS, "snake_body.png")
APPLE_IMAGE = os.path.join(ASSETS, "apple.png")
ICON_IMAGE = os.path.join(ASSETS, "icon.ico")

# Sounds
BG_MUSIC = os.path.join(SOUNDS, "bg_music.mp3")
EAT_SOUND = os.path.join(SOUNDS, "eat.wav")
GAMEOVER_SOUND = os.path.join(SOUNDS, "gameover.wav")