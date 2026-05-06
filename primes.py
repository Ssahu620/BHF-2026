def get_first_n_primes(n=10):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % p != 0 for p in primes):
            primes.append(candidate)
        candidate += 1
    return primes

def print_primes(n=10):
    print(*get_first_n_primes(n))

print_primes()
