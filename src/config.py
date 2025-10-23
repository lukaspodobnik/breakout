import pygame

from utils.resource_path import get_resource_path

TITLE = "Breakout"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

ASSETS_DIR = get_resource_path("assets")
LEVELS_DIR = get_resource_path(ASSETS_DIR / "levels")
SOUNDS_DIR = get_resource_path(ASSETS_DIR / "sounds")

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

RESPAWN_BALL = pygame.USEREVENT + 1
DEATH = RESPAWN_BALL + 1
