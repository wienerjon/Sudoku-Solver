from Heuristic import getBestHeuristic, isConsistent, getBox

def isCompleted(big_squares):
  for i in range(9):
    for j in range(9):
      if big_squares[0][i][j] == 0:
        return False
  return True
# end isCompleted

def backtracking(assignments, domains):
  if isCompleted(assignments):
    return assignments
  var = getBestHeuristic(assignments)
  i, j = var
  x, y = i % 3, j % 3
  b = getBox(i, j)
  originalDomain = domains[(b, x, y)]

  for value in domains[(b, x, y)]:
    if isConsistent(var, value, assignments):
      assignments[0][i][j] = value
      assignments[b][x][y] = value
      domains[(b, x, y)] = [value]
      result = backtracking(assignments, domains)
      if result != False:
        return result

  assignments[0][i][j] = 0
  assignments[b][x][y] = 0
  domains[(b, x, y)] = originalDomain
  return False
# end backtracking