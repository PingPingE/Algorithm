//3시간 반
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
using namespace std;
int N, M, T;
int board[60][60];
void rotate(int, int, int);
void check();
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N >> M >> T;
	int i = 1;
	for (; i <= N; i++)
		for (int j= 1; j <= M; j++)
			cin >> board[i][j];
		
	int x, d, k;
	int cnt = 0;
	while (T--)
	{
		cin >> x >> d >> k;
		for (int u = x; u <= N; u += x)//x의 배수
		{
			rotate(u, d, k);
		}
		
		check();//인접한거 지우기
	
	}
	for (int u = 1; u <= N; u++)
	{
		for (int uu = 1; uu <= M; uu++)
		{
			cnt += board[u][uu];
		}
	}
	
	cout << cnt;
	return 0;
}
void rotate(int u,int d, int k)//원판 회전
{
	int tmp[60];
	if (d)//반시계
	{
		int x = 1;
		for (int i = 1 + k; i <= M; i++)
		{
			tmp[x++] = board[u][i];
		}
		for (int i = 1; i < 1 + k; i++)
		{
			tmp[x++] = board[u][i];
		}
	}
	else //(N+1)-k만큼
	{
		int x = 1;
		for (int i = (M + 1) - k; i <= M; i++)
		{
			tmp[x++] = board[u][i];
		}
		for (int i = 1; i < (M + 1) - k; i++)
		{
			tmp[x++] = board[u][i];
		}

	}
	for (int i = 1; i <= M; i++) //복사
	{
		board[u][i] = tmp[i];
	}
}

void check()
{
	int first_check = 0;
	int total_sum = 0;
	for (int a = 1; a <= N; a++)
	{
		for (int b = 1; b <= M; b++)
			if (board[a][b] > 0)
			{
				total_sum += board[a][b];
				first_check += 1;
			}
	}
	if (first_check > 0)
	{
		bool stat[60][60] = { 0, };
		bool check_cnt = 0;
		for (int i = 1; i <= N; i++)
		{
			if (board[i][1] != 0 && board[i][1] == board[i][2])
			{
				stat[i][2] = 1;
				stat[i][1] = 1;
				check_cnt = 1;
			}

			if (board[i][M] != 0 && board[i][M] == board[i][M - 1])
			{
				stat[i][M - 1] = 1;
				stat[i][M] = 1;
				check_cnt = 1;
			}

			if (board[i][M] != 0 && board[i][M] == board[i][1])
			{
				stat[i][1] = 1;
				stat[i][M] = 1;
				check_cnt = 1;
			}

			for (int j = 1; j <= M; j++)
			{
				if (board[1][j] > 0 && board[1][j] == board[2][j])
				{
					stat[1][j] = 1;
					stat[2][j] = 1;
					check_cnt = 1;
				}
				if (board[N][j] > 0 && board[N][j] == board[N - 1][j])
				{
					stat[N][j] = 1;
					stat[N - 1][j] = 1;
					check_cnt = 1;
				}
				if (board[i][j] == 0)
					continue;
				if (j >= 2 && j <= M - 1 && board[i][j] == board[i][j - 1])
				{
					stat[i][j] = 1;
					stat[i][j - 1] = 1;
					check_cnt = 1;
				}

				if (j >= 2 && j <= M - 1 && board[i][j] == board[i][j + 1])
				{
					stat[i][j] = 1;
					stat[i][j + 1] = 1;
					check_cnt = 1;
				}

				if (i >= 2 && i <= N - 1 && board[i][j] == board[i - 1][j])
				{
					stat[i][j] = 1;
					stat[i - 1][j] = 1;
					check_cnt = 1;
				}
				if (i >= 2 && i <= N - 1 && board[i][j] == board[i + 1][j])
				{
					stat[i][j] = 1;
					stat[i + 1][j] = 1;
					check_cnt = 1;
				}
			}

		}
		if (check_cnt)
		{
			for (int a = 1; a <= N; a++)
				for (int b = 1; b <= M; b++)
				{
					if (stat[a][b])
						board[a][b] = 0;
				}
		}
		else
		{
			float avg  =(float)total_sum/first_check;
			for (int a = 1; a <= N; a++)
				for (int b = 1; b <= M; b++)
				{
					if (board[a][b] > avg)
						board[a][b] -= 1;
					else if (board[a][b] > 0 && board[a][b] < avg)
						board[a][b] += 1;
				}
		}
	}
}