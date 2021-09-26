def int_sqrt(n):
#fast integer sqrt
    if n > 10000000000:  
        binary = bin(n)[2:]
        x = 2 ** (len(binary)// 2+2) #good inital canddiate for large n.. need y to be large than sqrt(n)... rest of it is std. newton's approx iterations.
    else:
        x = n // 2
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
