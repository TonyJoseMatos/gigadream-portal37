"""
GIGADREAM // PORTAL 37
Terminal ASCII Engine by Tony Jose Matos (@TonyJMatos)
Pure Gigadream transmission. Hints of Beachpunk. No Masters.
"""

__version__ = "0.1.0"
__author__ = "Tony Jose Matos"

from .cli import main
from .art import get_frames, render_frame
from .sound import play_sequence

__all__ = ["main", "get_frames", "render_frame", "play_sequence"]