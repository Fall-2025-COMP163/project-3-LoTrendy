"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles character creation, loading, and saving.
"""

# character_manager.py
import os
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    
    character_dict = {"name":name, "class":character_class, "level":1, "health":0,"max_health":0, "strength":0, "magic":0, "experience":0, "gold":100, "inventory":[], "active_quests":[], "completed_quests":[]}
    if character_class == "Warrior":
        character_dict["max_health"] = 120
        character_dict["health"] = 120
        character_dict["strength"] = 15
        character_dict["magic"] = 5
        return character_dict
    elif character_class == "Mage":
        character_dict["max_health"] = 80
        character_dict["health"] = 80
        character_dict["strength"] = 8
        character_dict["magic"] = 20
        return character_dict
    elif character_class == "Rogue":
        character_dict["max_health"] = 90
        character_dict["health"] = 90
        character_dict["strength"] = 12
        character_dict["magic"] = 10
        return character_dict
    elif character_class == "Cleric":
        character_dict["max_health"] = 100
        character_dict["health"] = 100
        character_dict["strength"] = 10
        character_dict["magic"] = 15
        return character_dict
    else:
        raise InvalidCharacterClassError
        


def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    items = ""
    act_quests = ""
    comp_quests = ""
    for item in character["inventory"]:
        items += item
    for quest in character["active_quests"]:
        act_quests += quest
    for quest in character["completed_quests"]:
        comp_quests += quest
    filename = f"{character["name"]}_save.txt"
    try:
        full_path = os.path.join(save_directory, filename)
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
            with open(full_path, 'w') as f:
                f.write(f"NAME:{character["name"]}\nCLASS:{character["class"]}\nLEVEL:{character["level"]}\nHEALTH:{character["health"]}\nMAX_HEALTH:{character["max_health"]}\nSTRENGTH:{character["strength"]}\nMAGIC:{character["magic"]}\nEXPERIENCE: {character["experience"]}\nGOLD:{character["gold"]}\nINVENTORY:{items}\nACTIVE_QUESTS:{act_quests}\nCOMPLETED_QUESTS:{comp_quests}")
                return True
    except PermissionError:
        raise PermissionError
    except IOError:
        raise IOError

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    
    filename = f"{character_name}_save.txt"
    full_path = os.path.join(save_directory, filename)
    char_dict = {}
    try:
        with open(full_path, "r") as file:
            read = file.readlines()
            for line in read:
                if "," in line:
                    sp_line = line.strip().split(":")
                    sp_line[1] = sp_line[1].split(",")
                    char_dict[sp_line[0].lower()] = sp_line[1]
                else:
                    sp_line = line.strip().split(":")
                    char_dict[sp_line[0].lower()] = sp_line[1]
            return char_dict                
                    
    except FileNotFoundError:
        raise CharacterNotFoundError
    except SyntaxError:
        raise InvalidDateFormatError
    except NotADirectoryError:
        raise CorruptedDataError  
        
def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    with open(filename, "r") as file:
        content = file.read()
        return content

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    pass
        

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    if not is_character_dead(character):
        character["experience"] += int(xp_amount)
        levels = (character["level"] * 100) // int(xp_amount)
        for i in range(levels):
            character["level"] += 1
            character["max_health"] += 10
            character["strength"] += 2
            character["magic"] += 2
            character["health"] = character["max_health"]
    else:
        raise CharacterDeadError
        
        

def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    if character["gold"] + int(amount) > 0:
        character["gold"] += int(amount)
    else:
        raise ValueError

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    return amount

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    if character["health"] <= 0:
        return True
    else:
        return False

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health

    if is_dead(character):
        character["health"] = character["max_health"] * 0.50
        return True
# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    try:
        character["name"]
        character["class"]
        isinstance(character["level"], int)
        isinstance(character["health"], int)
        isinstance(character["max_health"], int)
        isinstance(character["strength"], int)
        isinstance(character["magic"], int)
        isinstance(character["experience"], int)
        isinstance(character["gold"], int)
        isinstance(character["inventory"], list)
        isinstance(character["active_quests"], list)
        isinstance(character["completed_quests"], list)
        return True
    except:
        raise InvalidSaveDataError

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")
    
    # Test character creation
    # try:
    #     char = create_character("TestHero", "Warrior")
    #     print(f"Created: {char['name']} the {char['class']}")
    #     print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    # except InvalidCharacterClassError as e:
    #     print(f"Invalid class: {e}")
    
    # Test saving
    # try:
    #     save_character(char)
    #     print("Character saved successfully")
    # except Exception as e:
    #     print(f"Save error: {e}")
    
    # Test loading
    # try:
    #     loaded = load_character("TestHero")
    #     print(f"Loaded: {loaded['name']}")
    # except CharacterNotFoundError:
    #     print("Character not found")
    # except SaveFileCorruptedError:
    #     print("Save file corrupted")
