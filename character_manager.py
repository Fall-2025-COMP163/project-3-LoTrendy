"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles character creation, loading, and saving.
"""

# character_manager.py
import os
import json
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

SAVE_DIR = os.path.join("data", "save_games")
os.makedirs(SAVE_DIR, exist_ok=True)

VALID_CLASSES = {
    "Warrior": {"max_health": 120, "strength": 15, "magic": 5},
    "Mage": {"max_health": 80,  "strength": 8,  "magic": 20},
    "Rogue": {"max_health": 90,  "strength": 12, "magic": 10},
    "Cleric":{"max_health": 100, "strength": 10, "magic": 15}
}

def create_character(name, character_class):
    """Create a new character dict. Raises InvalidCharacterClassError on invalid class."""
    if character_class not in VALID_CLASSES:
        raise InvalidCharacterClassError(f"Invalid class: {character_class}")

    base = VALID_CLASSES[character_class]
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "health": base["max_health"],
        "max_health": base["max_health"],
        "strength": base["strength"],
        "magic": base["magic"],
        "experience": 0,
        "gold": 100,
        "inventory": [],
        "active_quests": [],
        "completed_quests": [],
        # optional equipment slots
        "equipped_weapon": None,
        "equipped_armor": None
    }
    return character

def _filename_for(name):
    safe = "".join(ch for ch in name if ch.isalnum() or ch in (" ", "_", "-")).rstrip()
    return os.path.join(SAVE_DIR, f"{safe}_save.json")

def save_character(character):
    """Save a character to a JSON file. Returns True."""
    if not isinstance(character, dict) or "name" not in character:
        raise InvalidSaveDataError("Invalid character data for saving.")
    path = _filename_for(character["name"])
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(character, f, indent=2)
        return True
    except PermissionError:
        raise
    except IOError:
        raise

def load_character(character_name):
    """Load a character by name, returns character dict or raises CharacterNotFoundError."""
    path = _filename_for(character_name)
    if not os.path.exists(path):
        raise CharacterNotFoundError(f"No save found for '{character_name}'")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise SaveFileCorruptedError("Save file corrupted")
    # basic validation
    try:
        validate_character_data(data)
    except InvalidSaveDataError:
        raise InvalidSaveDataError("Save file contains invalid character data")
    return data

def list_saved_characters():
    """Return a list of saved character names (without suffix)."""
    if not os.path.isdir(SAVE_DIR):
        return []
    files = [f for f in os.listdir(SAVE_DIR) if f.endswith("_save.json")]
    names = [f[:-10] for f in files]  # remove _save.json
    return names

def delete_character(character_name):
    """Delete a save file for a character."""
    path = _filename_for(character_name)
    if not os.path.exists(path):
        raise CharacterNotFoundError(character_name)
    os.remove(path)
    return True

# ========== Character operations ==========

def gain_experience(character, xp_amount):
    """Add experience and handle level ups. Raises CharacterDeadError if dead."""
    if is_character_dead(character):
        raise CharacterDeadError("Cannot gain XP while dead.")
    xp_amount = int(xp_amount)
    if xp_amount <= 0:
        return
    character["experience"] += xp_amount
    # Level up loop: every level requires level * 100 xp
    while character["experience"] >= character["level"] * 100:
        character["experience"] -= character["level"] * 100
        character["level"] += 1
        character["max_health"] += 10
        character["strength"] += 2
        character["magic"] += 2
        character["health"] = character["max_health"]

def add_gold(character, amount):
    """Add or subtract gold. Raises ValueError if result negative."""
    amount = int(amount)
    new = character.get("gold", 0) + amount
    if new < 0:
        raise ValueError("Not enough gold")
    character["gold"] = new
    return character["gold"]

def heal_character(character, amount):
    """Heal the character; cannot exceed max_health. Returns actual healed amount."""
    amount = int(amount)
    if amount <= 0:
        return 0
    before = character["health"]
    character["health"] = min(character["health"] + amount, character["max_health"])
    return character["health"] - before

def is_character_dead(character):
    return character.get("health", 0) <= 0

def revive_character(character):
    """Revive to 50% max health if dead. Returns True if revived."""
    if not is_character_dead(character):
        return False
    character["health"] = int(max(1, character["max_health"] * 0.5))
    return True

def validate_character_data(character):
    """Ensure required fields exist and types are correct."""
    required_keys = [
        "name", "class", "level", "health", "max_health", "strength",
        "magic", "experience", "gold", "inventory", "active_quests", "completed_quests"
    ]
    if not isinstance(character, dict):
        raise InvalidSaveDataError("Character must be a dict")
    for k in required_keys:
        if k not in character:
            raise InvalidSaveDataError(f"Missing field: {k}")
    # type checks
    ints = ["level", "health", "max_health", "strength", "magic", "experience", "gold"]
    for k in ints:
        if not isinstance(character[k], int):
            raise InvalidSaveDataError(f"Field {k} must be int")
    lists = ["inventory", "active_quests", "completed_quests"]
    for k in lists:
        if not isinstance(character[k], list):
            raise InvalidSaveDataError(f"Field {k} must be list")
    return True

# Simple test runner
if __name__ == "__main__":
    c = create_character("Test", "Warrior")
    save_character(c)
    print("Saved:", list_saved_characters())
    loaded = load_character("Test")
    print("Loaded:", loaded["name"], loaded["class"])


