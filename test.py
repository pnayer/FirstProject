def is_prime(num):
    """بررسی اینکه آیا یک عدد اول است یا خیر."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    limit = int(input(" 23:"))
    if limit < 0:
        print(" 30")
    else:
        print_primes(limit)
except ValueError:
    print("90")

