# 1510-term-project

## Your names:

- Yifei Zeng
- Cai Chun (Steven) Yan

## Your student numbers:

- A01375821

## Your GitHub usernames:

- zengyifei327
- thebiggest0

## Important Notes:
Please run unit tests before play the game, as create new characters will modify json file.

for example, test_random_enemy will fail unit test if enemy difficulty is not on easy.

## Required Information

| Required elements                | Location of elements                                                                              |
|----------------------------------|---------------------------------------------------------------------------------------------------|
| Dictionary comprehension         | Package: enemy<br/>Module: enemy.py <br/>Function: create_enemy() <br/>Line: 22                   |
| Itertools                        | Package: introduction<br/>Module: game_start.py <br/>Function: warm_up_questions() <br/>Line: 123 |
| Auto save in json file           | Package: save<br/>Module: save_data.py                                                            |
| Immutable data structure - tuple | Package: character_actions<br/>Module: move.py <br/>Function: check_valid_move() <br/>Line: 113   |
| Mutable data structure - list    | Package: character<br/>Module: character.py <br/>Function: stat_increase() <br/>Line: 67          |
| For loop                         | Package: character<br/>Module: character.py <br/>Function: stat_increase() <br/>Line: 68          |
| If statement                     | Package: character<br/>Module: character.py <br/>Function: level_up() <br/>Line: 48               |
| Random module                    | Package: character_actions<br/>Module: trivia.py <br/>Function: star_wars_trivia() <br/>Line: 30  |
| Exception                        | Package: character_actions<br/>Module: combat.py <br/>Function: is_valid_choice() <br/>Line: 48   |
| F-string                         | Package: character<br/>Module: character.py <br/>Function: stat_increase() <br/>Line: 72          |
| Range                            | Package: character_actions<br/>Module: move.py <br/>Function: print_map() <br/>Line: 87           |
| Membership operator              | Package: introduction<br/>Module: game_start.py <br/>Function: difficulty_checker() <br/>Line: 92 |
| Function annotation              | Package: character<br/>Module: character.py <br/>Function: create_character() <br/>Line: 8        |
| GUI                              | game_with_GUI.py                                                                                  |


## Game Controls and Key Symbols

Welcome to the game! This section provides you with the essential controls and key symbols you will encounter throughout your adventure. Master these to navigate effectively and conquer challenges that lie ahead.

## Character Controls

    Movement: Use the W, A, S, D keys to move your character in the desired direction.
    Check Stats: Press the Q key to view your current stats, including HP, STR, INT, experience and levels.

## Key Symbols

    X: This symbol represents your character. It's your avatar in this epic journey.
    P: (Palpatine): Encounter with the final boss. Prepare for a challenging battle.
    V: (Darth Vader): This symbol denotes the second boss. A formidable opponent requiring strategy and strength.
    O: Represents mini-bosses like Count Dooku and General Grievous. Each mini-boss offers unique challenges.
    J: (Force Ghost): These are fallen jedi masters that provide unlimited healing and stat bonus. Answer their questions correctly to gain their aid.
    #: These are walls within the game. They define boundaries and obstacles in your path.

## Level system

    Players start at Level 1 and progress up to Level 5.
    To level up, players must earn experience points through combat with enemies.
    The experience requirements for each level are as follows:
        Level 1 to 2: 100 XP
        Level 2 to 3: 200 XP
        Level 3 to 4: 300 XP
        Level 4 to 5: 500 XP

        Level 1: Youngling
        Level 2: Padawan
        Level 3: Jedi Knight
        Level 4: Jedi Master
        Level 5: Jedi Grandmaster

    Upon reaching a new level, players will experience an enhancement in their abilities: 
    Each level up results in the player's current stats and HP increasing by a factor of 1.2.

## Game Secrets

    1. Force Ghosts do not disappear, players can interact with them multiple times to gain boots and healing
    2. Stat increase from the Froce Ghost is random, so constantly check your Stats with 'q' and use the higher value
    3. The highest obtainable level is 5, the more states you have at the time of level up the higher the bonus
    4. Physical attack is corolated to your strength while force attack is corrolated with your intelegence
    5. At anytime in the game, if your HP reaches 0 you will lose and your character will be deleted

## Game Save

    Our game supports multiple player accounts. Please make sure to create different character names. Each difficulty can
    only be experienced one at a time (when new difficulty is selected the existing enemy.json file will be updated). 
    
    Your game will auto save after a successful character movement, level up, battle and interaction. Exit the game and log
    back in by entering the same character name.

## Game Lore

    After narrowly escaping the treacherous Order 66, you arrive back on the planet of Coruscant. 
    The once-thriving heart of the Galactic Republic now casts a shadow of despair, signaling the fall of the Jedi 
    Order. The Dark Side's grip tightens over the galaxy, with Emperor Palpatine rising in power.

## Mission

    Your journey begins amidst the towering skyscrapers and neon-lit streets of Coruscant. As a surviving Jedi, your 
    mission is to navigate through this vast urban landscape, evading the clutches of the new regime, and make your 
    way to the Jedi Temple.

    The temple, once a symbol of hope is now in ruins. It is here that you must confront the ultimate embodiment of 
    evil, Emperor Palpatine himself. Defeat him, and you could restore balance to the Force, reviving hope in a galaxy 
    plunged into darkness.

## Gameplay

    Explore Coruscant: Traverse through the map and make your way into the jedi temple.
    Stealth and Strategy: Choose to fight your way into the jedi temple or take a stealthy approach instead.
    Combat and Skills: Engage in lightsaber duels and harness your Force abilities to overcome obstacles and enemies.
    Epic Confrontation: Face Emperor Palpatine, Darth Vador, General Grevious and more in an epic show down to restore balance to the force.

    Will you be the beacon of light in these dark times? Embark on this journey, outmaneuver the forces of darkness, 
    and carve a path to victory. Your legacy as a Jedi awaits.

## Retrospective

- We attempted the GUI and was not able to fully implement it.
If we had more time, we wish to create more dialogue and interactive elements in the game as well as enhance combat
and make our save system work for different levels as well.
- When we run unit tests, it will modify json file somehow, if we delete players in character.json, some unit 
  tests will fail
- Due to our limited experience with json we have tried our best to unit test a dynamic data set.
