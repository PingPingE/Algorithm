/*
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<map>
#include<queue>
#include<string>
using namespace std;
int main()
{
	int N, i = 0,res=0;
	queue<int> q;
	string st;
	map<string, int> m;
	m["push"] = 0;
	m["pop"] = 1;
	m["size"] = 2;
	m["empty"] = 3;
	m["front"] = 4;
	m["back"] = 5;
	for (cin >> N; i < N; i++)
	{
		cin >> st;
		//if로 문자열 비교 -> map+switch로 바꾸면: 404ms -> 288ms
		switch (m[st]) {
		case 0:
			scanf("%d", &res);
			q.push(res);
			break;
		case 1:
			if (q.empty())
				printf("-1\n");
			else
			{
				printf("%d\n",q.front());
				q.pop();
			}
			break;
		case 2:
			printf("%d\n",q.size());
			break;
		case 3: 
			printf("%d\n",q.empty());
			break;
		case 4:
			if (q.empty())
				printf("-1\n");
			else
				printf("%d\n",q.front());
			break;
		case 5:
			if (q.empty())
				printf("-1\n");
			else
				printf("%d\n",q.back());
			break;

		}
	
	}

	return  0;
}