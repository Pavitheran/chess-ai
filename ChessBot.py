class ChessBot:
	"""
	Return the name of your chess bot
	"""
	def name():
		raise NotImplementedError("All chess bots must implement this method")

	"""
	Method takes a standard chess game representation and
	returns another game representation with the next move appended.
	"""
	def play_move(game_repr):
		raise NotImplementedError("All chess bots must implement this method")

	"""
	Given a standard chess game representation, 
	method should return True if the bot wants to accept a surrender
	and false otherwise.
	"""
	def accept_surrender(game_repr):
		return False