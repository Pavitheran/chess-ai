from abc import ABC, abstractmethod
class BaseChessBot(ABC):
	"""
	Return the name of your chess bot
	"""
	@abstractmethod
	def get_name(self):
		pass

	"""
	Method takes a standard chess game representation and
	returns another game representation with the next move appended.
	"""
	@abstractmethod
	def play_move(self, board):
		pass
