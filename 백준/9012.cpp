/*
“(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

*하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
 
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<stack>
#include<string>
using namespace std;
bool sol(string,int);
int main()//1988kb	4ms
{
	int N,i=0;
	string st;
	cin >> N;
	for (; i < N; i++)
	{
		cin >> st;
		if (sol(st, st.size()))
			cout << "YES" << endl;
		else
			cout<< "NO" << endl;
	}
	return 0;
}

bool sol(string s , int size)
{
	stack<int> s1;
	for(int j=0; j<size; j++)
	{
		if (s[j] == '(')
			s1.push(1);
		else
		{
			if (!s1.empty())
				s1.pop();
			else
				return 0;
		}

	}
	if (!s1.empty())
		return 0;
	return 1;
}
