/*
스타트와 링크
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 

이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 

팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, 
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다
*/
#include<iostream>
#include<algorithm>
using namespace std;
int N;
int board[21][21];
const int INF = 987654321;
int res = INF;
int countBit(int);
int main() // 0ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> board[i][j];
	
	for (int b = 0; b < (1<<N); b++)
	{
		if (countBit(b) == N/2)
		{
			int tmp_sum2=0 , tmp_sum1= 0, t1=0, t2 = 0;
			int team1[21], team2[21];
			for (int j = 0; j < N; j++)
			{
				if (b & 1 << j)
					team1[t1++] = j;//team1배열에 해당 선수 인덱스 저장
				else
					team2[t2++] = j;
			}
			//team1의 능력치 sum 구하기
			for (int sum_t1 = 0; sum_t1 < t1; sum_t1++)
			{
				for (int with = 0; with < t1; with++)
				{
					tmp_sum1 += board[team1[sum_t1]][team1[with]];
				}
			}
			//team2의 능력치 sum 구하기
			for (int sum_t2 = 0; sum_t2 < t2; sum_t2++)
			{
				for (int with2 = 0; with2 < t2; with2++)
				{
					tmp_sum2 += board[team2[sum_t2]][team2[with2]];
				}
			}
			//cout << b <<" "<< tmp_sum1 <<" "<< tmp_sum2<<"\n";
			res = min(res, abs(tmp_sum1- tmp_sum2));
			if (res == 0)
				break;
			
		}
	}
	cout << res;
	return 0;
}
int countBit(int n)
{
	int cnt = 0;
	while (n)
	{
		if (n & 1)
			cnt++;
		n = n >> 1;
	}
	return cnt;
}