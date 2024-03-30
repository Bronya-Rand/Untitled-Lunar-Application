from character import Character
from environment import VERSION, LAST_UPDATE, LAST_HSR_UPDATE
from datetime import datetime
from exceptions import (
    UnknownRelicType,
    InvalidRelicRank,
    InvalidRelicLevel,
    SubstatSameAsMain,
    DuplicateSubstat,
)
from enums import (
    Characters,
    MainSubstats,
    RelicSet,
    RelicType,
    SURRelicSet,
)
from relics import (
    RelicsComponent,
    choose_main_stat,
    choose_substat,
    set_relic_rank,
    set_relic_substat_rank,
    set_relic_type,
    set_rs,
)
import os

# If anyone is looking at the source code, no this is not my favorite
# characters (cept Bronya) nor the team I run in H:SR. These are just
# placeholder characters.
CHARACTER_TEAM = {
    1: Character(Characters.MARCH_7TH),
    2: Character(Characters.BRONYA),
    3: Character(Characters.QINGQUE),
    4: Character(Characters.GALLAGHER),
}

SELECTED_CHARACTER = 1
SELECTED_RELIC_SLOT = 0


def change_team():
    """
    Displays the current team and prompts the user to select a character slot to change.

    If the user enters -1, the function returns and goes back to the main menu.
    If the selected character slot is invalid, an error message is displayed and the function is called recursively.

    Returns:
        None
    """
    print("Current Team:")
    print_team()

    choice = int(
        input(
            "Select a character slot to change (Type `-1` to return to the Main Menu): "
        )
    )

    if choice == -1:
        return

    if choice not in CHARACTER_TEAM:
        _ = os.system("cls")
        print("Invalid character slot. Please try again.\n")
        return change_team()

    def choose_new_character():
        print(f"Character List (as of H:SR {LAST_HSR_UPDATE}):")
        for characters in Characters:
            print(f"{characters.value[0]} - {characters.value[1]}")

        print(
            f"\nCurrent Character in Slot: {CHARACTER_TEAM[choice].get_character_name()}"
        )
        new_character = int(
            input(
                "Select the new character you want to switch to (Type `-1` to return to the Main Menu): "
            )
        )

        if (
            new_character == -1
            or new_character == CHARACTER_TEAM[choice].get_character_id()
        ):
            return None

        for character in Characters:
            if character.value[0] == new_character:
                return character

        _ = os.system("cls")
        print("Invalid character. Please try again.\n")
        return choose_new_character()

    new_character = choose_new_character()

    if new_character is None:
        return

    old_char_name = CHARACTER_TEAM[choice].get_character_name()
    CHARACTER_TEAM[choice].set_character(new_character)

    _ = os.system("cls")
    print(
        f"Changed Character Slot {choice} from {old_char_name} to {CHARACTER_TEAM[choice].get_character_name()}\n"
    )
    return


def change_current_character():
    """
    Displays the list of characters and prompts the user to select a new character to switch to in the current slot.

    If the user selects -1 or the current character, the function returns without making any changes.
    If the user selects a valid character, the current character is updated and a success message is printed.
    If the user selects an invalid character, an error message is printed and the function is called recursively.

    Returns:
        None
    """
    print(f"Character List (as of H:SR {LAST_HSR_UPDATE}):")
    for characters in Characters:
        print(f"{characters.value[0]} - {characters.value[1]}")

    print(
        f"\nCurrent Character in Slot: {CHARACTER_TEAM[SELECTED_CHARACTER].get_character_name()}"
    )
    new_character = int(
        input(
            "Select the new character you want to switch to (Type `-1` to return to the Main Menu): "
        )
    )

    if (
        new_character == -1
        or new_character == CHARACTER_TEAM[SELECTED_CHARACTER].get_character_id()
    ):
        _ = os.system("cls")
        print("Current character slot unchanged.\n")
        return

    for character in Characters:
        if character.value[0] == new_character:
            old_char_name = CHARACTER_TEAM[SELECTED_CHARACTER].get_character_name()
            CHARACTER_TEAM[SELECTED_CHARACTER].set_character(character)

            _ = os.system("cls")
            print(
                f"Changed Current Character from {old_char_name} to {CHARACTER_TEAM[SELECTED_CHARACTER].get_character_name()}\n"
            )
            return

    _ = os.system("cls")
    print("Invalid character. Please try again.\n")
    return change_current_character()


def change_relic_slot():
    """
    Changes the selected relic slot.

    Returns:
        None
    """
    global SELECTED_RELIC_SLOT
    _ = os.system("cls")
    print(f"Current Relic Slot: {SELECTED_RELIC_SLOT+1}\n")

    new_relic_slot = int(input("Select a relic slot: ")) - 1

    if new_relic_slot < 0 or new_relic_slot > 5:
        _ = os.system("cls")
        print("Invalid relic slot. Please try again.\n")
        change_relic_slot()

    old_relic_slot = SELECTED_RELIC_SLOT + 1
    SELECTED_RELIC_SLOT = new_relic_slot
    _ = os.system("cls")
    print(
        f"Changed Current Relic Slot from {old_relic_slot} to {SELECTED_RELIC_SLOT+1}\n"
    )
    return


def display_relics():
    """
    Displays the current relics equipped for the selected character.

    Prints the relic slot, relic set, relic rank, relic level, main stat, and substats for each equipped relic.

    Returns:
        None
    """
    _ = os.system("cls")
    print(
        f"Current Relics Equipped for {CHARACTER_TEAM[SELECTED_CHARACTER].get_character_name()}:"
    )
    for i, relic in enumerate(CHARACTER_TEAM[SELECTED_CHARACTER].relics):
        print(
            f"Relic Slot {i+1}: {relic.relic_set.value[1]} (Rank: {relic.relic_rank} - Level {relic.relic_level})"
        )
        print(f"Main Stat: {relic.main_stat.stat.value[1]}")
        print(
            f"Substats: {relic.substats[0].stat.value[1]}, {relic.substats[1].stat.value[1]}, {relic.substats[2].stat.value[1]}, {relic.substats[3].stat.value[1]}\n"
        )

    _ = input("Press any key to return to the Main Menu...")
    _ = os.system("cls")
    return


def create_new_relic():
    """
    Creates a new relic based on user input.

    Depending on the user's choice, it calls different functions to create different types of relics.
    If the user chooses to return to the main menu, the function exits.

    Returns:
        None
    """
    print("Relic Options:")

    print("1. Create a Level 0 Relic")
    print("2. Create a Level 15 Relic")
    print("3. Create a Level 60 Relic")
    print("4. Create a Custom Relic\n")

    choice = int(input("Choose an option (Type `-1` to return to the Main Menu): "))
    match choice:
        case 1:
            create_standard_relic()
        case 2:
            create_max_relic()
        case 3:
            warn_choice = int(
                input(
                    "Warning: Penta-BIS Relics will be set as Level 0 with Max Substat Levels (5).\nAscending to +15 will make the Relic (in theory) +75 with some substats at (6-10). These relics will be overkill against most content in H:SR.\nContinue with making a Penta-BIS Relic? (1 - Yes, -1 - No): "
                )
            )
            if warn_choice != 1:
                _ = os.system("cls")
                return create_new_relic()
            create_penta_bis_relic()
        case 4:
            create_custom_relic()
        case -1:
            _ = os.system("cls")
            print("Returning to the Main Menu...\n")
            return
        case _:
            _ = os.system("cls")
            print("Invalid choice. Please try again.\n")
            create_new_relic()
    return


def create_custom_relic():
    """
    Creates a custom relic using user provided values.

    Returns:
        None
    """
    new_relic = RelicsComponent()

    # See if the user wants to create a Simulated Universe Relic
    su_choice = int(
        input(
            "Do you wish to create a Simulated Universe Relic? (1 - Yes | 0 - No) (Type `-1` to return to the Main Menu): "
        )
    )

    if su_choice == -1:
        _ = os.system("cls")
        return

    relic_enum = RelicSet
    # If the user wants to create a SU relic, set the relic_enum to SURRelicSet instead
    if su_choice == 1:
        new_relic.set_su_relic()

    # Changes the print statement to reflect the relic set list
    if new_relic.is_su_relic:
        relic_enum = SURRelicSet
        print(f"Simulated Universe Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")
    else:
        print(f"Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")

    # Set the relic set
    relic_set = set_rs(relic_enum)

    if relic_set is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_set(relic_set)

    # Set the relic type
    relic_type = set_relic_type(new_relic.is_su_relic)

    if relic_type is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_type(relic_type)

    # Set the relic rank
    relic_rank = set_relic_rank()
    if relic_rank is None:
        _ = os.system("cls")
        return
    new_relic.set_relic_rank(relic_rank)

    # Set the relic level
    def set_relic_level():
        relic_level = int(input("Enter the relic level (0 - 15): "))

        if relic_level < 0 or relic_level > 15:
            _ = os.system("cls")
            print("Invalid relic level. Please try again.\n")
            return set_relic_level()
        return relic_level

    relic_level = set_relic_level()

    new_relic.set_relic_level(relic_level)

    # Set the main stat
    # If the relic type is HEAD or HAND, set the main stat to HP or ATK flat respectively
    if new_relic.relic_type == RelicType.HEAD or new_relic.relic_type == RelicType.HAND:
        if new_relic.relic_type == RelicType.HEAD:
            new_relic.set_main_stat(MainSubstats.HP_FLAT)
        else:
            new_relic.set_main_stat(MainSubstats.ATK_FLAT)
    else:
        _ = os.system("cls")

        main_stat = choose_main_stat(
            relic_type=new_relic.relic_type, su=new_relic.is_su_relic
        )

        if main_stat is None:
            _ = os.system("cls")
            return

        new_relic.set_main_stat(main_stat)

    # Set the substats
    for i in range(4):
        substat = choose_substat(i + 1)

        if substat is None:
            _ = os.system("cls")
            return

        new_relic.set_substat(substat, i)
        substat_rank = set_relic_substat_rank()

        if substat_rank is None:
            _ = os.system("cls")
            return

        new_relic.set_substat_rank(substat_rank, i)

    print("Validating Relic Information...")
    result = True
    err = None

    # Validate the relic information
    try:
        new_relic.validate()
    except UnknownRelicType as e:
        result = False
        err = e
    except InvalidRelicRank as e:
        result = False
        err = e
    except InvalidRelicLevel as e:
        result = False
        err = e
    except SubstatSameAsMain as e:
        result = False
        err = e
    except DuplicateSubstat as e:
        result = False
        err = e
    except Exception as e:
        result = False
        err = e

    # If the relic information is valid, set the relic for the selected character and slot
    if result:
        _ = os.system("cls")
        print("Relic Information Valid for H:SR!\n")
        CHARACTER_TEAM[SELECTED_CHARACTER].relics[SELECTED_RELIC_SLOT] = new_relic
        return
    else:
        _ = os.system("cls")
        print("Invalid Relic Information. Please try again.")
        print(f"Error Reason: {err}\n")
        return create_custom_relic()


def create_standard_relic():
    """
    Creates a standard +0 relic.

    Returns:
        None
    """
    new_relic = RelicsComponent()

    su_choice = int(
        input(
            "Do you wish to create a Simulated Universe Relic? (1 - Yes | 0 - No) (Type `-1` to return to the Main Menu): "
        )
    )

    if su_choice == -1:
        _ = os.system("cls")
        return

    relic_enum = RelicSet
    if su_choice == 1:
        new_relic.set_su_relic()

    if new_relic.is_su_relic:
        relic_enum = SURRelicSet
        print(f"Simulated Universe Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")
    else:
        print(f"Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")

    relic_set = set_rs(relic_enum)

    if relic_set is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_set(relic_set)

    relic_type = set_relic_type(new_relic.is_su_relic)

    if relic_type is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_type(relic_type)

    relic_rank = set_relic_rank()
    if relic_rank is None:
        _ = os.system("cls")
        return
    new_relic.set_relic_rank(relic_rank)

    new_relic.set_relic_level(0)

    if new_relic.relic_type == RelicType.HEAD or new_relic.relic_type == RelicType.HAND:
        if new_relic.relic_type == RelicType.HEAD:
            new_relic.set_main_stat(MainSubstats.HP_FLAT)
        else:
            new_relic.set_main_stat(MainSubstats.ATK_FLAT)
    else:
        _ = os.system("cls")

        main_stat = choose_main_stat(
            relic_type=new_relic.relic_type, su=new_relic.is_su_relic
        )

        if main_stat is None:
            _ = os.system("cls")
            return

        new_relic.set_main_stat(main_stat)

    for i in range(4):
        substat = choose_substat(i + 1)

        if substat is None:
            _ = os.system("cls")
            return

        new_relic.set_substat(substat, i)
        new_relic.set_substat_rank(1, i)

    print("Validating Relic Information...")

    result = True
    err = None
    try:
        new_relic.validate()
    except UnknownRelicType as e:
        result = False
        err = e
    except InvalidRelicRank as e:
        result = False
        err = e
    except InvalidRelicLevel as e:
        result = False
        err = e
    except SubstatSameAsMain as e:
        result = False
        err = e
    except DuplicateSubstat as e:
        result = False
        err = e
    except Exception as e:
        result = False
        err = e

    if result:
        _ = os.system("cls")
        print("Relic Information Valid for H:SR!\n")
        CHARACTER_TEAM[SELECTED_CHARACTER].relics[SELECTED_RELIC_SLOT] = new_relic
        return
    else:
        _ = os.system("cls")
        print("Invalid Relic Information. Please try again.")
        print(f"Error Reason: {err}\n")
        return create_standard_relic()


def create_max_relic():
    """
    Creates a max +15 relic.

    Returns:
        None
    """
    new_relic = RelicsComponent()

    su_choice = int(
        input(
            "Do you wish to create a Simulated Universe Relic? (1 - Yes | 0 - No) (Type `-1` to return to the Main Menu): "
        )
    )

    if su_choice == -1:
        _ = os.system("cls")
        return

    relic_enum = RelicSet
    if su_choice == 1:
        new_relic.set_su_relic()

    if new_relic.is_su_relic:
        relic_enum = SURRelicSet
        print(f"Simulated Universe Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")
    else:
        print(f"Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")

    relic_set = set_rs(relic_enum)

    if relic_set is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_set(relic_set)

    relic_type = set_relic_type(new_relic.is_su_relic)

    if relic_type is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_type(relic_type)

    relic_rank = set_relic_rank()
    if relic_rank is None:
        _ = os.system("cls")
        return
    new_relic.set_relic_rank(relic_rank)

    new_relic.set_relic_level(15)

    if new_relic.relic_type == RelicType.HEAD or new_relic.relic_type == RelicType.HAND:
        if new_relic.relic_type == RelicType.HEAD:
            new_relic.set_main_stat(MainSubstats.HP_FLAT)
        else:
            new_relic.set_main_stat(MainSubstats.ATK_FLAT)
    else:
        _ = os.system("cls")

        main_stat = choose_main_stat(
            relic_type=new_relic.relic_type, su=new_relic.is_su_relic
        )

        if main_stat is None:
            _ = os.system("cls")
            return

        new_relic.set_main_stat(main_stat)

    for i in range(4):
        substat = choose_substat(i + 1)

        if substat is None:
            _ = os.system("cls")
            return

        new_relic.set_substat(substat, i)
        new_relic.set_substat_rank(5, i)

    print("Validating Relic Information...")
    result = True
    err = None
    try:
        new_relic.validate()
    except UnknownRelicType as e:
        result = False
        err = e
    except InvalidRelicRank as e:
        result = False
        err = e
    except InvalidRelicLevel as e:
        result = False
        err = e
    except SubstatSameAsMain as e:
        result = False
        err = e
    except DuplicateSubstat as e:
        result = False
        err = e
    except Exception as e:
        result = False
        err = e

    if result:
        _ = os.system("cls")
        print("Relic Information Valid for H:SR!\n")
        CHARACTER_TEAM[SELECTED_CHARACTER].relics[SELECTED_RELIC_SLOT] = new_relic
        return
    else:
        _ = os.system("cls")
        print("Invalid Relic Information. Please try again.")
        print(f"Error Reason: {err}\n")
        return create_max_relic()


def create_penta_bis_relic():
    """
    Creates a penta-bis (+60) relic.

    Returns:
        None
    """
    new_relic = RelicsComponent()

    su_choice = int(
        input(
            "Do you wish to create a Simulated Universe Relic? (1 - Yes | 0 - No) (Type `-1` to return to the Main Menu): "
        )
    )

    if su_choice == -1:
        _ = os.system("cls")
        return

    relic_enum = RelicSet
    if su_choice == 1:
        new_relic.set_su_relic()

    if new_relic.is_su_relic:
        relic_enum = SURRelicSet
        print(f"Simulated Universe Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")
    else:
        print(f"Relic Set List (as of H:SR {LAST_HSR_UPDATE}):")

    relic_set = set_rs(relic_enum)

    if relic_set is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_set(relic_set)

    relic_type = set_relic_type(new_relic.is_su_relic)

    if relic_type is None:
        _ = os.system("cls")
        return

    new_relic.set_relic_type(relic_type)

    new_relic.set_relic_rank(5)

    new_relic.set_relic_level(0)

    if new_relic.relic_type == RelicType.HEAD or new_relic.relic_type == RelicType.HAND:
        if new_relic.relic_type == RelicType.HEAD:
            new_relic.set_main_stat(MainSubstats.HP_FLAT)
        else:
            new_relic.set_main_stat(MainSubstats.ATK_FLAT)
    else:
        _ = os.system("cls")

        main_stat = choose_main_stat(
            relic_type=new_relic.relic_type, su=new_relic.is_su_relic
        )

        if main_stat is None:
            _ = os.system("cls")
            return

        new_relic.set_main_stat(main_stat)

    for i in range(4):
        substat = choose_substat(i + 1)

        if substat is None:
            _ = os.system("cls")
            return

        new_relic.set_substat(substat, i)
        new_relic.set_substat_rank(15, i)

    print("Validating Relic Information...")
    result = True
    err = None
    try:
        new_relic.validate()
    except UnknownRelicType as e:
        result = False
        err = e
    except InvalidRelicRank as e:
        result = False
        err = e
    except InvalidRelicLevel as e:
        result = False
        err = e
    except SubstatSameAsMain as e:
        result = False
        err = e
    except DuplicateSubstat as e:
        result = False
        err = e
    except Exception as e:
        result = False
        err = e

    if result:
        _ = os.system("cls")
        print("Relic Information Valid for H:SR!\n")
        CHARACTER_TEAM[SELECTED_CHARACTER].relics[SELECTED_RELIC_SLOT] = new_relic
        return
    else:
        _ = os.system("cls")
        print("Invalid Relic Information. Please try again.")
        print(f"Error Reason: {err}\n")
        return create_penta_bis_relic()


def output_to_lunar_core():
    """
    Outputs Lunar Core commands to the user based on CLI or March 7th Console use.
    """
    print("Output Options:")
    print("1. Output Current Character to March 7th Console")
    print("2. Output Current Character to Lunar Core CLI")
    print("3. Output Team List to March 7th Console")
    print("4. Output Team List to Lunar Core CLI\n")

    choice = int(input("Choose an option (Type `-1` to return to the Main Menu): "))

    if choice == -1:
        _ = os.system("cls")
        return

    match choice:
        # Output the current character's relics to the March 7th Console
        case 1:
            _ = os.system("cls")
            for relic in CHARACTER_TEAM[SELECTED_CHARACTER].relics:
                print(relic.to_lunar_core_march_command())
            print(
                "\nCopy the following commands from this tool to the March 7th Console to obtain your desired relics."
            )

            _ = input("Press any key to return to the Main Menu...")
            return
        # Output the current character's relics to the Lunar Core CLI
        case 2:
            _ = os.system("cls")
            for relic in CHARACTER_TEAM[SELECTED_CHARACTER].relics:
                print(relic.to_lunar_core_cli_command())
            print(
                "\nCopy the following commands from this tool to the Lunar Core CLI to obtain your desired relics."
            )

            _ = input("Press any key to return to the Main Menu...")
            return
        # Output the team's relics to the March 7th Console
        case 3:
            _ = os.system("cls")
            for character in CHARACTER_TEAM.values():
                print(f"Character: {character.get_character_name()}")
                for relic in character.relics:
                    print(relic.to_lunar_core_march_command())
                print()

            print(
                "\nCopy the following commands from this tool to the March 7th Console to obtain your desired relics."
            )
            _ = input("Press any key to return to the Main Menu...")
            return
        # Output the team's relics to the Lunar Core CLI
        case 4:
            _ = os.system("cls")
            for character in CHARACTER_TEAM.values():
                print(f"Character: {character.get_character_name()}")
                for relic in character.relics:
                    print(relic.to_lunar_core_cli_command())
                print()

            print(
                "\nCopy the following commands from this tool to the Lunar Core CLI to obtain your desired relics."
            )
            _ = input("Press any key to return to the Main Menu...")
            _ = os.system("cls")
            return
        case _:
            _ = os.system("cls")
            print("Invalid choice. Please try again.\n")
            return output_to_lunar_core()


def print_header():
    """
    Prints the header information for the app.
    """
    print(f'Untitled Lunar Application for a "Certain" Anime Game - Version {VERSION}')
    print(
        f"Copyright (c) {datetime.now().year} Bronya-Rand (https://github.com/Bronya-Rand/Untitled-Lunar-Application). All Rights Reserved."
    )
    print(f"Last Updated: {LAST_UPDATE}\n")


def print_team():
    """
    Prints the characters in the CHARACTER_TEAM dictionary.
    """
    for id, character in CHARACTER_TEAM.items():
        print(f"{id} - {character}")
    print()


def main_menu():
    """
    Displays the main menu options and handles user input.
    """
    print("Current Team:")
    print_team()

    print(f"Selected Character: {CHARACTER_TEAM[SELECTED_CHARACTER]}")
    print(f"Selected Relic Slot: {SELECTED_RELIC_SLOT+1}\n")

    print("Options:")
    print("1. Change Team")
    print("2. Change Current Character")
    print("3. Change Current Relic Slot")
    print("4. Display Current Character's Relics")
    print("5. Create a New Relic")
    print("6. Output to Lunar Core")
    print("7. Exit\n")

    choice = int(input("Choose an option: "))

    match choice:
        case 1:
            change_team()
        case 2:
            change_current_character()
        case 3:
            change_relic_slot()
        case 4:
            display_relics()
        case 5:
            create_new_relic()
        case 6:
            output_to_lunar_core()
        case 7:
            exit()
        case _:
            _ = os.system("cls")
            print("Invalid choice. Please try again.\n")
    main_menu()


def exit():
    print("Exiting...")
    os._exit(0)


def main_cli():
    print_header()
    main_menu()


if __name__ == "__main__":
    main_cli()
