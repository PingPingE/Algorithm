#include <string>
#include <vector>
#include <map>
#include<queue>
using namespace std;
bool solution(int n, vector<vector<int>> path, vector<vector<int>> order) {
	map<int, vector<int>>path_m;	
	//A,B를 map으로 선언하니 시간초과가 났었다.
	vector<int>B(n, -1);
	vector<int>A(n, -1);
	vector<int> done(n, 0);
	queue<int> que;
	for (auto a : path)
	{
		path_m[a[0]].push_back(a[1]);
		path_m[a[1]].push_back(a[0]);
	}
	for (auto o : order)
	{
		if (o[1] == 0)
			return false;
		A[o[0]] = o[1];
		B[o[1]] = o[0];
	}
	
	done[0] = 1;
	if (A[0]>-1)
	{
		B[A[0]] = -1;
		A[0] = -1;
	}
	que.push(0);
	while (!que.empty())
	{
		int q = que.front();
		que.pop();
		for (auto i : path_m[q])
		{
			if (done[i])
				continue;
			if (A[i]>-1)//풀어줘야할(?) 노드(B)가 있는 경우
			{
				//일단 방문은 ok
				done[i] = 1;
				que.push(i);
				if (done[A[i]] == -1)//풀어준 노드가 waiting상태인 경우
				{
					done[A[i]] = 1;
					que.push(A[i]);
					A[i] = -1;
				}
				continue;
			}
			if (B[i]>-1)//먼저 방문해야할 노드(A)가 있는 경우
			{
				if (done[B[i]])//다행히 이미 방문한 경우
				{
					done[i] = 1;
					que.push(i);
					B[i] = -1;
				}
				else
					done[i] = -1;//waiting 상태(방문했지만 먼저 방문해야할 노드가 있는 상태)로 전환
				continue;
			}
			que.push(i);
			done[i] = 1;
		}
	}
	int result = 0;
	for (auto s : done)
		result += s;
	return (result == n ? true : false);
}
/*
정확성  테스트
테스트 1 〉	통과 (0.01ms, 3.79MB)
테스트 2 〉	통과 (0.01ms, 3.87MB)
테스트 3 〉	통과 (0.05ms, 3.95MB)
테스트 4 〉	통과 (0.52ms, 4.14MB)
테스트 5 〉	통과 (0.26ms, 3.91MB)
테스트 6 〉	통과 (0.47ms, 4.13MB)
테스트 7 〉	통과 (0.09ms, 3.79MB)
테스트 8 〉	통과 (0.22ms, 3.93MB)
테스트 9 〉	통과 (0.51ms, 4.06MB)
테스트 10 〉	통과 (0.01ms, 3.84MB)
테스트 11 〉	통과 (0.05ms, 3.79MB)
테스트 12 〉	통과 (0.01ms, 3.95MB)
테스트 13 〉	통과 (0.02ms, 3.78MB)
테스트 14 〉	통과 (0.02ms, 3.92MB)
테스트 15 〉	통과 (0.06ms, 3.88MB)
테스트 16 〉	통과 (0.05ms, 3.8MB)
테스트 17 〉	통과 (0.48ms, 4.11MB)
테스트 18 〉	통과 (0.54ms, 4.06MB)
테스트 19 〉	통과 (0.51ms, 4.07MB)
테스트 20 〉	통과 (0.06ms, 3.8MB)
테스트 21 〉	통과 (0.06ms, 3.81MB)
테스트 22 〉	통과 (0.83ms, 4.12MB)
테스트 23 〉	통과 (0.01ms, 3.92MB)
테스트 24 〉	통과 (0.02ms, 3.88MB)
테스트 25 〉	통과 (0.05ms, 3.96MB)
테스트 26 〉	통과 (0.62ms, 4.16MB)
테스트 27 〉	통과 (0.05ms, 3.84MB)
테스트 28 〉	통과 (0.54ms, 4.13MB)
테스트 29 〉	통과 (0.01ms, 3.8MB)
테스트 30 〉	통과 (0.01ms, 3.89MB)
테스트 31 〉	통과 (0.01ms, 3.88MB)
테스트 32 〉	통과 (0.01ms, 3.9MB)
테스트 33 〉	통과 (0.38ms, 4.07MB)
테스트 34 〉	통과 (0.38ms, 4.16MB)
효율성  테스트
테스트 1 〉	통과 (288.04ms, 61.1MB)
테스트 2 〉	통과 (350.73ms, 61MB)
테스트 3 〉	통과 (373.03ms, 61.8MB)
테스트 4 〉	통과 (315.23ms, 60.8MB)
테스트 5 〉	통과 (224.41ms, 61.3MB)
테스트 6 〉	통과 (255.86ms, 60.9MB)
테스트 7 〉	통과 (438.49ms, 61.7MB)
테스트 8 〉	통과 (395.53ms, 61MB)
테스트 9 〉	통과 (99.12ms, 61.7MB)
테스트 10 〉	통과 (126.70ms, 61.8MB)
*/