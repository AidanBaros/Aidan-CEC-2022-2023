#include<iostream>
using namespace std;

string reverse(string input) {
	string new_string = "";
	for (int i = input.length() - 1; i >= 0; i--)
		new_string = new_string + input[i];
	return new_string;
}

int main() {
	string input;
	cout << "Type a word to be checked. -- " << endl;
	cin >> input;
	string new_string = reverse(input);
	if (input == new_string)
		cout << "Your words is a palindrome!" << endl;
	else
		cout << "Your words is not a palindrome. :(" << endl;
}
