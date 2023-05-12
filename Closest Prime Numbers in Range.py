class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        isprime = [True for _ in range(right + 1)]
        isprime[0] = isprime[1] = False
        i = 2
        
        while i * i < right + 1:
            if isprime[i]:
                j = i * i
                while j < right + 1:
                    isprime[j] = False
                    j += i
            i += 1
        
        primes = []
        div = right
        l, r = -1, -1
        
        for i in range(left, right + 1):
            if isprime[i]:
                primes.append(i)
        if len(primes) < 2:
            return [-1,-1]
        i = 0
        while i < len(primes) - 1:
            if primes[i + 1] - primes[i] < div:
                div = primes[i + 1] - primes[i]
                l = primes[i]
                r = primes[i + 1]
            i += 1
        return [l, r]
