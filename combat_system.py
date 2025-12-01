"""
COMP 163 - Project 3: Quest Chronicles
Combat System Module - Starter Code

Name: Christopher Taylor

AI Usage: [Document any AI assistance used]

Handles combat mechanics
"""
import random

from custom_exceptions import (
    InvalidTargetError,
    CombatNotActiveError,
    CharacterDeadError,
    AbilityOnCooldownError
)

# ============================================================================
# ENEMY DEFINITIONS
# ============================================================================

def create_enemy(enemy_type):
    """
    Create an enemy based on type
    
    Example enemy types and stats:
    - goblin: health=50, strength=8, magic=2, xp_reward=25, gold_reward=10
    - orc: health=80, strength=12, magic=5, xp_reward=50, gold_reward=25
    - dragon: health=200, strength=25, magic=15, xp_reward=200, gold_reward=100
    
    Returns: Enemy dictionary
    Raises: InvalidTargetError if enemy_type not recognized
    """
    # TODO: Implement enemy creation
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    enemy_dict = {}
    if enemy_type == "goblin":
        enemy_dict = {"name":"Goblin", "health":50, "strength":8, "magic":2, "xp_reward":25, "gold_reward":10}
    elif enemy_type == "orc":
        enemy_dict = {"name":"Orc", "health":80, "strength":12, "magic":5, "xp_reward":50, "gold_reward":25}
    elif enemy_type == "dragon":
        enemy_dict = {"name":"Dragon", "health":200, "strength":25, "magic":15, "xp_reward":200, "gold_reward":100}
    elif enemy_type == "wolverine":
        enemy_dict = {"name":"Wolverine", "health":150, "strength":16, "magic":15, "xp_reward":120, "gold_reward":80}
    elif enemy_type == "vampire":
        enemy_dict = enemy_dict = {"name":"Vampire", "health":280, "strength":20, "magic":20, "xp_reward":280, "gold_reward":300}
    else:
        raise InvalidTargetError
    return enemy_dict

def get_random_enemy_for_level(character_level):
    """
    Get an appropriate enemy for character's level
    
    Level 1-2: Goblins
    Level 3-5: Orcs
    Level 6+: Dragons
    Level 7+: Wolverines
    Level 10+: Vampires
    Returns: Enemy dictionary
    """
    # TODO: Implement level-appropriate enemy selection
    # Use if/elif/else to select enemy type
    # Call create_enemy with appropriate type

    if 1 <= character["level"] <= 2:
        return create_enemy("goblin")
    elif 3 <= character["level"] <= 5:
        return create_enemy("orc")
    elif character["level"] >= 6:
        return create_enemy("dragon")
    elif character["level"] >= 7:
        return create_enemy("wolverine")
    elif character["level"] >= 10:
        return create_enemy("vampire")

# ============================================================================
# COMBAT SYSTEM
# ============================================================================

class SimpleBattle:
    """
    Simple turn-based combat system
    
    Manages combat between character and enemy
    """
    
    def __init__(self, character, enemy):
        """Initialize battle with character and enemy"""
        # TODO: Implement initialization
        # Store character and enemy
        # Set combat_active flag
        # Initialize turn counter
    
        self.character = character
        self.enemy = enemy
        self.combat_active = True
        self.turn_counter = 1

    def start_battle(self):
        """
        Start the combat loop
        
        Returns: Dictionary with battle results:
                {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
        
        Raises: CharacterDeadError if character is already dead
        """
        # TODO: Implement battle loop
        # Check character isn't dead
        # Loop until someone dies
        # Award XP and gold if player wins
        if character["health"] <= 0:
            raise CharacterDeadError
        elif enemy["health"] <= 0:
            return {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
            
    
    def player_turn(self):
        """
        Handle player's turn
        
        Displays options:
        1. Basic Attack
        2. Special Ability (if available)
        3. Try to Run
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement player turn
        # Check combat is active
        # Display options
        # Get player choice
        # Execute chosen action
        if self.combat_active == True:
            choice = input("1. Basic Attack\n2. Special Ability (if available)\n3. Try to Run")
            if choice == "1":
                damage = calculate_damage(self.character, self.enemy)
                apply_damage(damage, self.enemy)
            elif choice == "2":
                use_special_ability(self.character, self.enemy)
            elif choice == "3":
                attempt_escape()
        else:
            raise CombatNotActiveError
    
    def enemy_turn(self):
        """
        Handle enemy's turn - simple AI
        
        Enemy always attacks
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement enemy turn
        # Check combat is active
        # Calculate damage
        # Apply to character
        if self.enemy == "vampire":
            damage = calculate_damage(self.enemy, self.character)
            apply_damage(damage, self.character)
            enemy += 8.5
        else:
            damage = calculate_damage(self.enemy, self.character)
            apply_damage(damage, self.character)
    
    def calculate_damage(self, attacker, defender):
        """
        Calculate damage from attack
        
        Damage formula: attacker['strength'] - (defender['strength'] // 4)
        Minimum damage: 1
        
        Returns: Integer damage amount
        """
        # TODO: Implement damage calculation
        damage = attacker['strength'] - (defender['strength'] // 4)
        if damage >= 1:
            return damage
        else:
            return 1
    
    def apply_damage(self, target, damage):
        """
        Apply damage to a character or enemy
        
        Reduces health, prevents negative health
        """
        # TODO: Implement damage application
        if (target["health"] - damage) > 0:
            target["health"] -= damage
        else:
            target["health"] = 0
    
    def check_battle_end(self):
        """
        Check if battle is over
        
        Returns: 'player' if enemy dead, 'enemy' if character dead, None if ongoing
        """
        # TODO: Implement battle end check
        if player["health"] == 0:
            return "enemy"
        elif enemy["health"] == 0:
            return "player"
    
    def attempt_escape(self):
        """
        Try to escape from battle
        
        50% success chance
        
        Returns: True if escaped, False if failed
        """
        # TODO: Implement escape attempt
        # Use random number or simple calculation
        # If successful, set combat_active to False
        ran_num = ramdom.randomint(1, 100)
        if 1 <= ran_num <= 50:
            return True
        else:
            return False

# ============================================================================
# SPECIAL ABILITIES
# ============================================================================

def use_special_ability(character, enemy):
    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)
    if character["class"] == "Warrior":
        warrior_power_strike(character, enemy)
        return "Powerful blow towards enemy"
    elif character["class"] == "Mage":
        mage_fireball(character, enemy)
        return "Fireball towards enemy"
    elif character["class"] == "Rogue":
        rogue_critical_strike(character, enemy)
        return "Critical Hit on enemy"
    elif character["class"] == "Cleric":
        cleric_heal(character)
        return "Character got healed"

def warrior_power_strike(character, enemy):
    """Warrior special ability"""
    # TODO: Implement power strike
    # Double strength damage
    enemy["health"] -= (character['strength'] - (enemy['strength'] // 4) * 2)

def mage_fireball(character, enemy):
    """Mage special ability"""
    # TODO: Implement fireball
    # Double magic damage
    enemy["health"] -= (character['magic'] - (enemy['magic'] // 4) * 2)

def rogue_critical_strike(character, enemy):
    """Rogue special ability"""
    # TODO: Implement critical strike
    # 50% chance for triple damage
    if 1 <= ran_num <= 50:
        enemy["health"] -= (character['strength'] - (enemy['strength'] // 4) * 3)
    else:
        enemy["health"] -= character["strength"]

def cleric_heal(character):
    """Cleric special ability"""
    # TODO: Implement healing
    # Restore 30 HP (not exceeding max_health)
    if character["health"] + 30 <= character["max_health"]:
        character["health"] += 30
    else:
        character["health"] = character["max_health"]

# ============================================================================
# COMBAT UTILITIES
# ============================================================================

def can_character_fight(character):
    """
    Check if character is in condition to fight
    
    Returns: True if health > 0 and not in battle
    """
    # TODO: Implement fight check
    if character["health"] > 0 and self.combat_active == False:
        return True
    else:
        return False

def get_victory_rewards(enemy):
    """
    Calculate rewards for defeating enemy
    
    Returns: Dictionary with 'xp' and 'gold'
    """
    # TODO: Implement reward calculation
    return {"xp":enemy["xp_reward"], "gold":enemy["gold_reward"]}

def display_combat_stats(character, enemy):
    """
    Display current combat status
    
    Shows both character and enemy health/stats
    """
    # TODO: Implement status display
    print(f"\n{character['name']}: HP={character['health']}/{character['max_health']}")
    print(f"{enemy['name']}: HP={enemy['health']}/{enemy['max_health']}")
    

def display_battle_log(message):
    """
    Display a formatted battle message
    """
    # TODO: Implement battle log display
    print(f">>> {message}")

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== COMBAT SYSTEM TEST ===")
    
    # Test enemy creation
    # try:
    #     goblin = create_enemy("goblin")
    #     print(f"Created {goblin['name']}")
    # except InvalidTargetError as e:
    #     print(f"Invalid enemy: {e}")
    
    # Test battle
    # test_char = {
    #     'name': 'Hero',
    #     'class': 'Warrior',
    #     'health': 120,
    #     'max_health': 120,
    #     'strength': 15,
    #     'magic': 5
    # }
    #
    # battle = SimpleBattle(test_char, goblin)
    # try:
    #     result = battle.start_battle()
    #     print(f"Battle result: {result}")
    # except CharacterDeadError:
    #     print("Character is dead!")
