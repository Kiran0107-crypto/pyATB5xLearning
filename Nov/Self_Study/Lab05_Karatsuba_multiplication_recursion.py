def karatsuba(x, y):
    # Base case: if x or y is a single-digit number, return their product
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits in the larger number
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y into two halves
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    # Recursive calls to compute P1, P2, and P3
    p1 = karatsuba(a, c)          # A * C
    p2 = karatsuba(b, d)          # B * D
    p3 = karatsuba(a + b, c + d)  # (A + B) * (C + D)

    # Use Karatsuba's formula to combine the results
    result = (10**(2*m)) * p1 + (10**m) * (p3 - p1 - p2) + p2

    return result

# Example usage
x = 12345678
y = 87654321
result = karatsuba(x, y)
print(f"{x} * {y} = {result}")
