#include<iostream>
#include<cmath>
#include<iomanip>
#include<string>

using namespace std;

namespace power {
    int pow(int x, int y) {
        int answer = 1;
        for (int i = 0; i < y; i++) {
            answer = answer * x;
        }
        return answer;
    };
};

int main() {
	int x = 3;
	int y = 2;
	int answer = power::pow(x, y);
    cout << x << " to the " << y << " power is " << answer << endl;

}
