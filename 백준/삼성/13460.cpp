/*
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고,
보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다.
게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.


첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
*/
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