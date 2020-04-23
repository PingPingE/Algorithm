#include<iostream>
#include<queue>
using namespace std;
const int INF = 987654321;
struct ball 
{
	int y, x, dir, cnt;
};
int dy[4] = { -1,1,0,0 };
int dx[4] = { 0,0,-1,1 };
ball blueBack(ball);
ball redBack(ball);
int main() //142276kb 180ms
{
	char board[11][11];
	int N,M;
	cin >> N >> M;
	queue<pair<ball,ball>> que;
	ball red;
	ball blue;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> board[i][j];
			if (board[i][j] == 'R')
			{
				red = { i,j,0,1};
			}
			else if (board[i][j] == 'B')
			{
				blue = { i,j,0,1};
			}
		}
	}
	for (int d = 0; d < 4; d++)//4방 모두 넣어서
	{
		pair<ball, ball> p;
		red.dir = d;
		blue.dir = d;
		p = pair<ball, ball>(red, blue);
		que.push(p);
	}
	
	int res = INF;
	while (!que.empty())
	{
		pair<ball, ball> q = que.front();
		que.pop();
		red = q.first;
		blue = q.second;
		if (red.cnt > 10)
			break;
		if (red.cnt >= res)
			continue;
		bool stat[2] = { 0,0 };//red 골여부, blue 골여부
		int r_ny, r_nx, b_ny, b_nx;
		
		r_ny = red.y + dy[red.dir];
		r_nx = red.x + dx[red.dir];

		while (1)
		{
			if (board[r_ny][r_nx] == '#')
			{
				ball new_r = { r_ny, r_nx,red.dir,red.cnt };
				new_r = redBack(new_r);
				r_ny = new_r.y;
				r_nx = new_r.x;
				break;
			}
				
			else if (board[r_ny][r_nx] == 'O')
			{
				stat[0] = 1;
				break;
			}
			r_ny += dy[red.dir];
			r_nx += dx[red.dir];
		}
		

		b_ny = blue.y + dy[blue.dir];
		b_nx = blue.x + dx[blue.dir];
		while (1)
		{
			if (board[b_ny][b_nx] == '#')
			{
				ball new_b = { b_ny,b_nx,blue.dir,blue.cnt };
				new_b = blueBack(new_b);
				b_ny = new_b.y;
				b_nx = new_b.x;
				break;
			}
			else if (board[b_ny][b_nx] == 'O')
			{
				stat[1] = 1;
				break;
			}
			b_ny += dy[blue.dir];
			b_nx += dx[blue.dir];

		}

		if (b_ny == r_ny && r_nx == b_nx)//둘이 같은곳에 있는경우
		{
			int b = abs(b_ny - blue.y) + abs(b_nx - blue.x);
			int a = abs(r_ny - red.y) + abs(r_nx - red.x);
			if (a < b)//red가 차지
			{
				ball new_b = { b_ny,b_nx,blue.dir,blue.cnt };
				new_b = blueBack(new_b);
				b_ny = new_b.y;
				b_nx = new_b.x;
			}
			else//blue가 차지
			{
				ball new_r = { r_ny, r_nx,red.dir,red.cnt };
				new_r = redBack(new_r);
				r_ny = new_r.y;
				r_nx = new_r.x;
			}
		}

		if (stat[0] && !stat[1])
			res = res > red.cnt ? red.cnt : res;
		else if (stat[1] == 1)
			continue;
		else
		{
			ball next_r, next_b;
			for (int d = 0; d < 4; d++)
			{
				next_r = { r_ny,r_nx,d,red.cnt + 1 };
				next_b = { b_ny, b_nx, d, blue.cnt + 1 };
				que.push(pair<ball, ball>(next_r, next_b));
			}
		}
	}
	if (res == INF)
	{
		cout << -1;
	}
	else
		cout << res;
	return 0;
}
ball redBack(ball red)
{
	if (red.dir == 0)
	{
		red.y += dy[1];
		red.x += dx[1];
	}
	else if (red.dir == 1)
	{
		red.y += dy[0];
		red.x += dx[0];

	}
	else if (red.dir == 2)
	{
		red.y += dy[3];
		red.x += dx[3];
	}
	else
	{
		red.y += dy[2];
		red.x += dx[2];
	}
	return red;
}
ball blueBack(ball blue)
{
	
	if (blue.dir == 0)
	{
		blue.y += dy[1];
		blue.x += dx[1];
	}
	else if (blue.dir == 1)
	{
		blue.y += dy[0];
		blue.x += dx[0];
	}
	else if (blue.dir == 2)
	{
		blue.y += dy[3];
		blue.x += dx[3];
	}
	else
	{
		blue.y += dy[2];
		blue.x += dx[2];
	}
	return blue;
}