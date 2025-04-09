#Given a 2x2 grid there is 6 routes to get from top-left corner to bottom-right
#What is the number of routes in a 20x20 grid
"""___ ___
  |___|___|
  |___|___|
in this 2x2 grid there is 6 routes if only allowed to move right or down
  """
#This is a very easy problem which takes no coding if you don't want
#The answer is simply (2n)C(n) in this case n = 20
import math

def number_of_routes(n):
    result = math.comb(2*n, n)
    return result
print(number_of_routes(20))