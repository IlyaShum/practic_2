def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

#объявление функции для возведения числа a в степень n по модулю p
def power(a, n, p):
    res = 1
    a = a % p
    while n > 0:
        if n & 1:
            res = (res * a) % p
        n = n >> 1
        a = (a * a) % p
    return res

#объявление функции для проверки, является ли число простым
def isPrimeNumber(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#объявление функции для проверки теоремы Ферма для чисел a и p
def FermatTheorem(a, p):
    if gcd(a, p) != 1:
        return False
    if power(a, p - 1, p) != 1:
        return False
    return True

def main():
    a = int(input("Введите a: "))
    x = int(input("Введите x: "))
    p = int(input("Введите p: "))

    #проверка на простоту числа p
    if not is_prime(p):
        print("p не является простым числом")
        return
    #проверка выполнения теоремы Ферма для чисел a и p
    if not fermat_test(a, p):
        print("Теорема Ферма не справедлива для a и p")
        return

    result = power(a, x, p)
    print("Результат:", result)

if __name__ == "__main__":

