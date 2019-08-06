class BaseChessBot(object):
	"""
	Return the name of your chess bot
	"""
	def get_name(self):
		raise NotImplementedError("All chess bots must implement the name method")

	"""
	Method takes a standard chess game representation and
	returns another game representation with the next move appended.
	"""
	def play_move(self, board):
		raise NotImplementedError("All chess bots must implement the play_move method")

	"""
	Given a standard chess game representation, 
	method should return True if the bot wants to accept a surrender
	and false otherwise.
	"""
	def accept_surrender(self, board):
		return False