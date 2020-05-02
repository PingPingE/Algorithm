#include<iostream>
#include<map>
#include <vector>
#include<algorithm>
using namespace std;
int ar = 0, ac = 3;
int A[101][101] = { 0, };
void R();
void C();
int main() //2028kb	4ms
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int r, c, k;
	cin >> r >> c >> k;
	r -= 1;
	c -= 1;
	for (ar; ar < 3; ar++)
	{
		cin >> A[ar][0] >> A[ar][1] >> A[ar][2];
	}
	//ar, ac는 다음에 들어갈 칸을 가리킴
	int T = 0;
	while (T < 101)//100이 아니라 101...
	{
		if (A[r][c] == k) //종료 조건
		{
			cout << T;
			return 0;
		}
		T++;

		if (ar >= ac)
			R();
		else
			C();
	}
	cout << -1;
	return 0;
}
bool cmp(pair<int, int> a, pair<int, int> b)
{
	return a.second != b.second ? a.second < b.second : a.first < b.first;
}
void R()
{
	int maxCol= 0;
	for (int i = 0; i < ar; i++)
	{
		map<int, int> count;
		int j = 0;
		int c_ = 0;
		while(c_<ac)
		{
			if (A[i][c_] > 0)
			{
				j++;
				count[A[i][c_]] += 1;
			}
			c_++;
		}
		vector<pair<int,int>>vec;
		map<int, int>::iterator v;
		for (v = count.begin(); v != count.end(); v++)
			vec.push_back(make_pair(v->first, v->second));
		sort(vec.begin(), vec.end(), cmp);
		int countC = 0;
		for (int v_ind =0 ; v_ind<vec.size(); v_ind++)
		{
			A[i][countC++] = vec[v_ind].first;
			if (countC > 99)
				break;
			A[i][countC++] = vec[v_ind].second;
			if (countC > 99)
				break;
		}
		maxCol = max(maxCol, countC);
		while (countC < 100)
			A[i][countC++] = 0;
	}
	//최대 컬럼 개수 갱신
	ac = maxCol;		
}
void C()
{
	int maxRow = 0;
	for (int j = 0; j < ac; j++)
	{
		int i = 0;
		map<int, int>count;
		int r_ = 0;
		while (r_ <ar)
		{
			if(A[r_][j] >0)
			{
				i++;
				count[A[r_][j]] += 1;
			}
			r_++;
		}
		vector<pair<int, int>>vec;
		map<int, int>::iterator v;
		
		for (v = count.begin(); v != count.end(); v++)
			vec.push_back(make_pair(v->first, v->second));

		sort(vec.begin(), vec.end(), cmp);
		int countR = 0;
		for (int v_ind = 0; v_ind<vec.size(); v_ind++)
		{
			A[countR++][j] = vec[v_ind].first;
			if (countR>99)
				break;
			A[countR++][j] = vec[v_ind].second;
			if (countR>99)
				break;
		}
		maxRow = max(maxRow, countR);
		while (countR < 100)
			A[countR++][j] = 0;

	}
	//최대 행 개수 갱신
	ar = maxRow;
}