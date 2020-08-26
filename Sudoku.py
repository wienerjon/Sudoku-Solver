from Backtracking import backtracking
from Setup import readInput, createDomains
from ForwardCheck import forwardChecking

def main(inputFile, outputFile):
  assignments = readInput(inputFile)
  domains = createDomains(assignments)
  try:
    domains, repeat = forwardChecking(assignments, domains) # run forward checking
  except:
    print("There is no solution")
    exit() 
  while (repeat): # repeat forwardChecking if necessary
    try:
      domains, repeat = forwardChecking(assignments, domains)
    except:
      print("There is no solution")
      exit()

  solution = backtracking(assignments, domains)
  if solution == False:
    print('no solution')
    exit()
  
  solution = solution[0]
  for line in solution:
    print(' '.join([str(x) for x in line]))

  out = open(outputFile, 'w')
  for line in solution:
    line = ' '.join([str(x) for x in line])
    out.write(line+'\n')
  out.close()
  
main('input1.txt', 'output1.txt')