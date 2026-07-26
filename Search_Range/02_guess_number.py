def guessNumber(n):
    L, R = 1, n
    while L <= R:
        M = L + (R - L) // 2
        res = guess(M)
        
        if res == 0:
            return M  # Mil gaya secret number!
        elif res == -1:
            R = M - 1  # Guess bada tha, toh chhota guess karo
        else:
            L = M + 1  # Guess chhota tha, toh bada guess karo
