/*
N개의 정수 A[1],A[2] ... A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램
1<=N<=100000
1<=M<=100000
M개의 수들이 A[1]~A[N]에 있는지(있으면 1 없으면 0)
각 수는 -2^31~(2^31)-1
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
using namespace std;
bool check(int, int[], int);
int main() //2252kb 52ms 
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int arr_N[100001];
	int N, M, i = 0, j = 0, int_M;
	cin >> N;
	for (; i < N; i++)
		cin >> arr_N[i];
	cin >> M;
	sort(arr_N, arr_N + N);
	while (M--)//-> 만약 bool check함수 따로 안만들고 while 문안에서 연산을 다 돌았으면 52ms->60ms
	{
		cin >> int_M;
		cout << check(int_M, arr_N, N) << "\n";
	}
	return 0;
}
//만약 arr_N, N을 전역변수로 선언해서 함수에 인자로 안넘겼다면 52ms->56ms로 시간 증가 + 2252kb -> 2376kb로 메모리도 증가
bool check(int target, int arr_N[], int N)
{
	int r = N - 1;
	int l = 0;
	while (r >= l)
	{
		int m = (r + l) / 2;
		if (arr_N[m] == target) {
			return 1;
		}
		else if (arr_N[m] > target)
			r = m - 1;
		else
			l = m + 1;
	}
	return 0;
}
/*
int N;
int A[1000001];
bool check(int);
int main()
{
	int M;
	cin >> N;
	//cin -> scanf로 바꾸니 런타임에러 ->정답
	for (int i = 0; i < N; i++)
		scanf("%d", &A[i]);
	sort(A, A + N);//오름차순 정렬

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
}*/