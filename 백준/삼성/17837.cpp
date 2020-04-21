#include <iostream>
#include<map>
#include<stack>
using namespace std;
int N, K;
int board[14][14];
struct horse
{
	int y, x, d, flag = 0;//방향(1:오, 2:왼, 3:위, 4:아래), 못움직이는 경우(1)
};
int dy[5] = { 0, 0,0,-1,1 };
int dx[5] = { 0, 1,-1,0,0 };
horse h_arr[11];//말 목록
map<pair<int, int>, stack<int>> h_map;// key:위치, value: 해당 말의 인덱스 순서대로 쌓기
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N >> K;
	for (int i = 1; i <= N; i++) //주의!! 1부터 N
		for (int j = 1; j <= N; j++)
			cin >> board[i][j]; //0은 흰, 1은 빨, 2는 파

	for (int i = 0; i < K; i++)
	{
		horse tmp_h;
		cin >> tmp_h.y >> tmp_h.x >> tmp_h.d;
		h_arr[i] = tmp_h;
		h_map[pair<int, int>(tmp_h.y, tmp_h.x)].push(i);
	}

	int turn = 0;
	map<pair<int, int>, stack<int>>::iterator m_it;
	while (turn++ <= 1000) // 종료조건
	{
		int ny, nx;
		int i = 0;
		while (i<K)
		{
			
			ny = h_arr[i].y + dy[h_arr[i].d];
			nx = h_arr[i].x + dx[h_arr[i].d];

			if (ny <= 0 || nx <= 0 || ny > N || nx > N || board[ny][nx] == 2)
			{
				if (h_arr[i].flag)
				{
					h_arr[i].flag = 0; //다시 0으로 돌려놔야함
					i++;//이 위치
					continue;
				}
				h_arr[i].flag = 1;//flag 1로
				h_arr[i].d = h_arr[i].d % 2 ? h_arr[i].d + 1 : h_arr[i].d - 1;//방향반대로
				continue;

			}
			else if (board[ny][nx] == 1)//빨간색
			{
				pair<int, int> origin = make_pair(h_arr[i].y, h_arr[i].x);
				pair<int, int> next = make_pair(ny, nx);

				while (h_map[origin].top() != i)
				{
					int group = h_map[origin].top();
					h_arr[group].y = ny;//위에 있는 말들도 모두 갱신해야함
					h_arr[group].x = nx;

					h_map[next].push(group);
					h_map[origin].pop();

				}
				h_map[next].push(h_map[origin].top());
				h_map[origin].pop();


			}
			else
			{
				pair<int, int> origin = make_pair(h_arr[i].y, h_arr[i].x);
				stack<int>tmp;
				pair<int, int> next = make_pair(ny, nx);

				while (h_map[origin].top() != i)
				{
					int group = h_map[origin].top();
					h_arr[group].y = ny;
					h_arr[group].x = nx;
					tmp.push(group);
					h_map[origin].pop();

				}
				tmp.push(h_map[origin].top());
				h_map[origin].pop();

				while (!tmp.empty()) {
					h_map[next].push(tmp.top());
					tmp.pop();
				}

			}
			//해당 말 위치 갱신
			h_arr[i].y = ny;
			h_arr[i].x = nx;
			
			//한칸에 말 4개 이상인지 체크(턴의 중간에 4개 이상 쌓이면 멈춰야함) 
			for (m_it = h_map.begin(); m_it != h_map.end(); m_it++)
			{
				if (m_it->second.size() >= 4)
				{
					cout << turn;
					return 0;
				}
			}

			if (h_arr[i].flag)
				h_arr[i].flag = 0;
			i++;
		}
	}
	cout << -1;
	return 0;
}