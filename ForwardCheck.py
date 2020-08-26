def forwardChecking(big_squares, domains):
  repeat = False

  for b in range(1, 10):
    for i in range(3):
      for j in range(3):
        if len(domains[(b, i, j)]) == 1:
          currVal = big_squares[b][i][j]
          #check in box
          for k in range(3):
            if k != i:
              try:
                domains[(b, k, j)].remove(currVal)
                if len(domains[(b, k, j)]) == 0:
                  return 'Invalid'
                if len(domains[(b, k, j)]) == 1:
                  repeat = True
              except:
                pass

            if k != j:
              try:
                domains[(b, i, k)].remove(currVal)
                if len(domains[(b, i, k)]) == 0:
                  return 'Invalid'
                if len(domains[(b, i, k)]) == 1:
                  repeat = True
              except:
                pass

  return domains, repeat
# end forwardChecking