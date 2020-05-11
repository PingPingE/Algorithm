/*
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
*/
#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
int main()//1984kb	0ms
{
	int N;
	char board[26][26];
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
			cin >> board[i][j];
	}

	int dy[4] = { -1,1,0,0 }, dx[4] = { 0,0,-1,1 };
	bool done[26][26] = { 0, };
	vector<int> total_cnt;
	for (int r = 0; r < N; r++)
	{
		for (int c = 0; c < N; c++)
		{
			if (!done[r][c] && board[r][c] == '1')
			{
				int local_cnt = 1;
				done[r][c] = 1;
				queue<pair<int, int>> que;
				que.push(pair<int, int>(r, c));
				while (!que.empty())
				{
					pair<int, int> rc = que.front();
					que.pop();
					for (int d = 0; d < 4; d++)
					{
						int ny = rc.first + dy[d], nx = rc.second + dx[d];
						if (ny < 0 || nx < 0 || ny >= N || nx >= N || board[ny][nx] == '0' || done[ny][nx])
							continue;
						done[ny][nx] = 1;
						que.push(pair<int, int>(ny, nx));
						local_cnt++;
					}
				}
				total_cnt.push_back(local_cnt);
			}
		}
	}
	cout << total_cnt.size() << "\n";
	sort(total_cnt.begin(), total_cnt.end());
	for (auto i : total_cnt)
		cout << i << "\n";

	return 0;
}