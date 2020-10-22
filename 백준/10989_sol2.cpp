#include <iostream>
using namespace std;
int main()
{	// 1984kb	2580ms
	int N = 0;
	cin >> N;
	int A[10001] = { 0, };
	for (int i = 0; i < N; i++)
	{
		int tmp = 0;
		//scanf_s("%d", &tmp);
		cin >> tmp;
		A[tmp] ++;
	}
	for (int i = 0; i < 10001; i++)
	{
		while (A[i] > 0)
		{
			printf("%d\n", i);
			--A[i];
		}
	}

	//메모리 초과
	/*
	priority_queue<int, vector<int>, greater<int>> pq;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int tmp = 0; 
		scanf_s("%d", &tmp);
		pq.push(tmp);
	}
	while (!pq.empty())
	{
		printf("%d\n",pq.top());
		pq.pop();
	}

	*/
	
	return 0;
}
