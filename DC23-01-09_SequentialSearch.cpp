#include<iostream>
#include<list>
using namespace std;

int main() {
	int location;
	int found;
	location = 0;
	found = 0;
	int IDs[] = { 234,567,321,234,789 };

	int searchItem;
	cout << "enter the ID you are looking for:" << endl;
	cin >> searchItem;

	char reversechoice;
	cout << "would you like to reverse the order of the list? Y/N" << endl;
	cin >> reversechoice;

	if (reversechoice == 'Y' or reversechoice == 'y') {
		location = size(IDs) - 1;
		while (location >= 0) {
			if (IDs[location] == searchItem) {
				found++;
			}
			location--;
		}
	}
	else {
		while (location < size(IDs)) {
			if (IDs[location] == searchItem) {
				found++;
			}
			location++;
		}
	}

	if (found > 0) {
		cout << "ID " << searchItem << " was found " << found << " times." << endl;
	}
	else
		cout << "ID was not found" << endl;
}

