#include<iostream>
using namespace std;

//practice using the "8" operator
//"&" means "address of" in C++. it returns the address of a given variable

void funOne(int a, int& b, char v);
void funTwo(int& x, int y, char& w);
void funThree(int a, int b, char c);

int main() {
	int num1, num2;
	char ch;

	num1 = 10;
	num2 = 15;
	ch = 'A';

	cout << num1 << " " << num2 << " " << ch << endl;

	funOne(num1, num2, ch);

	cout << num1 << " " << num2 << " " << ch << endl;

	funTwo(num2, 25, ch);

	cout << num1 << " " << num2 << " " << ch << endl;

	funThree(num2, 25, ch);

	cout << num1 << " " << num2 << " " << ch << endl;
}

void funOne(int a, int& b, char v) {
	int one;
	one = a;
	a++;
	b = b * 2;
	v = 'B';
	cout << "Inside funOne: ";
	cout << a << " " << b << " " << v << endl;
}

void funTwo(int& x, int y, char& w) {
	x++;
	y = y * 2;
	w = 'G';
	cout << "Inside funTwo:";
	cout << x << " " << y << " " << w << endl;
}

void funThree(int a, int b, char c) {
	a = a*a;
	b = b + b;
	c = c + c;
	cout << "Inside funThree:";
	cout << a << " " << b << " " << c << endl;
}
