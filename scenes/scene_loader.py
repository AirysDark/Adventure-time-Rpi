from scenes.title_screen import TitleScreen
from scenes.treehouse import Treehouse
from scenes.candy_kingdom import CandyKingdom

def load_scene(name):
    if name == "title":
        return TitleScreen()
    elif name == "treehouse":
        return Treehouse()
    elif name == "candy_kingdom":
        return CandyKingdom()
