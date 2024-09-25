#include <iostream> //подключение библиотеки для ввода-вывода
#include <string>   //подключение библиотеки для работы со строками
#include <cmath>    //подключение библиотеки для математических функций
#include <ctime>    //подключение библиотеки для работы со временем
#include <locale.h> //подключение библиотеки для работы с локалью

//Функция для вычисления НОД
__int64 gcd(__int64 a, __int64 b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

//Функция для вычисления обратного числа
__int64 modInverse(__int64 a, __int64 m) {
    a = a % m;
    for (__int64 x = 1; x < m; x++)
        if ((a * x) % m == 1)
            return x;
    return -1;
}

//Функция для шифрования
__int64 encrypt(__int64 i, __int64 e, __int64 n) {
    __int64 current = i;
    __int64 result = 1;
    for (__int64 j = 0; j < e; j++) {
        result = (result * current) % n;
    }
    return result;
}

//Функция для дешифрования
__int64 decrypt(__int64 i, __int64 d, __int64 n) {
    __int64 current = i;
    __int64 result = 1;
    for (__int64 j = 0; j < d; j++) {
        result = (result * current) % n;
    }
    return result;
}

//Функция для проверки числа на простоту
bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    if (num == 2) {
        return true;
    }
    if (num % 2 == 0) {
        return false;
    }
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    setlocale(LC_ALL, "rus");   //установка русской локали

    srand(static_cast<unsigned int>(time(nullptr)));    //инициализация генератора случайных чисел

    __int64 p = 47;   //простое число p
    __int64 q = 71;   //простое число q

    //Проверка чисел на простоту
    if (!isPrime(p) || !isPrime(q)) {
        std::cout << "Оба числа должны быть простыми." << std::endl;
        return 1;
    }

    __int64 n = p * q;    //вычисление модуля n
    __int64 phi = (p - 1) * (q - 1);  //вычисление функции Эйлера phi

    __int64 e = 79;   //открытая экспонента e

    __int64 d = modInverse(e, phi);   //вычисление закрытой экспоненты d

    std::string message;    //объявление переменной для хранения исходного текста
    std::cout << "Введите исходный текст: ";
    std::getline(std::cin, message);    //ввод исходного текста с клавиатуры

    std::string encrypted_message = ""; //переменная для хранения зашифрованного сообщения

    //Шифрование
    for (char c : message) {
        __int64 encrypted_char = encrypt(c, e, n);
        encrypted_message += std::to_string(encrypted_char) + " ";
    }

    std::string decrypted_message = ""; //переменная для хранения расшифрованного сообщения
    std::string temp = "";  //временная переменная для хранения символов при дешифровании

    //Дешифрование
    for (char c : encrypted_message) {
        if (c == ' ') {
            __int64 decrypted_char = decrypt(std::stoll(temp), d, n);
            decrypted_message += static_cast<char>(decrypted_char);
            temp = "";
        }
        else {
            temp += c;
        }
    }

    std::cout << "Зашифрованный текст: " << encrypted_message << std::endl; //вывод зашифрованного сообщения
    std::cout << "Дешифрованный текст: " << decrypted_message << std::endl; //вывод расшифрованного сообщения

    return 0;
}

