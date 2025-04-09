# Cuboid Route

import math

def solve_problem_86(target=1_000_000):
    """
    Returns the smallest integer M such that the number of integer-dimension
    cuboids (a <= b <= c <= M) having an integer shortest path from one corner
    to the opposite corner exceeds 'target'.
    """
    
    def is_square(n):
        r = int(math.isqrt(n))
        return (r * r == n)
    
    total_solutions = 0
    M = 0
    
    while True:
        M += 1
        new_solutions = 0
        
        # For fixed c = M, let x = a + b, where 2 <= x <= 2M
        for x in range(2, 2*M + 1):
            dist_sq = x*x + M*M
            if is_square(dist_sq):
                # Count valid pairs (a, b) with:
                #   1 <= a <= b <= M
                #   a + b = x
                #   a <= b => a <= x/2
                #   b <= M => x - a <= M => a >= x - M
                a_min = max(1, x - M)
                a_max = x // 2
                if a_max >= a_min:
                    new_solutions += (a_max - a_min + 1)
        
        total_solutions += new_solutions
        
        if total_solutions > target:
            return M

def main():
    result = solve_problem_86(1_000_000)
    print("Smallest M with more than 1,000,000 solutions:", result)

if __name__ == "__main__":
    main()
