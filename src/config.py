from utils.resource_path import get_resource_path

TITLE = "Breakout"
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
HUD_HEIGHT = 50

ASSETS_DIR = get_resource_path("assets")
LEVELS_DIR = get_resource_path(ASSETS_DIR / "levels")
SOUNDS_DIR = get_resource_path(ASSETS_DIR / "sounds")

EXP_BASE = 100
EXP_GROWTH = 1.5
PLAYER_SPEED = 400
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 8
MAX_ANGLE = 250

BALL_SIZE = 15
BALL_SPEED = 450

BLOCK_WIDTH = 40
BLOCK_HEIGHT = 25
BLOCK_SPACING = 5

DAMAGE_ZONE_HEIGHT = 10
