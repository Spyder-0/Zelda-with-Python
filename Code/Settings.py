import os

# This is for file (images specifically) importing (This line changes the directory to where the project is saved)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
	"player": -26,
	"object": -40,
	"grass": -10,
	"invisible": 0
	}

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "../Graphics/Font/Joystix.ttf"
UI_FONT_SIZE = 18

# General Colors
WATER_COLOR = "#71ddee"
UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

# UI Colors
HEALTH_COLOR = "Red"
ENERGY_COLOR = "Blue"
UI_BORDER_COLOR_ACTIVE = "Gold"

# Upgrade Menu
TEXT_COLOR_SELECTED = "#111111"
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED = "#111111"
UPGRADE_BG_COLOR_SELECTED = "#EEEEEE"

# Weapons
weapon_data = {
	"sword": {"cooldown": 100, "damage": 15, "graphic": "../Graphics/Weapons/Sword/Full.png"},
	"lance": {"cooldown": 400, "damage": 30, "graphic": "../Graphics/Weapons/Lance/Full.png"},
	"axe": {"cooldown": 300, "damage": 20, "graphic": "../Graphics/Weapons/Axe/Full.png"},
	"rapier": {"cooldown": 50, "damage": 8, "graphic": "../Graphics/Weapons/Rapier/Full.png"},
	"sai": {"cooldown": 80, "damage": 10, "graphic": "../Graphics/Weapons/Sai/Full.png"}
    }

# Magic
magic_data = {
	"flame": {"strength": 5, "cost": 20, "graphic": "../Graphics/Particles/Flame/Fire.png"},
	"heal": {"strength": 20, "cost": 10, "graphic": "../Graphics/Particles/Heal/Heal.png"}
	}

# Enemies
monster_data = {
	"squid": {"health": 100, "exp": 180, "damage": 20, "attack_type": "slash", "attack_sound": "../Audio/Attack/Slash.wav", "speed": 3, "resistance": 3, "attack_radius": 80, "notice_radius": 360},
	"raccoon": {"health": 300, "exp": 300, "damage": 40, "attack_type": "claw", "attack_sound": "../Audio/Attack/Claw.wav", "speed": 2, "resistance": 3, "attack_radius": 120, "notice_radius": 400},
	"spirit": {"health": 100, "exp": 200, "damage": 8, "attack_type": "thunder", "attack_sound": "../Audio/Attack/Fireball.wav", "speed": 4, "resistance": 3, "attack_radius": 60, "notice_radius": 350},
	"bamboo": {"health": 70, "exp": 150, "damage": 6, "attack_type": "leaf_attack", "attack_sound": "../Audio/Attack/Slash.wav", "speed": 3, "resistance": 3, "attack_radius": 50, "notice_radius": 300}
	}
