/*
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
*/

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<queue>
#include<algorithm>
#include<tuple>
using namespace std;
int sol(queue<tuple<int,int>>*, vector<int>*, int);
int main() // 1984kb 0ms
{
	int T, N, M;
	cin >> T;
	while (T > 0)
	{
		cin >> N>> M;
		queue<tuple<int, int>> q;
		vector<int> maxx;
		for (int i = 0; i < N; i++)
		{
			int t;
			scanf("%d", &t);
			if (i == M)
				q.push(make_tuple(t, 1));//1로 타겟 표시
			else
				q.push(make_tuple(t, 0));
			maxx.push_back(t);
		}
		sort(maxx.begin(), maxx.end());
		cout << sol(&q,&maxx,0)<<endl;
		T--;
	}

	return 0;
}
int sol(queue<tuple<int, int>> *q, vector<int> *maxx, int cnt)
{
	while (!maxx->empty())
	{
		int temp = maxx->back();//중요도 큰거부터 
		maxx->pop_back();
		while (!q->empty())
		{
			tuple<int, int> que = q->front();
			q->pop();
			if (get<0>(que) == temp)
			{
				cnt++;
				cout << "pop: "<<get<0>(que) << endl;
				if (get<1>(que) == 1)//타겟이면
					return cnt;
				break;
			}
			else
				q->push(que);

		}
	}
	return cnt;
}