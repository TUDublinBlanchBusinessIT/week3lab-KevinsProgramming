#kevin tshiaka
#07/02/2024
#perfect number

from divisors import divisors

def perfectNumber(x):
    results = False

    if sum(divisors(x)) == x:
        result = True

    return result
