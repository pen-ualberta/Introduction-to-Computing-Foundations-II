x = "hello"

if not type(x) is int:

  raise TypeError("Only integers are allowed")

#Tile Class Test
#initialize tile test
tile1= Tile(2)
tile2 = Tile(2)
tile3 = Tile(2)

#retreiving value of tile
print(tile1.getValue())

#double the value of tile
tile1.doubleValue()
print(tile1 .getValue())

#equating two tiles by their values
print(tile1.__eq__(tile2))
print(tile2.__eq__(tile3))

#turning the tile to a string
print(tile1.__str__())


board = Columns1000(7,4)
board.drawColumns()
print(board.columnFull(2))
tile = Tile(4)
board.placeTile(6,tile)
board.drawColumns()