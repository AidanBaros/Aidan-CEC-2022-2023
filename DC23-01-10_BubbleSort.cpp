#include <iostream>
#include <ctime>
#include <time.h> 

using namespace std;

int main() {
    const int listsize = 10;
    int myList[listsize] = { 0,0,0,0,0,0,0,0,0,0 };
    
    srand(time(NULL));

    for (int i = 0; i < listsize; i++) {
        myList[i] = (rand() % 101);
        cout << myList[i] << endl;
    }
    int temp = 0;
    for (int i = 0; i < listsize; i++) {
        for (int j = 0; j < listsize-1; j++) {
            if (myList[j]>myList[j+1]) {
                temp = myList[j];
                myList[j] = myList[j + 1];
                myList[j + 1] = temp;
            }
        }
    }
    for (int i = 0; i < listsize; i++) {
        cout << myList[i] << endl;
    }

    return 0;
}
