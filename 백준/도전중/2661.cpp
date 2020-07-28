#include<iostream>
#include<queue>
#include<string>
using namespace std;
bool isTrue;
int main()
{
	string st;
	int N;
	cin >> N;
	queue<string> que;
	if (N == 1)
	{
		cout << 1;
		return 0;
	}
	que.push("12");
	while (!que.empty())
	{
		string q_st = que.front();
		que.pop();
		if (q_st.size() == N)
		{
			cout << q_st;
			break;
		}
		char c_list[3] = { '1','2','3' };
		for (int i = 0; i < 3; i++)
		{
			isTrue = 1;
			string next_st = q_st+c_list[i];
			int s = next_st.size() - 1;
			for (int m = 1; m<=(int)next_st.size() / 2; m++)
			{
				string sub1 = next_st.substr(s - m, m);
				string sub2 = next_st.substr(s, m);
				if (sub1.compare(sub2) == 0)
				{
					isTrue = 0;
					break;
				}
				s--;
			}
			if (isTrue)
				que.push(next_st);
		}
		
		
	}
	return 0;
}
