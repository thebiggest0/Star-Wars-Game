"""
Change character status.
"""
from save import save_data


def create_character(name):
    """
    Create a character with specified attributes.

    :param name: a non-empty string, name of the character user entered
    :precondition: name must be a non-empty string
    :postcondition: create a character dict with specified attributes
    :return: a dict, with specified attributes
    >>> create_character('Thor')
    {'name': 'Thor', 'level': 1, 'experience': 0, 'hp': 50, 'str': 15, 'int': 15, 'x-coordinate': 0, 'y-coordinate': 0}
    >>> create_character('Loki')
    {'name': 'Loki', 'level': 1, 'experience': 0, 'hp': 50, 'str': 15, 'int': 15, 'x-coordinate': 0, 'y-coordinate': 0}
    """
    character_info = {
        'name': name,
        'level': 1,
        'experience': 0,
        'hp': 50,
        'str': 15,
        'int': 15,
        'x-coordinate': 10,
        "y-coordinate": 11
    }
    return character_info


def level_up(character_info):
    """
    Increase level of the character if it reached certain experience.

    :param character_info: a dict containing the character's attributes
    :precondition: character_info must be a dict containing the character's attributes
    :postcondition: increase level of the character in the dict if it reached certain experience, else the dict stay
    unchanged
    :return: a dict with updated level if the character reached certain experience, else the dict stay
    unchanged
    """
    experience_check = [100, 200, 300, 500]
    if experience_check[character_info['level'] - 1] <= character_info['experience']:
        character_info['experience'] -= experience_check[character_info['level'] - 1]
        character_info['level'] += 1
        print(f'Congratulations {character_info["name"]}! you\'ve leveled up!')
        stat_increase(character_info)
    return character_info


def stat_increase(character_info):
    """
    Increase stats of the character.

    :precondition: character leveled up
    :postcondition: increase player hp by 10%
    :postcondition: increase player stats by 20%
    :postcondition: print something to the screen
    """
    character_info['hp'] = int(character_info['hp'] * 1.2)
    stats = ['str', 'int']
    for stat in stats:
        character_info[stat] = int(character_info[stat] * 1.1)
    save_data.save_game(character_info)
    print('Your stats have increased!')
    print(f'HP: {character_info["hp"]} \nSTR: {character_info["str"]} \nINT: {character_info["int"]} ')


def check_stats(character):
    print(f'Character STR: {character["str"]} INT: {character["int"]}')
    print(f'Character HP: {character["hp"]}')
    print(f'LEVEL: {character["level"]} EXP: {character["experience"]}')


def main():
    """
    Drive the program.
    """
    name = 'Yoda'
    character = create_character(name)
    level_up(character)
    stat_increase(character)


if __name__ == "__main__":
    main()