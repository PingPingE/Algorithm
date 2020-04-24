/*
치킨 배달

크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 
도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 
즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

*/
#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
const int INF = 987654321;
struct RC
{
	int y, x;
};
RC chicken[14];
RC house[101];
int res = INF;
int countBit(int);
int main() //1988kb	132ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int N, M, tmp, h= 0, c= 0; // h: 집 인덱스, c: 치킨집 인덱스
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> tmp;
			if (tmp == 1)
			{
				RC  tmp_h = { i,j };
				house[h++] = tmp_h;
			}
			else if (tmp == 2)
			{
				RC tmp_c = { i,j };
				chicken[c++] = tmp_c;
			}
		}
	}
	for (int k = 0; k <(1<<c); k++)
	{
		if (countBit(k) >=1 && countBit(k) <= M)
		{
			int sum = 0;
			map<int, int> map_house;//house의 인덱스, 이번 조합에서의 치킨거리
			for (int t_h = 0; t_h < h; t_h++)
				map_house[t_h] = INF; // 초기화
			for (int g = 0; g < c; g++)
			{
				if (k & 1 << g)
				{
					int chy = chicken[g].y;
					int chx = chicken[g].x;
					
					for (int d = 0; d < h; d++)
					{
						map_house[d] = min(map_house[d], abs(chy - house[d].y) + abs(chx - house[d].x));
					}
				}
			}
			for (int t_h = 0; t_h < h; t_h++)
			{
				sum += map_house[t_h];
			}
			res = min(res, sum);
		}
	}
	cout << res;
	return 0;
}
int countBit(int num)
{
	int cnt = 0;
	while (num) {
		if (num & 1)
			cnt+=1;
		num = num >> 1;
	}
	return cnt;
}