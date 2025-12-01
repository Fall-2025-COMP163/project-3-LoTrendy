"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]
Used AI to explain isinstance()

This module handles loading and validating game data from text files.
"""

import os
from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

def load_quests(filename="data/quests.txt"):
    """
    Load quest data from file
    
    Expected format per quest (separated by blank lines):
    QUEST_ID: unique_quest_name
    TITLE: Quest Display Title
    DESCRIPTION: Quest description text
    REWARD_XP: 100
    REWARD_GOLD: 50
    REQUIRED_LEVEL: 1
    PREREQUISITE: previous_quest_id (or NONE)
    
    Returns: Dictionary of quests {quest_id: quest_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle:
    # - FileNotFoundError → raise MissingDataFileError
    # - Invalid format → raise InvalidDataFormatError
    # - Corrupted/unreadable data → raise CorruptedDataError
    try:
        data_dict = {}
        quest_data_dict ={}
        with open(filename, "r") as file:
            content = file.readlines()
            for line in content:
                if line == "\n" or line == "":
                    quest_data_dict[key] = data_dict
                    key = ""
                    data_dict = {}
                else:
                    sp_line = line.strip().split(":")
                    if sp_line[0] == "QUEST_ID":
                        key = sp_line[1]
                        data_dict[sp_line[0].lower()] = sp_line[1]
                    elif sp_line[0] == "REQUIRED_LEVEL":
                        data_dict[sp_line[0].lower()] = sp_line[1].strip()
                    else:
                        data_dict[sp_line[0].lower()] = sp_line[1]
            return quest_data_dict
            
    except FileNotFoundError:
        raise MissingDataFileError
    except IndexError:
        raise InvalidDataFormatError
    except SyntaxError:
        raise CorruptedDataError                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

def load_items(filename="data/items.txt"):
    """
    Load item data from file
    
    Expected format per item (separated by blank lines):
    ITEM_ID: unique_item_name
    NAME: Item Display Name
    TYPE: weapon|armor|consumable
    EFFECT: stat_name:value (e.g., strength:5 or health:20)
    COST: 100
    DESCRIPTION: Item description
    
    Returns: Dictionary of items {item_id: item_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle same exceptions as load_quests
    
    try:
        data_dict = {}
        item_data_dict = {}
        with open(filename, "r") as file:
            content = file.readlines()
            for line in content:
                if line == "\n" or line == "":
                    item_data_dict[key] = data_dict
                else:
                    sp_line = line.strip().split(":")
                    if sp_line[0] == "ITEM_ID":
                        key = sp_line[1].strip()
                        data_dict[sp_line[0].lower()] = sp_line[1]
                    elif sp_line[0] == "EFFECT":
                        data_dict[sp_line[0].lower()] = f"{sp_line[1]}:{sp_line[2]}"
                    else:
                        data_dict[sp_line[0].lower()] = sp_line[1]
            return item_data_dict
            
    except FileNotFoundError:
        raise MissingDateFileError
    except SyntaxError:
        raise InvalidDateFormatError
    except NotADirectoryError:
        raise CorruptedDataError        

def validate_quest_data(quest_dict):
    """
    Validate that quest dictionary has all required fields
    
    Required fields: quest_id, title, description, reward_xp, 
                    reward_gold, required_level, prerequisite
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields
    """
    # TODO: Implement validation
    # Check that all required keys exist
    # Check that numeric values are actually numbers
    
    fields = ["quest_id", "title", "description", "reward_xp", "reward_gold", "required_level", "prerequisite"]
    for required in fields:
        if required not in quest_dict:
            raise InvalidDataFormatError
            return None   
        elif required == "reward_xp" or required == "reward_gold" or required == "required_level":
            if not isinstance(quest_dict[required], (int, float)):
                raise InvalidDataFormatError
                return None
    return True

def validate_item_data(item_dict):
    """
    Validate that item dictionary has all required fields
    
    Required fields: item_id, name, type, effect, cost, description
    Valid types: weapon, armor, consumable
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields or invalid type
    """
    # TODO: Implement validation
    fields = ["item_id", "name", "type", "effect", "cost", "description"]
    for required in fields:
        if required not in item_dict or (required == "type" and not (item_dict[required] == "weapon" or item_dict[required] == "armor" or item_dict[required] == "consumable")):
            raise InvalidDataFormatError
            return None
    return True

def create_default_data_files():
    """
    Create default data files if they don't exist
    This helps with initial setup and testing
    """
    # TODO: Implement this function
    # Create data/ directory if it doesn't exist
    # Create default quests.txt and items.txt files
    # Handle any file permission errors appropriately
    quests = "data/quests.txt" 
    items = "data/items.txt"
    try:
        with open(quests, "r") as file:
            contents = file.readlines
        with open(items, "r") as file:
            contents = file.readlines
    except:
        with open(quests, "w") as file:
            contents = file.readlines
        with open(items, "w") as file:
            contents = file.readlines

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_quest_block(lines):
    """
    Parse a block of lines into a quest dictionary
    
    Args:
        lines: List of strings representing one quest
    
    Returns: Dictionary with quest data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    # Split each line on ": " to get key-value pairs
    # Convert numeric strings to integers
    # Handle parsing errors gracefully
    quest_dict = {}
    count = 0
    sp_lines = lines.split(":")
    for line in sp_lines:
        count += 1
        if count % 2 == 1:
            key = line
        else:
            if line.isnumeric():
                quest_dict[key] = int(line)
            else:
                quest_dict[key] = line

def parse_item_block(lines):
    """
    Parse a block of lines into an item dictionary
    
    Args:
        lines: List of strings representing one item
    
    Returns: Dictionary with item data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    item_dict = {}
    count = 0
    sp_lines = lines.split(":")
    for line in sp_lines:
        count += 1
        if count % 2 == 1:
            key = line
        else:
            quest_dict[key] = int(line)

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")
    
    # Test creating default files
    # create_default_data_files()
    
    # Test loading quests
    # try:
    #     quests = load_quests()
    #     print(f"Loaded {len(quests)} quests")
    # except MissingDataFileError:
    #     print("Quest file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid quest format: {e}")
    
    # Test loading items
    # try:
    #     items = load_items()
    #     print(f"Loaded {len(items)} items")
    # except MissingDataFileError:
    #     print("Item file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid item format: {e}")
