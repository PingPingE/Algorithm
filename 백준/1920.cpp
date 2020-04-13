/*
N���� ���� A[1],A[2] ... A[N]�� �־��� ���� ��, �� �ȿ� X��� ������ �����ϴ��� �˾Ƴ��� ���α׷�
1<=N<=100000
1<=M<=100000
M���� ������ A[1]~A[N]�� �ִ���(������ 1 ������ 0)
�� ���� -2^31~(2^31)-1
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
using namespace std;
int N;
int A[1000001];
bool check(int);
int main()
{
	int M;
	cin >> N;
	//cin -> scanf�� �ٲٴ� ��Ÿ�ӿ��� ->����
	for (int i = 0; i < N; i++)
		scanf("%d", &A[i]);
	sort(A, A + N);//�������� ����

	int m;
	cin >> M;
	for (int i = 0; i < M; i++)
	{
		scanf("%d", &m);
		printf("%d\n", check(m));
	}

	return 0;
}
bool check(int target)
{
	int m = 0;
	int l = 0;
	int r = N - 1;
	while (l <= r)
	{
		m = (int)(l + r) / 2;
		if (A[m] == target)
			return 1;
		else if (A[m] > target)
			r = m - 1;
		else
			l = m + 1;
	}

	return 0;
}