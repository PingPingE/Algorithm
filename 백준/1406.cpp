/*
이 편집기가 지원하는 명령어는 다음과 같다.

1. L: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
2. D: 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
3. B: 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
4. P $: $라는 문자를 커서 왼쪽에 추가함

초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
*/

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<list>
using namespace std;
/*
list<char>li;
list<char>::iterator it;
void solve(int);
int main() //sol1) stl의 list 활용 : 20844kb 136ms
{
	int i = 0,j=0,N;
	string st;
	cin >> st;
	for (; i < st.size(); i++)
	{
		li.push_back(st[i]);
	}
	cin >> N;
	it = li.end();//처음엔 마지막 노드 다음을 가리킴
	solve(N);
	for (list<char>::iterator it = li.begin(); it != li.end(); it++)
		printf("%c", *it);
	return 0;
}
void solve(int N)
{
	while (N > 0)
	{
		char temp;
		cin >> temp;
		if (temp == 'P')
		{
			cin >> temp;
			it = li.insert(it, temp);
			it++;
		}
		else if (temp == 'B')
		{
			if (it != li.begin())
				it = li.erase(--it);

		}
		else if (temp == 'L')
		{
			if (it != li.begin())
				it--;
		}
		else
		{
			if (it != li.end())
				it++;
		}
		N--;
	}
	
}*/

//sol2) 두개의 덱큐로 구현 : 4188kb   96ms
#include<deque>
int main()
{
	deque<char> q1;
	deque<char> q2;
	string st;
	cin >> st;
	int i = 0,N;
	for (; i < st.size(); i++)
		q1.push_back(st[i]);
	cin >> N;
	while (N--)
	{
		char ch;
		cin >> ch;
		if (ch == 'P')
		{
			cin >> ch;
			q1.push_back(ch);
		}
		else if (ch == 'B')
		{
			if (!q1.empty())
				q1.pop_back();
		}
		else if (ch == 'L')
		{
			if (!q1.empty())
			{
				q2.push_front(q1.back());
				q1.pop_back();
			}
		}
		else
		{
			if (!q2.empty())
			{
				q1.push_back(q2.front());
				q2.pop_front();
			}
		}
	}
	//출력
	string res;
	while (!q1.empty())
	{
		res += q1.front();
		q1.pop_front();
	}
	while (!q2.empty())
	{
		res += q2.front();
		q2.pop_front();
	}
	cout << res;
	return 0;
}


//다른 사람 풀이 -> 두개의 stack으로 구현: 4264kb	24ms
/*
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;
#define endl '\n'

int main()
{
	// Set up : I/O
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	// Set up : Input
	string S; cin >> S;

	// Process
	stack<char> left; //스택 두개로 구현
	stack<char> right;
	for (auto &letter : S) { left.push(letter); }

	int M; cin >> M;

	while (M--) {
		char cmd; cin >> cmd;

		if (cmd == 'L') {
			if (not(left.empty())) {
				right.push(left.top());
				left.pop();
			}
		}
		else if (cmd == 'D') {
			if (not(right.empty())) {
				left.push(right.top());
				right.pop();
			}
		}
		else if (cmd == 'B') {
			if (not(left.empty())) {
				left.pop();
			}
		}
		else if (cmd == 'P') {
			char ch; cin >> ch;
			left.push(ch);
		}
	}

	// Control : Output
	string str_left;
	while (not(left.empty())) {
		str_left.push_back(left.top());
		left.pop();
	}
	reverse(str_left.begin(), str_left.end()); //주의: 왼쪽은 꺼낸다음 reverse해줘야함 (오른쪽은 그대로)
	string str_right;
	while (not(right.empty())) {
		str_right.push_back(right.top());
		right.pop();
	}
	cout << str_left + str_right << endl;
}*/