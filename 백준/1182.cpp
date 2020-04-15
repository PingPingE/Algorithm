/*
N개의 정수로 이루어진 수열이 있을 때,
크기가 양수인 부분수열 중 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하라
1<=N<=20
abs(S)<=1000000
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int cnt = 0;
int cnt_ = 0;
int arr[21];
int N, S;
void dfs(int, bool*, int);
int dp(int, int, bool);
int main()
{
	scanf("%d%d", &N, &S);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	bool done[21];
	for (auto& i : done)
		i = false;
	dfs(-1, done, 0); //S가 0인경우, 돌지 않고 바로 cnt++을 해버리므로 첫 시작을 표시하기 위해 cur_i=-1로 초기화
	cnt = dp(0, 0, 0);
	cout << cnt << ' ' << cnt_;
	return 0;
}
//sol1) 1984kb, 8ms
void dfs(int cur_i, bool *done, int cur_sum)
{

	if (cur_i != -1 && cur_sum == S)//여기서 return을 해버린 것이 문제였다. 정답에 도달해도 더 봐야한다.
	{
		/*for(int i =0; i<N; i++)
		cout << done[i] << ' ';
		cout << endl;
		*/
		cnt_++;
	}
	if (cur_i == -1)
		cur_i = 0;
	else if (cur_i >= N)
		return;

	for (int i = cur_i; i<N; i++)
	{
		if (!done[i])
		{
			done[i] = true;
			dfs(i, done, cur_sum + arr[i]);
			done[i] = false;
		}
	}
}
//sol2) dp -> 1984kb, 4ms(시간 반으로 줄어듦)
int dp(int cur_i, int cur_sum, bool done)
{
	if (cur_i == N)
		if (cur_sum == S && done)
			return 1;
		else
			return 0;
	return dp(cur_i + 1, cur_sum, done + 0) + dp(cur_i + 1, cur_sum + arr[cur_i], 1); //부분집합에 미포함, 포함
}