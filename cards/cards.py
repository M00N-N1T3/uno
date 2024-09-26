"Contains all the logic needed to generate a card"

__author__ = "Johnny"
__all__ = ["generate_cards", "generate_card_set","get_deck"]

def generate_cards(color:str, data:list | tuple):
    """
    Creates a group of cards for the given cards
    Args:
        color (str): the color the cards must be
        data (list): an iterable containing the data set
    Returns:
        list : contains a list of values that make up a
        concatenated string of color + element
    """
    tmp = []

    for da in data:
        tmp.append(color+da)
    return tmp


def get_numbers():
    """
    Generates a list of numbers from range 0, 10

    """
    return [str(x) for x in range(0,10)]


def generate_card_set(color: str):
    """
    A set of cards. The set includes the numbered cards, wild cards and special cards
    Args:
        color (str): the color we want the cards to be
    Return:
        list : the set of cards
    """

    card_set = []
    color = color + "_"
    sp_cards = ("skip","reverse","draw_two")
    wild_cards = ("wild","wild_four")
    numbers = get_numbers()

    numbered_cards = generate_cards(color,numbers)
    specials = generate_cards(color,sp_cards)

    card_set.extend(numbered_cards)
    card_set.extend(wild_cards)
    card_set.extend(specials)

    return card_set

def get_deck():
    """
    Creates the deck of cards that we need for the game
    """
    deck = []

    for color in ["blue","red","green","yellow"]:
        deck.extend(generate_card_set(color))
    return deck