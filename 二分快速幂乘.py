def power(a, n):
    result = 1
    while n:
        if n & 1:
            result *= n
        n *= n
        n >>= 1;
    return result

            
