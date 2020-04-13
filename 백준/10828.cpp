/*
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stack>
#include<string>
#include<map>
using namespace std;
stack<int> st;
int N;
int main()
{
	int i = 0,tmp;
	map<string, int> m;
	m["pop"] = 0;
	m["size"] = 1;
	m["empty"] = 2;
	m["top"] = 3;

	string str;
	for (cin >> N; i < N; i++)
	{
		cin >> str;
		if (str == "push")
		{
			scanf("%d",&tmp);//여기만 cin -> scanf로 바꿔도 408ms -> 288ms
			st.push(tmp);
		}
		else
		{
			int res;
			switch(m[str])
			{
			case 0:
				if (st.empty())
					res = -1;
				else
				{
					res = st.top();
					st.pop();
				}
				break;
			case 1:
				res = st.size();
				break;
			case 2: 
				res=st.empty();
				break;
			case 3:
				if (st.empty())
					res = -1;
				else
					res = st.top();
				break;
			default: 
				break;
			}	
			printf("%d\n", res);
		}
	}

	return  0;
}