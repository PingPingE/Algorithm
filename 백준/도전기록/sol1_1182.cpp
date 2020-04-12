/*
N���� ������ �̷���� ������ ���� ��, 
ũ�Ⱑ ����� �κм��� �� �� ������ ���Ҹ� �� ���� ���� S�� �Ǵ� ����� ���� ���϶�
1<=N<=20
abs(S)<=1000000
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int cnt = 0;
int arr[21];
int N, S;
int dfs (int,bool*,int);
int main()
{
	cin >> N >> S;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	
	bool done[21];
	for (auto& i : done)
		i = false;
	dfs(-1, done,0);
	cout << cnt;
	return 0;
}
int dfs(int cur_i, bool *done, int cur_sum)
{
	if (cur_i != -1 && cur_sum == S)
	{
		for (int i = 0; i < N; i++)
			cout << done[i] << ' ';
		cout << endl;
		return 1;
	}
	if (cur_i >= N)
		return 0;
	if (cur_i == -1)
		cur_i = 0;
	for (int i=cur_i; i<N; i++)
	{
		if (!done[i])
		{
			done[i] = true;
			cnt += dfs(i, done, cur_sum+arr[i]);
			done[i] = false;
		}
	}
	return 0;
}