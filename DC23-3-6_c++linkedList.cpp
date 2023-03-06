//train simulator- shows basics of linked lists in C++
#include <iostream>
using namespace std;

enum CarType { engine, tanker, box, passenger, caboose };

class Node {
public:
	int carNumber;
	int carType;
	bool isFull;
	Node* next;
};


//this function inserts a new node in FRONT of the list---------------------------------------------------
void addFront(Node** head, int num, int type, bool isFull) {
	//make a new car
	Node* newNode = new Node;

	//give it its data
	newNode->carNumber = num;
	newNode->carType = type;
	newNode->isFull = isFull;

	//set next of new node as head
	newNode->next = (*head);

	//move the head to point to the new node 
	(*head) = newNode;
}

//this function adds a new node AFTER a given node------------------------------------------------------
void addAfter(Node* prev_node, int num, int type, bool isFull) {

	//check if previous node is NULL, give error message if it is
	if (prev_node != NULL) {
		Node* newNode = new Node;

		//give it its data
		newNode->carNumber = num;
		newNode->carType = type;
		newNode->isFull = isFull;

		//set next of new node as head
		newNode->next = (prev_node);

		//move the head to point to the new node 
		(prev_node) = newNode;
	}

}

//this function prints out the whole list----------------------------------------------------------------
void displayList(Node* node) {

	cout << "Printing Train! Choo Choo!" << endl << endl;
	//traverse the list to display each node
	while (node != NULL) {
		cout << "[ ";
		if (node->carType == 0)
			cout << "engine";
		else if (node->carType == 1)
			cout << "tanker";
		else if (node->carType == 2)
			cout << "boxcar";
		else if (node->carType == 3)
			cout << "passenger";
		else
			cout << "caboose!";

		cout << " # ";
		cout << node->carNumber;
		if (node->isFull == true)
			cout << " is: Full" << " ] --> ";
		else
			cout << " is: Not Full" << " ] --> ";
		node = node->next;
	}

	if (node == NULL)
		cout << "end" << endl << endl; //end of train
}


int main() {
	Node* head = NULL;
	addFront(&head, 100, box,true);
	addFront(&head, 200, box,false);
	addFront(&head, 300, box,false);
	addFront(&head, 400, box,true);
	addFront(&head, 2394, engine,false);
	addAfter(head, 1234, tanker, true);
	displayList(head);
}
