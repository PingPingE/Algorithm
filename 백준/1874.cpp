#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stack>
#include<queue>
using namespace std;
int main() //2380kb 32ms : res를 list로 했을 경우,  8188kb  40ms: res를 queue로 했을 경우
{
	stack<int>s;
	queue<int>target;
	queue<char> res;
	int N, tmp, i = 0;
	cin >> N;
	for (; i < N; i++)
	{
		scanf("%d", &tmp);
		target.push(tmp);
	}
	int t = target.front();
	target.pop();
	int j = 1;
	while(j<=N)//첫번째
	{
		res.push('+');
		s.push(j);
		
		while (!s.empty() && s.top() == t)
		{
			s.pop();
			res.push('-');
			if (target.empty())
				break;
			t = target.front();
			target.pop();
		}
		j++;
	}
	while (!s.empty())
	{
		if (t != s.top())
		{
			cout << "NO";
			return 0;
		}
		res.push('-');
		s.pop();
		if (target.empty())
			break;
		t = target.front(); //새로운 타겟
		target.pop();
	}
	while (!res.empty())
	{
		printf("%c\n", res.front());
		res.pop();
	}
	return 0;
}