#include<iostream>
#include<ctime>
#include<string>
#include<chrono>
using namespace std;

int main() {
	string input;
	string guess;
	

	cout << "Input a password to test -- ";
	cin >> input;

	for (int i = 0; i < input.size(); i++) {
		guess += (char)32;
	}

	auto start = chrono::high_resolution_clock::now();
	while (true) {
		if (guess == input) {
			auto stop = chrono::high_resolution_clock::now();
			auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);
			float totalTime = duration.count() / double(1000);
			if (totalTime >= 60) {
				int tt = totalTime;
				int min = tt / 60;
				int sec = tt % 60;
				cout << "It took " << min << " minutes and " << sec << " seconds to find your password, -- " << guess << endl;
			}
			else {
				cout << "It took " << totalTime << " seconds to find your password, -- " << guess << endl;
			}
			break;
		}
		guess[0] = (char) int(guess[0]) + 1;
		for (int i = 0; i < input.size(); i++) {
			if (guess[i] % 127 == 0) {
				guess[i] = (char)32;
				guess[i+1] = (char) int(guess[i+1]) + 1;
			}
		}
	}
}
