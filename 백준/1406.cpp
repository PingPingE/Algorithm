/*
한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
이 편집기가 지원하는 명령어는 다음과 같다.

1. L: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
2. D: 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
3. B: 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
4. P $: $라는 문자를 커서 왼쪽에 추가함

초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

* 1<= N(문자열 길이)<=100,000
* 1 <= M(명령어 개수) <= 500,000
*시간 제한: 0.3 초
*메모리 제한: 512mb

*/
#include<iostream>
#include<deque>
#include<string>
using namespace std;
int main()//2768kb	36ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int M;
	char ch;
	deque<char> left;
	deque<char> right;
	string s;
	cin >> s;
	for (int i = 0; i < s.size(); i++)
		left.push_back(s[i]);
	cin >> M;
	while (M--)
	{
		cin >> ch;
		if (ch == 'P')
		{
			cin >> ch;
			left.push_back(ch);
		}
		else if (ch == 'L')
		{
			//맨앞이면 왼쪽으로 이동안함
			if (!left.empty())
			{
				right.push_front(left.back());
				left.pop_back();
			}
		}
		else if (ch == 'D')
		{
			//맨 뒤면 오른쪽으로 이동안함
			if (!right.empty())
			{
				left.push_back(right.front());
				right.pop_front();
			}
		}
		else//B
		{
			//맨앞이면 삭제안함
			if (!left.empty())
				left.pop_back();
		}
	}
	while (!left.empty())
	{
		cout << left.front();
		left.pop_front();
	}
	while (!right.empty())
	{
		cout << right.front();
		right.pop_front();
	}

	return 0;
}
/*
#include<iostream>
#include<string>
#include<list>
using namespace std;
int main() //20984kb	68ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int M;
	string st;
	list<char> ch_list;
	cin >> st >> M;
	for (int i = 0; i < st.size(); i++)
		ch_list.push_back(st[i]);
	list<char>::iterator it =ch_list.end();
	while (M--)
	{
		char ch;
		cin >> ch;
		if (ch == 'P')
		{
			cin >> ch;
			it = ch_list.insert(it, ch);
			it++;

		}
		else if (ch == 'B')
		{
			//삭제
			if (it != ch_list.begin())
				it = ch_list.erase(--it);
		}
		else if (ch == 'L')
		{
			//index --
			if (it != ch_list.begin())
				it--;
		}
		else
		{
			//index ++
			if (it != ch_list.end())
				it++;
		}
	}
	for (list<char>::iterator iter = ch_list.begin(); iter != ch_list.end(); iter++)
		cout << *iter;
	return 0;
}

*/
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

//sol2) 두개의 덱으로 구현 : 4188kb   96ms
/*
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

*/
