#include <iostream>
#include <cmath>
#include <locale.h>
using namespace std; 
int main() {
    setlocale(LC_ALL, "rus");   //установка русской локали
    double base, exponent1, exponent2;

    //Ввод основания
    cout << "Введите основание: ";
    cin >> base;

    //Ввод первого показателя степени
    cout << "Введите первый показатель степени: ";
    cin >> exponent1;

    //Вычисление степени первого показателя
    double result = pow(base, exponent1);

    //Ввод второго показателя степени
    cout << "Введите второй показатель степени: ";
    cin >> exponent2;

    //Вычисление степени второго показателя от результата первого вычисления
    result = pow(result, exponent2);

    //Вычисление последней цифры результата
    int lastDigit = static_cast<int>(result) % 10;

    //Вывод результата
    cout << "Последняя цифра трехэтажного числа: " << lastDigit << endl;

    return 0;
}

