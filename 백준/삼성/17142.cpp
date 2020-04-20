#include<iostream>
#include<queue>
using namespace std;
int countBits(int);

struct Virus {
	int y;
	int x;
	int t = 1;
};
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };
int N, M, time;
int count_zero = 0;
int board[51][51] = { 0, };
Virus v[11];
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int tmp;
	cin >> N >> M;
	int v_cnt = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> tmp;
			if (tmp == 0)
				count_zero += 1;//초기 0개수 카운트
			else if (tmp == 2)
			{
				Virus t_v;
				t_v.y = i;
				t_v.x = j;
				v[v_cnt++] = t_v;
			}
			board[i][j] = tmp;
		}
	}
	if (count_zero == 0)
	{
		cout << 0;
		return 0;
	}
	time = (N*N) + 1; //초기 시간
	for (int i = 0; i < (1 << v_cnt); i++)
	{
		if (countBits(i) == M)
		{
			bool done[51][51] = { 0, };
			queue<Virus> que;
			for (int j = 0; j<v_cnt; j++)
			{
				if (i&(1 << j))
				{
					done[v[j].y][v[j].x] = 1;
					que.push(v[j]);
				}
			}

			int zero = count_zero;
			while (!que.empty())
			{
				Virus q_virus = que.front();
				que.pop();
				//cout << q_virus.t << endl;
				bool stat = 0;
				for (int i = 0; i < 4; i++)
				{
					int ny = q_virus.y + dy[i], nx = q_virus.x + dx[i];
					if (ny < 0 || nx < 0 || ny >= N || nx >= N || done[ny][nx] || board[ny][nx] == 1)
						continue;
					if (board[ny][nx] == 0)
					{
						zero -= 1;
						if (!zero)
						{
							stat = 1;
							time = time > q_virus.t ? q_virus.t : time;
							break;
						}
					}
					done[ny][nx] = 1;
					Virus tmp;
					tmp.x = nx;
					tmp.y = ny;
					tmp.t = q_virus.t + 1;
					que.push(tmp);
				}
				if (stat)
					break;
			}
		}
	}
	if (time == (N*N) + 1)
		cout << -1;
	else
		cout << time;
	return 0;
}
int countBits(int bits)
{
	int cnt = 0;
	while (bits)
	{
		//cout << bits << endl;
		if (bits & 1)
			cnt++;
		bits = bits >> 1;
	}
	return cnt;
}
