"""Interface for chess bots."""

from abc import ABC, abstractmethod


# pylint: disable=R0201
class BaseChessBot(ABC):
    """Interface for all chess bots."""

    @abstractmethod
    def get_name(self):
        """Return name of bot."""

    @abstractmethod
    def play_move(self, board):
        """Push move onto board."""

    def accept_surrender(self):
        """Return bool to accecpt/reject surrender."""
        return False
