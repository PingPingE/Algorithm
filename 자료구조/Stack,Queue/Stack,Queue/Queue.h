#pragma once
#include<iostream>
#include "error.h"
using namespace std;
#define MAX_SIZE 30 //공간 크기

class Queue //FIFO
{
private:
	int *data;
	int front;
	int rear;
public:
	Queue():front(0),rear(0){ data = new int[MAX_SIZE]; } // data동적할당 및 front, rear 0초기화
	~Queue() { delete data; } //할당 해제
	
	bool isEmpty()
	{
		return front == rear; // front와 rear가 만나게 되면 empty상태
	}
	
	bool isFull()
	{
		return rear == MAX_SIZE - 1; //더이상 추가할 공간이 없음(하지만 front 앞에 공간이 있을 수 있기에 순환큐가 효율적)
	}

	void enqueue(int val)
	{
		if (isFull())
			error("꽉찼음");//해당 메세지 출력 후 종료
		data[rear++] = val; //뒤에서 들어오므로 rear만 ++ (참고로 rear는 가장 마지막 데이터를 가리키는게 X )
		//그 다음 빈공간을 가리킴
	}
	
	int dequeue()
	{
		if (isEmpty())
			error("비었음");//해당 메세지 출력 후 종료
		return data[front++]; //앞에서 빠져나가므로 front++
	}

	void display()
	{
		for (int i = front; i < rear; i++)
			cout << data[i] << " ";
		cout << endl;
	}

};