/*
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<deque>
#include<string>
#include<map>
using namespace std;
int main()//메모리:1996  시간:300ms
{
	int N,i=0,tmp=0;
	deque<int> deq;
	string st;
	map<string, int> m;
	m["push_front"] = 0;
	m["push_back"] = 1;
	m["pop_front"] = 2;
	m["pop_back"] = 3;
	m["size"] = 4;
	m["empty"] = 5;
	m["front"] = 6;
	m["back"] = 7;
	for (cin >> N; i < N; i++)
	{
		cin >> st;
		switch (m[st])
		{
		case 0:
			scanf("%d", &tmp);
			deq.push_front(tmp);
			break;
		case 1:
			scanf("%d", &tmp);
			deq.push_back(tmp);
			break;
		case 2:
			if (deq.empty())
				printf("-1\n");
			else
			{
				printf("%d\n", deq.front());
				deq.pop_front();
			}
			break;
			
		case 3:
			if (deq.empty())
				printf("-1\n");
			else
			{
				printf("%d\n", deq.back());
				deq.pop_back();
			}
			break;
		case 4:
			printf("%d\n", deq.size());
			break;
		case 5:
			printf("%d\n", deq.empty());
			break;
		case 6:
			if (deq.empty())
				printf("-1\n");
			else 
				printf("%d\n", deq.front());
			break;
		case 7:
			if (deq.empty())
				printf("-1\n");
			else
				printf("%d\n", deq.back());
			break;
		}
	}
	return 0;
}

//다른사람 코드 ->메모리:1228kb 시간:0ms....대단
/*
#include <stdio.h>
#include <queue>

int main()
{
	std::deque<int> Q;
	int n, t, s;
	char c, S[12];
	for (scanf("%d", &n); n--;)//이 방법을 참고해서 내 코드를 고쳐보았다. 기존 300ms -> 308ms(scanf말고 cin)로 시간이 증가함 *scanf로 하니 408ms로 더 증가했다.
	{
		scanf("%s", S);
		c = S[1];
		s = Q.size();
		if (c == 'r' || c == 'a') //문자열 앞부분만 잘라서 확인(r->front, a->back)
			printf("%d\n", s ? c % 2 ? Q.back() : Q.front() : -1); //디폴트값은 -1(이 부분은 처음 알게되었다!)
		
		else if (c == 'i' || c == 'm') //i->size, m->empty
			printf("%d\n", c % 3 ? s ? 0 : 1 : s);

		else if (c % 9)//pop
		{
			c = S[4];//f냐 b이냐
			printf("%d\n", s ? c % 3 ? Q.back() : Q.front() : -1);
			if (s) c % 3 ? Q.pop_back() : Q.pop_front();
		}
		
		else//push: 'u'의 아스키코드는 117이므로 9로 나누어 떨어짐
		{
			c = S[5];//f냐 b이냐
			scanf("%d", &t);
			c % 3 ? Q.push_back(t) : Q.push_front(t);
		}
	}

	return 0;
}
*/