#pragma once
#include "Node.h"
#include <iostream>
using namespace std;
class LinkedList
{
private:
	Node* head;
public:
	LinkedList() : head(NULL) {} //�ʱ�ȭ
	~LinkedList() {}
	void insert(int val) //���ο� ������ ����
	{
		Node* n = new Node; //���ο� ��� ����
		n->data = val; //������ ����
		n->link = head; //������ �߰�
		head = n;

	}
	void remove(int val)
	{
		Node* finder = head;
		if (finder->data != val)
		{
			Node* next = finder->link;
			while (next->data != val) // ���� ��忡 ã�� �����Ͱ� ������
			{
				finder = finder->link;//��� ��������
				next = finder->link;
			}

			finder->link = next->link; //finder�� ��� ��带 ����Ŵ(�� ��� ����� �� �����)
			//finder�� ��� ����� ���� ��带 ����Ű���� �Ѵ�.
		}
		else //head�� ����Ű�� ��尡 �������
		{
			head = finder->link; //head�� �ٲ��ش�.
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