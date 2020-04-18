/*

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
이를 계산하는 프로그램을 작성하라.

*1 ≤ n ≤ 100,000
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

*/

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stack>
#include<queue>
using namespace std;
int main() // 2872kb  24ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int N, i = 1, j = 0, res_i = 0, target_i = 0;
	cin >> N;
	stack<int>int_stack;
	char result[500000];
	int target[100001];
	for (; j < N; j++)
		cin >> target[j];

	for (; i <= N; i++)
	{
		result[res_i++] = '+';
		int_stack.push(i);
		while (!int_stack.empty() && int_stack.top() == target[target_i])
		{
			int_stack.pop();
			result[res_i++] = '-';
			if (target_i < N - 1)
				target_i++;
		}
	}
	if (!int_stack.empty())
		cout << "NO";
	else
	{
		for (int k = 0; k < res_i; k++)
			cout << result[k] << "\n";
	}
	return 0;
}
/*
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
}*/