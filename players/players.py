"Player logic."

def set_player_name() -> str:
    """
    Setting a new player name
    Return:
        str - The user name (non empty str)
    """

    while True:
        name = input("Enter your name: ").upper()

        if name != "":
            return name
        print("\nName may not be blank.")


def validate_name(name: str, names: list | tuple) -> bool:
    """
    Checks whether the chosen name has already been taken
    Args:
        name (str): the name to check
        names (list): the names we already have
    Returns:
        boolean
    """
    return name in names


def add_player(players: list) -> str:
    """
    Returns the name of player we want to add to our game

    Args:
        players (list): All available players in the game

    Returns:
        str : the player's name
    """
    while True:
        name = set_player_name()
        if not validate_name(name,players):
            return name
        print("\nName has already been taken, please choose another.")



if __name__ == "__main__":
    print(add_player(["P"]))