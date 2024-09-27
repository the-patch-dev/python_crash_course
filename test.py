# Part 1: Identify if 21488566 is prime
number = 21488566
if sympy.isprime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Part 2: Create a Cayley table for addition modulo 6 and output only primes

def is_prime(n):
    """ Check if a number is prime. """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cayley_table_modulo(n):
    """ Generate a Cayley table for addition modulo n and filter primes. """
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            result = (i + j) % n
            row.append(result)
        table.append(row)
    
    return table

def print_prime_cayley_table(table):
    """ Print only the prime numbers from the Cayley table. """
    primes = []
    for row in table:
        prime_row = [x for x in row if is_prime(x)]
        primes.append(prime_row)
    
    print("Prime Numbers in the Cayley Table:")
    for row in primes:
        print(row)

# Create the Cayley table for addition modulo 6
cayley_table = cayley_table_modulo(6)

# Output only the prime numb
