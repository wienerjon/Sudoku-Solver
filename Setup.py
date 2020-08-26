def readInput(filename):
  f = open(filename, 'r')
  big_squares = {}
  for x in range(10):
    big_squares[x] = []

  for x in range(9):
    line = f.readline()
    lineArray = line.split()
    lineArray = [int(y) for y in lineArray]
    big_squares[0].append(lineArray)

    if x < 3:
      key = 1
    elif x < 6:
      key = 4
    else:
      key = 7

    big_squares[key].append(lineArray[:3])
    big_squares[key+1].append(lineArray[3:6])
    big_squares[key+2].append(lineArray[6:])

  return big_squares
# end readInput

def createDomains(big_squares):
  domains = {}
  for big in range(1, 10):
    for i in range(3):
      for j in range(3):
        box = (big, i, j)
        if big_squares[big][i][j] != 0:
          domains[box] = [big_squares[big][i][j]]
        else: # domain is numbers 1-9
          domains[box] = [x for x in range(1, 10)]
  return domains
# end createDomains