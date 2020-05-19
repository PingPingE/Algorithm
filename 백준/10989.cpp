/*
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

시간제한: 3초, 메모리제한: 8MB
*/
#include<iostream>
#include<map>
using namespace std;
//	2512kb	2908ms
int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(0);
	int N,tmp; 
	map<int, int> m;
	cin >> N;
	while (N--)
	{
		cin >> tmp;
		m[tmp] ++;
	}
	for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
	{
		for (int i = 0; i < it->second; i++)
			cout << it->first << "\n";
	}
	return 0;
}