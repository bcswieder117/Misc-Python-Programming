# Blaine Swieder
# LeetCode (Python): Count the Number of Arrays with "K" Matching Adjacent Elements
# June 17th, 2025

MOD = 10**9 + 7

def mod_pow(a, e):
    res = 1
    while e:
        if e % 2: res = res * a % MOD
        a = a * a % MOD
        e //= 2 
    return res

MAX_N = 100000
fact = [1] * (MAX_N + 1)
inv_fact = [1] * (MAX_N + 1)

for i in range(1, MAX_N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[MAX_N] = mod_pow(fact[MAX_N], MOD - 2)

for i in range(MAX_N, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

def nCr(n, r):
    if r < 0 or r > n: 
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

class Solution(object): 
    def countGoodArrays(self, n, m, k):
        if k > n - 1: 
            return 0
        if m == 1: 
            return 1 if k == n - 1 else 0
        
        runs = n - k
        ways_to_split = nCr(n - 1, runs - 1)
        ways_to_color = m * mod_pow(m - 1, runs - 1) % MOD

        return ways_to_split * ways_to_color % MOD

###### Example Usage ##############################
    
    
sol = Solution()
print(sol.countGoodArrays(4, 3, 1)) # Desired Output: 36
