import math

def minEatingSpeed(piles, h):
    L, R = 1, max(piles)
    ans = R
    
    while L <= R:
        k = L + (R - L) // 2
        
        # Check karo is speed k se kitne hours lagenge
        hours_needed = sum(math.ceil(p / k) for p in piles)
        
        if hours_needed <= h:
            ans = k       # Speed valid hai, record kar lo!
            R = k - 1     # Kya isse bhi kam speed mein ho sakta hai? Check Left!
        else:
            L = k + 1     # Speed bohot kam hai, time zyada lag raha hai. Increase Speed!
            
    return ans
