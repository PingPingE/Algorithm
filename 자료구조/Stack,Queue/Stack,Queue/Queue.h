#pragma once
#include<iostream>
#include "error.h"
using namespace std;
#define MAX_SIZE 30 //���� ũ��

class Queue //FIFO
{
private:
	int *data;
	int front;
	int rear;
public:
	Queue():front(0),rear(0){ data = new int[MAX_SIZE]; } // data�����Ҵ� �� front, rear 0�ʱ�ȭ
	~Queue() { delete data; } //�Ҵ� ����
	
	bool isEmpty()
	{
		return front == rear; // front�� rear�� ������ �Ǹ� empty����
	}
	
	bool isFull()
	{
		return rear == MAX_SIZE - 1; //���̻� �߰��� ������ ����(������ front �տ� ������ ���� �� �ֱ⿡ ��ȯť�� ȿ����)
	}

	void enqueue(int val)
	{
		if (isFull())
			error("��á��");//�ش� �޼��� ��� �� ����
		data[rear++] = val; //�ڿ��� �����Ƿ� rear�� ++ (����� rear�� ���� ������ �����͸� ����Ű�°� X )
		//�� ���� ������� ����Ŵ
	}
	
	int dequeue()
	{
		if (isEmpty())
			error("�����");//�ش� �޼��� ��� �� ����
		return data[front++]; //�տ��� ���������Ƿ� front++
	}

	void display()
	{
		for (int i = front; i < rear; i++)
			cout << data[i] << " ";
		cout << endl;
	}

};