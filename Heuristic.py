from CheckConsistent import inRow, inCol, inBox

def isConsistent(var, value, assignments):
  i, j = var
  x, y = i % 3, j % 3
  b = getBox(i, j)
  if inRow(var, value, assignments) or inBox((b, x, y), value, assignments) or inCol(var, value, assignments):
    return False
  return True
# end isConsistent

def getBox(i, j):
  if i < 3:
    box = 1
  elif i < 6:
    box = 4
  else:
    box = 7
  
  if j < 3:
    pass
  elif j < 6:
    box += 1
  else:
    box += 2
  return box
# end getBox
  
def mostConstrained(values, i, j):
  domain = [x for x in range(1, 10)]
  x, y = i % 3, j % 3
  b = getBox(i, j)
  # check rows
  for k in range(9):
    if k != i and values[0][k][j] != 0:
      try:
          domain.remove(values[0][k][j])
      except:
          pass
  if k != j and values[0][i][k] != 0:
      try:
          domain.remove(values[0][i][k])
      except:
          pass
  # check box
  for n in range(3):
    for m in range(3):
      if (n, m) != (x, y) and values[b][n][m] != 0:
        try:
          domain.remove(values[b][n][m])
        except:
          pass
  return len(domain)
# end mostConstrained

def mostConstraining(values, i, j):
  res = 0
  x, y = i % 3, j % 3
  b = getBox(i, j)
  for k in range(9):
      if k != i and values[0][k][j] == 0:
        res += 1
      if k != j and values[0][i][k] == 0:
        res += 1
  for n in range(3):
    for m in range(3):
      if (n, m) != (x, y) and values[b][n][m] == 0:
        res += 1
  return res

def getBestHeuristic(big_squares):
  # most constrained
  best = {
    'locations': [],
    'amtConstrained': 10
  }
  for i in range(9):
    for j in range(9):
      if big_squares[0][i][j] == 0:
        amtConstrained = mostConstrained(big_squares, i, j)
        if amtConstrained == best['amtConstrained']:
          best['locations'].append((i, j))
        elif amtConstrained < best['amtConstrained']:
           best['locations'] = [(i, j)]
           best['amtConstrained'] = amtConstrained

  if len(best['locations']) == 1:
    return best['locations'][0]

  ties = best['locations']
  mostConstaining = (None, -1)
  for location in ties:
    (i, j) = location
    currConstaints = mostConstraining(big_squares, i, j)
    if currConstaints > mostConstaining[1]:
      mostConstaining = (location, currConstaints)

  return mostConstaining[0]
# end getBestHeuristic