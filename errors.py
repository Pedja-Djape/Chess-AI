class PositionNotInRangeError(Exception):

    def __init__(self,position,message = "Desired position is not in [0,63] range:"):
        self.pos = position
        self.message = f"{message} {position}"
        super().__init__(self.message)
        pass
class NotOnTeamError(Exception):

    def __init__(self,board,position,message = "The piece at this position does not belong to current players team:"):
        self.piece = board[position]
        self.message = f"{message}  {(self.piece)}"
        super().__init__(self.message)

class InvalidMoveError(Exception):
    def __init__(self,dst,message = "The destination of your piece is not considered a legal move:"):
        self.dst = dst 
        self.message = f"{message} {self.dst}"
        super().__init__(self.message)

class InertPieceError(Exception):
    def __init__(self,position,message = "The piece you've selected currently has no legal moves."):
        self.pos = position
        self.message = f"{message}: {self.pos}"