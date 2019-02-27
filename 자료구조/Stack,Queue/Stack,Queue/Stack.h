#pragma once
#include <iostream>
#include "error.h"
#define MAX_SIZE 30 //���� ũ��
using namespace std;


class Stack //LIFO
{
private:
	int top; //���� �ֱٿ� ���� ������
	int *data; //������ ���� ����
public:
	Stack() :top(-1) { data = new int[MAX_SIZE]; } //top=-1 �ʱ�ȭ, data �����Ҵ�
	
	~Stack() { delete data; }; // �Ҵ�����
	
	bool isEmpty() 
	{
		return top == -1;
	}
	bool isFull()
	{
		return top == MAX_SIZE-1;
	}

	void push(int val) //������ ����
	{
		if (isFull())
			error("��á��"); //�ش� �޼��� ��� �� ����
		data[++top] = val; //top ���� val ����
		
	}

	int pop() //������ ����
	{
		if (isEmpty())
			error("�����");//�ش� �޼��� ��� �� ����
		return data[top--]; //top��ġ�� ������ ���� �� --

	}
	
	int peek() //top ������ Ȯ��
	{ 
		if (isEmpty()) 
			error("�����");//�ش� �޼��� ��� �� ����
		return data[top]; //top��ġ�� ������ ����
	}

	void display() //�ؿ������� ���
	{
		for (int i = 0; i <= top; i++)
			cout << data[i] << " ";
		cout << endl;
	}

};