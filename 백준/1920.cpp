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
	while (M--)//-> ���� bool check�Լ� ���� �ȸ���� while ���ȿ��� ������ �� �������� 52ms->60ms
	{
		cin >> int_M;
		cout << check(int_M, arr_N, N) << "\n";
	}
	return 0;
}
//���� arr_N, N�� ���������� �����ؼ� �Լ��� ���ڷ� �ȳѰ�ٸ� 52ms->56ms�� �ð� ���� + 2252kb -> 2376kb�� �޸𸮵� ����
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
}*/