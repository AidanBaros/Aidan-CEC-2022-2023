#include<iostream>
using namespace std;

long double blackHole(long double mass);
const long double G = 6.674e-11;
const long double c = 2.998e8;

int main() {
	long double startingMass;
	while (true) {
		cout << "enter mass in kilograms:" << endl;
		cin >> startingMass;
		cout << "Radius is " << blackHole(startingMass) << " meters." << endl << endl;
	}
}

long double blackHole(long double mass) {
	return (2 * G * mass) / (c * c);
}
