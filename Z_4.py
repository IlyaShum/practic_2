#Импорт модуля random для генерации случайных чисел
import random

#Функция для проверки числа на простоту с помощью теста теоремы Ферма
def is_prime_fermat(n, k=5):
    #Если число равно 2 или 3, то оно является простым
    if n == 2 or n == 3:
        return True
    #Если число меньше или равно 1 или четное, то оно не является простым
    if n <= 1 or n % 2 == 0:
        return False

    #Проверка числа на простоту с помощью теста теоремы Ферма
    for _ in range(k):
        #Выбор случайного числа 'a' в диапазоне от 2 до n - 2
        a = random.randint(2, n - 2)
        #Проверка условия теста теоремы Ферма: a^(n-1) ≡ 1 (mod n)
        if pow(a, n - 1, n) != 1:
            return False
    #Если тест пройден для всех 'k' случайных 'a', то число простое
    return True

#Функция для генерации больших простых чисел
def generate_large_prime(key_size):
    #Генерация случайного числа в заданном диапазоне и проверка его на простоту
    while True:
        num = random.randrange(2**(key_size - 1), 2**key_size)
        if is_prime_fermat(num):
            return num

#Функция для вычисления наибольшего общего делителя (НОД)
def gcd(a, b):
    #Алгоритм Евклида для вычисления НОД
    while b != 0:
        a, b = b, a % b
    return a

#Функция для вычисления обратного элемента по модулю
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    #Расширенный алгоритм Евклида для вычисления обратного элемента
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    #Если НОД равен 1, то возвращаем обратный элемент
    if temp_phi == 1:
        return d + phi

#Функция для генерации ключей
def generate_keys(key_size):
    #Генерация двух простых чисел и вычисление модуля и функции Эйлера
    p = generate_large_prime(key_size)
    q = generate_large_prime(key_size)

    n = p * q
    phi = (p - 1) * (q - 1)

    #Генерация открытой экспоненты и проверка её на взаимную простоту с функцией Эйлера
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Вычисление закрытой экспоненты
    d = multiplicative_inverse(e, phi)

    #Возврат открытого и закрытого ключей
    return (e, n), (d, n)

#Функция для шифрования текста
def encrypt(public_key, plaintext):
    #Разложение открытого ключа на экспоненту и модуль
    key, n = public_key
    #Шифрование каждого символа исходного текста
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

#Функция для дешифрования текста
def decrypt(private_key, ciphertext):
    #Разложение закрытого ключа на экспоненту и модуль
    key, n = private_key
    #Дешифрование каждого символа зашифрованного текста
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    #Объединение символов в строку
    return ''.join(plain)

#Функция для демонстрации работы алгоритма
def main():
    #Генерация ключей
    public_key, private_key = generate_keys(16)

    #Ввод исходного текста с клавиатуры
    message = input("Введите исходный текст: ")
    #Шифрование текста
    encrypted_message = encrypt(public_key, message)
    #Дешифрование текста
    decrypted_message = decrypt(private_key, encrypted_message)

    #Вывод исходного, зашифрованного и дешифрованного текстов
    print(f'Исходный текст: {message}')
    print(f'Зашифрованный текст: {encrypted_message}')
    print(f'Дешифрованный текст: {decrypted_message}')

if __name__ == "__main__":
    main()

