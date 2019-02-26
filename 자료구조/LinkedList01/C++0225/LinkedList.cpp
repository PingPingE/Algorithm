#include <iostream>
using namespace std;
typedef struct node
{
	int data;
	node* next;
}Node;
Node* head = NULL; //첫번째 노드를 가리킬 포인터
void main()
{
	Node* a = (Node *)malloc(sizeof Node);
	a->data = 3;
	a->next = NULL;
	head = a;

	Node* b = new Node;
	b->data = 5;
	b->next = NULL;
	a->next = b;
	
	Node* p = head;
	while (p != NULL)
	{
		cout << p->data << endl;
		p = p->next;
	}
	free(a);
	delete b;

}