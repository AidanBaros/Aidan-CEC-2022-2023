#include<iostream>
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

	int newList[size(IDs)];

	if (toupper(reversechoice) == 'Y') {
		for (int i = 0; i < size(IDs); i++) {
			newList.push_front(IDs[i]);
		}
	}

	//cout << size(IDs) << endl;
	while (location < size(IDs)) {
		if (IDs[location] == searchItem) {
			found++;
		}
		location++;
	}

	if (found > 0) {
		cout << "ID " << searchItem << " was found " << found << " times." << endl;
	}
	else
		cout << "ID was not found" << endl;
}
