/*

N개의 정수가 주어진다. 
이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 
같은 정수는 한 번만 출력한다.

* 1 ≤ N ≤ 100,000
* 수는 절댓값이 1000보다 작거나 같은 정수

*/

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include <set>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int N, i=0,tmp;
	//sol1) set를 활용해 중복을 제거 후 정렬한 방법: 1984kb, 20ms
	set<int> s;
	for (cin >> N; i < N; i++)
	{
		scanf("%d", &tmp);
		s.insert(tmp);
	}
	for (std::set<int>::iterator it = s.begin(); it != s.end(); ++it)
	{
		printf("%d ", *it);
	}
	//sol2) 정렬 후 unique + erase로 중복 제거: 2764kb, 20ms
	/*vector<int> v;
	int N,i = 0,t;
	for (cin >> N; i < N; i++)
	{
		scanf("%d", &t);
		v.push_back(t);
	}
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());
	for (auto j : v)
		printf("%d ", j);*/
	return 0;
}