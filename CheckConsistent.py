def inBox(location, value, big_squares):
  currBigBox = big_squares[location[0]]
  for i in range(3):
    for j in range(3):
      if currBigBox[i][j] == value:
        return True
  return False
# end inBox

def inRow(location, value, big_squares):
  i = location[0]

  for k in range(9):
    if big_squares[0][i][k] == value:
      return True

  return False
# end inRow

def inCol(location, value, big_squares):
  j = location[1]

  for k in range(9):
    if big_squares[0][k][j] == value:
      return True

  return False
# end inCol