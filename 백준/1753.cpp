/*
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
*/
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
//9072kb 108ms
int INF = 10000000;
int V, E, K;
void min_cost(vector<vector<pair<int, int>>>&);
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> V >> E;
	cin >> K;
	int u, v, w;
	vector<vector<pair<int, int>>> Vec(V + 1);
	for (int i = 0; i < E; i++)
	{
		cin >> u >> v >> w;
		Vec[u].push_back(pair<int, int>(v, w));//간선 담기
	}
	min_cost(Vec);//최소 비용 구하기 + print
	return 0;
}
void min_cost(vector<vector<pair<int,int>>>& Vec)
{
	int cur_min = INF;
	vector<int> result(V+1, INF);//각 정점까지의 최단거리 저장
	priority_queue<pair<int, int>> pq;
	pq.push(pair<int,int>(0, K));//비용, 현재 노드 순
	result[K] = 0;//자기자신은 0
	while (!pq.empty())
	{
		int cost = -pq.top().first;//음수값이 들어가므로 뺄때 - 필수
		int cur = pq.top().second;
		pq.pop();

		if (result[cur] < cost)
			continue;

		for (int i = 0; i < Vec[cur].size(); i++)
		{
			int n_cur = Vec[cur][i].first;
			int n_cost = Vec[cur][i].second + cost;
			if (result[n_cur] > n_cost)
			{
				result[n_cur] = n_cost;
				pq.push(pair<int, int>(-n_cost, n_cur));//들어갈때 -cost(비용이 적은게 우선이어야하므로) 
			}
		}
	}

	for (int i = 1; i<=V; i++)
		(result[i] == INF ? cout << "INF"<<"\n" : cout << result[i]<<"\n");
	
	
}