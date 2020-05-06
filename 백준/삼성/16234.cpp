#include<iostream>
#include<queue>
using namespace std;
int board[51][51];
//2124kb 388ms
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int N, L, R;
	cin >> N >> L >> R;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> board[i][j];
	int res = 0, cnt = 1;
	int dy[4] = { -1,1,0,0 }, dx[4] = { 0,0,-1,1 };

	while (cnt > 0)
	{
		cnt = 0;//국경선 연 나라 수
		int done[51][51] = { 0 };
		int num = 1;//다른 연합국 표시
		for (int i = 0; i < N; i++)
		{
			int ny, nx;
			for (int j = 0; j < N; j++)
			{
				if (done[i][j] > 0)
					continue;
				bool stat = 0;
				queue<pair<int, int>> que;
				que.push(pair<int, int>(i, j));
				while (!que.empty())
				{
					pair<int, int> p = que.front();
					que.pop();
					for (int d = 0; d < 4; d++)
					{
						ny = p.first + dy[d];
						nx = p.second + dx[d];
						if (ny < 0 || nx < 0 || ny >= N || nx >= N || done[ny][nx] >0)
							continue;
						int target = abs(board[p.first][p.second] - board[ny][nx]);
						if (target > R || target < L)
							continue;
						done[ny][nx] = num;
						que.push(pair<int, int>(ny, nx));
						stat = 1;
					}
				}
				if (stat)
				{
					done[i][j] = num;
					num++;
					cnt++;
				}
			}
		}
		
		if (cnt > 0)
		{
			bool p_done[51][51] = { 0 };
			for (int r = 0; r < N; r++)
			{
				for (int c = 0; c < N; c++)
				{
					if (done[r][c]>0 && !p_done[r][c])
					{
						int t_num = done[r][c];
						p_done[r][c] = 1;
						int ny, nx, total_pop = board[r][c], total_area = 1;
						queue<pair<int, int>> pop_moving;//같은 연합국 위치
						queue<pair<int, int>> que;
						que.push(pair<int, int>(r, c));
						//연합국 탐색 -> 총 인구, 총 칸 수 구하기
						while (!que.empty())
						{
							pair<int, int> p = que.front();
							que.pop();
							pop_moving.push(p);
							for (int d = 0; d < 4; d++)
							{
								ny = p.first + dy[d];
								nx = p.second + dx[d];
								if (ny < 0 || nx < 0 || ny >= N || nx >= N || p_done[ny][nx] || done[ny][nx] != t_num)//범위 이탈,이미 방문, 연합국이 아닌 경우
									continue;
								p_done[ny][nx] = 1;
								total_pop += board[ny][nx];
								total_area++;
								que.push(pair<int, int>(ny, nx));
							}
						}
						while (!pop_moving.empty())
						{
							pair<int, int>p = pop_moving.front();
							pop_moving.pop();
							board[p.first][p.second] = (int)(total_pop / total_area);
						}

					}
				}
			}
			res++;
		}

	}
	cout << res;
	return 0;
}