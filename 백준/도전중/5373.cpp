#include<iostream>
#include<string>
#include<deque>
using namespace std;
char cube[6][3][3];
char col_list[6] = { 'o','r','g','b','y','w' };//뒤,앞,왼,오,아,위
void rotate(char, int);
void print();
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	
	int T,N;
	cin >> T;
	while (T--)
	{
		for (int c = 0; c < 6; c++)
		{
			char col = col_list[c];
			for (int i = 0; i < 3; i++)
			{
				for (int j = 0; j < 3; j++)
					cube[c][i][j] = col;
			}
		}
		cin >> N;
		string s;
		while (N--)
		{
			char dir, op;
			cin >> dir>>op;
			if (op == '-')
				rotate(dir, 3);
			else
				rotate(dir, 1);
		}
		print();
	}

	return 0;
}
void print()
{
	for (int i = 0; i < 3; i++)
	{
		for (int j = 2; j>=0; j--)
			cout << cube[5][i][j];
		cout << "\n";
	}
}
void rotate(char op, int rot_num)
{
	deque<char> deq;
	if (op == 'B')
	{
		int arr_list[4] = { 5,2,4,3 };//위왼아오
		
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			while (j<3)
				deq.push_back(cube[arr_list[i]][0][j++]);
		}
		while (rot_num--)//왼쪽으로
		{
			for (int k = 0; k < 3; k++)
			{
				deq.push_back(deq.front());
				deq.pop_front();
			}
		}
		//다시 넣기
		int d = 0;
		for (int i = 0; i < 4; i++)
		{
			int j = 0;
			while (j < 3)
				cube[arr_list[i]][0][j++] = deq[d++];
		}
	}
	else if (op == 'F')
	{
		int arr_list[4] = { 5,2,4,3 };//위왼아오
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			while (j<3)
				deq.push_back(cube[arr_list[i]][2][j++]);
		}
		while (rot_num--)//오른쪽으로
		{
			for (int k = 0; k < 3; k++)
			{
				deq.push_front(deq.back());
				deq.pop_back();
			}
		}
		//다시 넣기
		int d = 0;
		for (int i = 0; i < 4; i++)
		{
			int j = 0;
			while (j < 3)
				cube[arr_list[i]][2][j++] = deq[d++];
		}
	}
	else if (op == 'L')
	{
		int arr_list[4] = {0,5,1,4};//뒷위앞아
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			if (i == 5)
			{
				while (j<3)
					deq.push_back(cube[arr_list[i]][j++][2]);
			}
			else
			{
				while (j<3)
					deq.push_back(cube[arr_list[i]][j++][0]);
			}
			
		}
		while (rot_num--)//오른쪽으로
		{
			for (int k = 0; k < 3; k++)
			{
				deq.push_front(deq.back());
				deq.pop_back();
			}
		}
		//다시 넣기
		int d = 0;
		for (int i = 0; i < 4; i++)
		{
			int j = 0;
			if (i == 5)
			{
				while (j < 3)
					cube[arr_list[i]][j++][2] = deq[d++];
			}
			else
			{
				while (j < 3)
					cube[arr_list[i]][j++][0] = deq[d++];
			}
		}
		
	}
	else if (op == 'R')
	{
		int arr_list[4] = { 0,5,1,4 };//뒷위앞아
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			if (i == 5)
			{
				while (j<3)
					deq.push_back(cube[arr_list[i]][j++][0]);
			}
			else
			{
				while (j<3)
					deq.push_back(cube[arr_list[i]][j++][3]);
			}

		}
		while (rot_num--)//왼쪽으로
		{
			for (int k = 0; k < 3; k++)
			{
				deq.push_back(deq.front());
				deq.pop_front();
			}
		}
		//다시 넣기
		int d = 0;
		for (int i = 0; i < 4; i++)
		{
			int j = 0;
			if (i == 5)
			{
				while (j < 3)
					cube[arr_list[i]][j++][0] = deq[d++];
			}
			else
			{
				while (j < 3)
					cube[arr_list[i]][j++][3] = deq[d++];
			}
		}
	}
	else if (op == 'D')
	{
		int arr_list[4] = { 0,3,1,2 };//뒷오앞왼
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			if (i == 0)
				deq.push_back(cube[arr_list[i]][2][j++]);
			else if (i == 1)
				deq.push_back(cube[arr_list[i]][0][j++]);
			else if (i == 3)
				deq.push_back(cube[arr_list[i]][j++][0]);
			else
				deq.push_back(cube[arr_list[i]][j++][2]);
		}
		while (rot_num--)//오른쪽으로
		{
			for (int k = 0; k < 3; k++)
			{
				deq.push_front(deq.back());
				deq.pop_back();
			}
		}
		//다시 넣기
		int d = 0;
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			if (i == 0)
				cube[arr_list[i]][2][j++] = deq[d++];
			else if (i == 1)
				cube[arr_list[i]][0][j++] = deq[d++];
			else if (i == 3)
				cube[arr_list[i]][j++][0] = deq[d++];
			else
				cube[arr_list[i]][j++][2] = deq[d++];
		}
	}
	else//윗면
	{
		int arr_list[4] = { 0,3,1,2 };//뒷오앞왼
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			if (i == 0)
				deq.push_back(cube[arr_list[i]][0][j++]);
			else if (i == 1)
				deq.push_back(cube[arr_list[i]][2][j++]);
			else if (i == 3)
				deq.push_back(cube[arr_list[i]][j++][2]);
			else
				deq.push_back(cube[arr_list[i]][j++][0]);
		}
		while (rot_num--)//오른쪽으로
		{
			for (int k = 0; k < 3; k++)
			{
				deq.push_front(deq.back());
				deq.pop_back();
			}
		}
		//다시 넣기
		int d = 0;
		for (int i = 0; i <4; i++)
		{
			int j = 0;
			if (i == 0)
				cube[arr_list[i]][0][j++] = deq[d++];
			else if (i == 1)
				cube[arr_list[i]][2][j++] = deq[d++];
			else if (i == 3)
				cube[arr_list[i]][j++][2] = deq[d++];
			else
				cube[arr_list[i]][j++][0] = deq[d++];
		}
	}
	for (auto i : deq)
		cout << i << " ";
	cout << endl;
}