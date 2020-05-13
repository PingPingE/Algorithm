/*
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000)
다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
*/
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
#define INF 987654321
void dijkstra(vector<int> &res, vector<vector<int>> &V, int start);
int N, E;
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N >> E;
	vector<vector<int>> V(N + 1, vector<int>(N + 1, INF));
	int a, b, c;
	for (int i = 0; i < E; i++)
	{
		cin >> a >> b >> c;
		V[a][b] = min(c, V[a][b]);
		V[b][a] = min(c, V[b][a]);
	}
	int v1, v2;
	cin >> v1 >> v2;
	/*
	//플로이드 와샬 방식 : 4636kb 532ms
	for (int i = 1; i <= N; i++)
	{
	V[i][i] = 0;
	for (int j = 1; j <= N; j++)
	{
	for (int k = 1; k <= N; k++)
	{
	V[j][k] = min(V[j][k], V[j][i] + V[i][k]);
	}
	}
	}
	if (V[1][v1] >= INF || V[v1][v2] >= INF || V[v2][N] >= INF)
	cout << -1;
	else
	cout <<min(V[1][v1] + V[v1][v2]+V[v2][N], V[1][v2] + V[v2][v1] + V[v1][N]);
	*/
	vector<int> res1(N + 1, INF), res2(N + 1, INF), res3(N + 1, INF);
	dijkstra(res1, V, 1);
	dijkstra(res2, V, v1);
	dijkstra(res3, V, v2);

	if (res1[v1] == INF || res2[v2] == INF || res3[N] == INF)
		cout << -1;
	else
		cout << min(res1[v1] + res2[v2] + res3[N], res1[v2] + res3[v1] + res2[N]);

	return 0;
}
//다익스트라 방식 : 4636kb	48ms
void dijkstra(vector<int> &res, vector<vector<int>> &V, int start)
{
	priority_queue<pair<int, int>> que;
	res[start] = 0;
	que.push(pair<int, int>(0, start));
	while (!que.empty())
	{
		int cost = -que.top().first;
		int cur = que.top().second;
		que.pop();
		if (res[cur] < cost) continue;

		for (int i = 1; i <= N; i++)
		{
			int n_cost = cost + V[cur][i];
			if (res[i] > n_cost)
			{
				res[i] = n_cost;
				que.push(pair<int, int>(-res[i], i));
			}
		}
	}

}