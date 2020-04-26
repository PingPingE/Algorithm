#include<iostream>
#include<queue>
using namespace std;
int N;
int res = 0;
void dfs(int[][21], int);
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N;
	int board[21][21];
	for (int i = 0; i < N; i++)
	{		for (int j = 0; j < N; j++)
		{
			cin >> board[i][j];
			res = max(res, board[i][j]);
		}
	}
	if (N == 1)
	{
		cout << res;
		return 0;
	}
	dfs(board,0);
	cout << res;
	return 0;
}
void dfs(int a[][21],int cnt)
{
	if (cnt == 5)
		return;
	for (int d = 0; d < 4; d++)
	{
		int tmp_board[21][21] = { 0, };
		if (d == 0)//상
		{
			
			//위로 다 올리기
			int a_[21][21] = { 0, };
			for (int q = 0; q < N; q++)//열
			{
				int t = 0;//행
				for (int w = 0; w < N; w++)//행
				{
					if (a[w][q] > 0)
					{
						
						a_[t++][q] = a[w][q];
					}
						
				}
			}
			for (int j = 0; j < N; j++)//열
			{
				int t = 0;
				int i = 0;
				while (i <N) //행
				{
					if (i+1 <N && a_[i][j] == a_[i+1][j])//위에 같은 값이 있으면
					{
						tmp_board[t++][j] = a_[i][j] + a_[i+1][j];
						res = max(res, a_[i][j] + a_[i + 1][j]);
						i += 2;
					}
					else
					{
						tmp_board[t++][j] = a_[i][j];
						res = max(res, a_[i][j]);
						i++;
					}
				}
			}
		}
		else if (d == 1)//하
		{
			
			//밑으로 다 내리기
			int a_[21][21] = { 0, };
			for (int q = 0; q < N; q++)//열
			{
				int t = N-1;//행
				for (int w = N-1; w >=0; w--)//행
				{
					if (a[w][q] > 0)
					{
						a_[t--][q] = a[w][q];
					}
						
				}
			}
			for (int j = 0; j < N; j++)//열
			{
				int t = N - 1;
				int i = N - 1;
				while (i >= 0) //행
				{
					if (i - 1 >= 0 && a_[i][j] == a_[i - 1][j])//위에 같은 값이 있으면
					{
						tmp_board[t--][j] = a_[i][j] + a_[i - 1][j];
						res = max(res, a_[i][j] + a_[i - 1][j]);
						i -= 2;
					}
					else
					{
						tmp_board[t--][j] = a_[i][j];
						res = max(res, a_[i][j]);
						i--;
					}
				}
			}
		}
		else if (d == 2) // 좌
		{
			
			//왼쪽으로 다 밀기
			int a_[21][21] = { 0, };
			for (int q = 0; q < N; q++)//행
			{
				int t = 0;//열
				for (int w = 0; w < N;  w++)//열
				{
					if (a[q][w] > 0)
					{
						
						a_[q][t++] = a[q][w];
					}
						
				}
			}

			for (int j = 0; j < N; j++)//행
			{
				int t = 0;
				int i = 0;
				while (i < N) //열
				{
					if (i+1 <N && a_[j][i] == a_[j][i+1])//옆에 같은 값이 있으면
					{
						tmp_board[j][t++] = a_[j][i] + a_[j][i + 1];
						res = max(res, a_[j][i] + a_[j][i +1]);
						i += 2;
					}
					else
					{
						tmp_board[j][t++] = a_[j][i];
						res = max(res, a_[j][i]);
						i++;
					}
				}
			}
		}
		else //우
		{
			
			//오른쪽으로 다 밀기
			int a_[21][21] = { 0, };
			for (int q = 0; q < N; q++)//행
			{
				int t = N - 1;//열
				for (int w = N - 1; w >= 0; w--)//열
				{
					if (a[q][w] > 0)
					{
						
						a_[q][t--] = a[q][w];
					}
						
				}
			}
			
			for (int j = 0; j < N; j++)//행
			{
				int t = N-1;
				int i = N - 1;
				while(i>=0) //열
				{
					if (i-1>=0 && a_[j][i] == a_[j][i - 1])//옆에 같은 값이 있으면
					{
						tmp_board[j][t--] = a_[j][i] + a_[j][i - 1];
						res = max(res, a_[j][i] + a_[j][i - 1]);
						i -= 2;
					}
					else
					{
						tmp_board[j][t--] = a_[j][i];
						res = max(res, a_[j][i]);
						i--;
					}
				}
			}
		}
		dfs(tmp_board, cnt + 1);
	}
}