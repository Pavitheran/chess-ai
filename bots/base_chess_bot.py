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

	"""
	Given a standard chess game representation,
	method should return True if the bot wants to accept a surrender
	and false otherwise.
	"""
	def accept_surrender(self, board):
		return False
