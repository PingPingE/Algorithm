#include<iostream>
using namespace std;
int N;
void sol(int);
int res;
bool check(int);
int rc[16] = { 0 };
void main()//4936ms
{
	res = 0;
	cin >> N;
	sol(0);
	cout << res;
}

void sol(int row)
{
	for (int i = 0; i < N; i++)
	{
		rc[row] = i;
		if (check(row))
		{
			if (row == N - 1)
				res++;
			else
				sol(row + 1);
		}
	}
}

bool check(int r)
{
	for (int k = 0; k < r; k++)//row
	{
		if (abs(rc[k] - rc[r]) == abs(k - r) || rc[k] == rc[r])
			return 0;
	}
	return 1;
}
/*bool check(int, int);
void dfs(int, int);
int n, sum = 0;
bool board[16][16] = { 0, };
bool col[16] = { 0, };
int main() //4328ms
{
	cin >> n;
	dfs(0, 0); // 시작 행
	cout << sum;
	return 0;
}
void dfs(int cur_i, int pick)
{
	if (pick == n)
	{
		sum += 1;
		return;
	}
	if (cur_i == n)
		return;

	for (int j = 0; j < n; j++)
	{
		if (!col[j] && check(cur_i, j))
		{
			col[j] = 1;
			board[cur_i][j] = 1;
			dfs(cur_i + 1, pick + 1);
			board[cur_i][j] = 0;
			col[j] = 0;
		}
	}
}
bool check(int y, int x)
{
	for (int i = 0; i < n; i++)
	{
		if (x - i >= 0 && y - i >= 0 && board[y - i][x - i])
			return 0;
		if (x + i < n &&y + i < n&&board[y + i][x + i])
			return 0;
		if (x - i >= 0 && y + i < n&&board[y + i][x - i])
			return 0;
		if (x + i < n && y - i >= 0 && board[y - i][x + i])
			return 0;
	}
	return 1;
}*/