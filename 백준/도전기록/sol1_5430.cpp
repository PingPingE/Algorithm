#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
using namespace std;
int main()//시간초과
{
	int T;
	cin >> T;
	while (T--)
	{
		queue<int>arr;
		char p[100002];
		int n;
		bool stat =1;//에러 여부
		scanf("%s", p);
		cin >> n;
		string s;
		cin >> s;
		s.erase(s.begin());
		s.erase(s.end()-1);
		int cnt = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == ',')
			{
				int tmp = 0; 
				for (int j = i - cnt; j < i; j++)
				{
					tmp += (s[j] - '0')*pow(10, cnt-1);
					cnt--;
				}
				arr.push(tmp);
				continue;
			}
				
			cnt++;
		}
		if (cnt > 0)
		{
			int tmp = 0;
			for (int j = s.size()-cnt; j < s.size(); j++)
			{
				tmp += (s[j] - '0')*pow(10, cnt - 1);
				cnt--;
			}
			arr.push(tmp);
		}
		int it = 0;
		while(p[it]=='R'|| p[it]=='D' )
		{
			if (p[it] == 'R')
			{
				stack<int>st;
				while (!arr.empty())
				{
					st.push(arr.front());
					arr.pop();
				}
				while (!st.empty())
				{
					arr.push(st.top());
					st.pop();
				}
				stat = 0;
			}
			else
			{
				if (arr.empty())
				{
					stat = 1;
					break;
				}
				arr.pop();
			}
			it++;
		}
		if (stat == 1)
		{
			printf("error\n");
			continue;
		}
			
		printf("[");
		while (!arr.empty())
		{
			printf("%d",arr.front());
			arr.pop();
			if (arr.empty())
				printf("]\n");
			else
				printf(",");
		}
	}
	return 0;
}