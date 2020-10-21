/*
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
*/
//2376kb	64ms
#include <iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
int A[100001];
int N;
int find(int target);

inline void getInt(int &n) {
	n = 0;
	char ch = getchar();
	char sign = 1;
	while (ch < '0' || ch > '9') 
	{ 
		if (ch == '-')
			sign = -1; 
		ch = getchar();//공백
	}
	while (ch >= '0' && ch <= '9')
	{
		n = (n << 3) + (n << 1) + ch - '0';
		ch = getchar();//공백
	}
	n = n*sign;
}
int main()
{	
	int M=0;
	getInt(N);
	for (int i = 0; i < N; i++)
	{
		getInt(A[i]);
	}
	sort(A,A+N);
	cin >> M;
	for (int j = 0; j < M; j++)
	{
		int target = 0;
		getInt(target);
		printf("%d\n",find(target));
	}
	return 0;
}
int find(int target)
{
	int low = 0, high = N, mid = 0;
	while (low <= high)
	{
		mid = int((low + high) / 2);
		if (A[mid] == target)
			return 1;
		else if (A[mid] > target)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return 0;
}