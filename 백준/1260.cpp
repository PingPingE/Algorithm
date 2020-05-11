/*
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
*/
#include<iostream>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<vector>
#include<algorithm>
//2388kb	8ms
using namespace std;
bool cmp(int a, int b)
{
	return a > b;
}
int main()
{
	map<int, vector<int>>m;
	int N, M, V;
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		//양방향
		m[a].push_back(b);
		m[b].push_back(a);
	}
	bool stat = 1;
	if (m.find(V) == m.end())
	{
		cout << V << "\n" << V;
		return 0;
	}
	for (int i = 0; i < 2; i++)
	{
		set<int> done;
		queue<int> result;
		if(stat)//dfs
		{
			int target;
			stack<int> stack;
			stack.push(V);
			while (!stack.empty())
			{
				target = stack.top();
				stack.pop();
				if (done.find(target) != done.end())//stack은 확인 필수
					continue;
				result.push(target);
				done.insert(target);
				if (m.find(target) != m.end())
				{
					sort(m[target].begin(), m[target].end(), cmp);
					for (vector<int>::iterator it = m[target].begin(); it != m[target].end(); it++)
					{
						if (done.find(*it) == done.end())
							stack.push(*it);
					}
				}
			}
		
		}
		else//bfs
		{
			int target;
			done.insert(V);
			queue<int> que;
			que.push(V);
			while (!que.empty())
			{
				target = que.front();
				que.pop();
				result.push(target);
				if (m.find(target) != m.end())
				{
					sort(m[target].begin(), m[target].end());
					for (vector<int>::iterator it = m[target].begin(); it != m[target].end(); it++)
					{
						if (done.find(*it) == done.end())
						{
							done.insert(*it);
							que.push(*it);
						}
					}
				}
			}
		}
		
		while (!result.empty())
		{
			cout << result.front();
			result.pop();
			if (!result.empty())
				cout << " ";
		}
		if(stat)
			cout << endl;
		stat ^= 1;
	}
	

	return 0;
}