class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return (n * 2) // math.gcd(2,n)