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
void dfs(int, bool*, int);//진행중인 index(첫시작은 -1로), sum에 포함한거 체크, 현재까지의 sum
int sol2(int, int, bool);
int main()
{
	scanf("%d%d", &N, &S);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	bool done[21];
	for (auto& i : done)
		i = false;
	dfs(-1, done, 0); //S가 0인경우, 돌지 않고 바로 cnt++을 해버리므로 첫 시작을 표시하기 위해 cur_i=-1로 초기화
	cnt = sol2(0, 0, 0);
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
//sol2) -> 1984kb, 4ms(시간 반으로 줄어듦)
int sol2(int cur_i, int cur_sum, bool done) //현재 index, 현재sum, 하나라도 집합에 포함했는지
{
	if (cur_i == N) // 중간에 sum이 S라고 return하면 X 끝까지 다 돌고 return해야함(뒤에가 0일 수도 있고, -1, 1이런식일수잇음
		if (cur_sum == S && done)
			return 1;
		else
			return 0;
	return sol2(cur_i + 1, cur_sum, done + 0) + sol2(cur_i + 1, cur_sum + arr[cur_i], 1); //부분집합에 미포함, 포함
}