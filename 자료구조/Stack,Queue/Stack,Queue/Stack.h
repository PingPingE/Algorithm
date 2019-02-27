#pragma once
#include <iostream>
#include "error.h"
#define MAX_SIZE 30 //공간 크기
using namespace std;


class Stack //LIFO
{
private:
	int top; //제일 최근에 들어온 데이터
	int *data; //데이터 담을 공간
public:
	Stack() :top(-1) { data = new int[MAX_SIZE]; } //top=-1 초기화, data 동적할당
	
	~Stack() { delete data; }; // 할당해제
	
	bool isEmpty() 
	{
		return top == -1;
	}
	bool isFull()
	{
		return top == MAX_SIZE-1;
	}

	void push(int val) //데이터 삽입
	{
		if (isFull())
			error("꽉찼음"); //해당 메세지 출력 후 종료
		data[++top] = val; //top 위에 val 삽입
		
	}

	int pop() //데이터 삭제
	{
		if (isEmpty())
			error("비었음");//해당 메세지 출력 후 종료
		return data[top--]; //top위치의 데이터 리턴 후 --

	}
	
	int peek() //top 데이터 확인
	{ 
		if (isEmpty()) 
			error("비었음");//해당 메세지 출력 후 종료
		return data[top]; //top위치의 데이터 리턴
	}

	void display() //밑에서부터 출력
	{
		for (int i = 0; i <= top; i++)
			cout << data[i] << " ";
		cout << endl;
	}

};