#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int sol(int);
int main()//1984kb	0ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int T,N;
	cin >> T;
	while (T--)
	{
		cin >> N;
		cout << sol(N) << "\n";
	}
	return 0; 
}
int sol(int target)
{
	if (target == 0)
		return 1;
	if (target<0)
		return 0;
	return sol(target - 1) + sol(target - 2) + sol(target - 3);
}