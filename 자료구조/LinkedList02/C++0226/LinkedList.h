#pragma once
#include "Node.h"
#include <iostream>
using namespace std;
class LinkedList
{
private:
	Node* head;
public:
	LinkedList() : head(NULL) {} //초기화
	~LinkedList() {}
	void insert(int val) //새로운 데이터 삽입
	{
		Node* n = new Node; //새로운 노드 생성
		n->data = val; //데이터 삽입
		n->link = head; //앞으로 추가
		head = n;

	}
	void remove(int val)
	{
		Node* finder = head;
		if (finder->data != val)
		{
			Node* next = finder->link;
			while (next->data != val) // 다음 노드에 찾는 데이터가 없으면
			{
				finder = finder->link;//계속 다음으로
				next = finder->link;
			}

			finder->link = next->link; //finder는 대상 노드를 가리킴(즉 대상 노드의 전 노드임)
			//finder는 대상 노드의 다음 노드를 가리키도록 한다.
		}
		else //head가 가리키는 노드가 대상노드라면
		{
			head = finder->link; //head만 바꿔준다.
		}

	}
	void display()
	{
		Node* p = head;
		while (p != NULL)
		{
			cout << "<" << p->data << ">";
			p = p->link;
		}
		cout << endl;
	}

};