class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __str__(self):
        return f"{self.color} {self.__class__.__name__} at {self.position}"

    def change_color(self):
        self.color = 'black' if self.color == 'white' else 'white'

    def change_position(self, new_position):
        x, y = new_position
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.position = new_position
        else:
            print("Invalid position! The piece cannot be placed outside the board.")

    def is_valid_move(self, new_position):
        raise NotImplementedError("Subclasses must implement the is_valid_move method.")


class Pawn(ChessPiece):
    def is_valid_move(self, new_position):
        x, y = new_position
        if self.color == 'white':
            return x == self.position[0] + 1 and y == self.position[1]
        else:
            return x == self.position[0] - 1 and y == self.position[1]


class Knight(ChessPiece):
    def is_valid_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Bishop(ChessPiece):
    def is_valid_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return dx == dy


class Rook(ChessPiece):
    def is_valid_move(self, new_position):
        x, y = new_position
        return x == self.position[0] or y == self.position[1]


class Queen(ChessPiece):
    def is_valid_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (x == self.position[0] or y == self.position[1]) or (dx == dy)


class King(ChessPiece):
    def is_valid_move(self, new_position):
        x, y = new_position
        dx = abs(x - self.position[0])
        dy = abs(y - self.position[1])
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1)


def get_valid_moves(pieces, new_position):
    valid_pieces = []
    for piece in pieces:
        if piece.is_valid_move(new_position):
            valid_pieces.append(piece)
    return valid_pieces
