#include<iostream>
#include<math.h>
using namespace std;

int main() {
	int one = 0x010;
	int* three;
	three = &one;
	*(three + 20) = int(3);

	cout << *three << endl;
	three += 20;
	cout << *three << endl;

	//-----------------------------------------------------------------------------------------------------------------------

	long double two = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679;
	auto four = two == (atan(1) * 4);
	bool* eight = &four;
	cout << *eight << endl;
}
