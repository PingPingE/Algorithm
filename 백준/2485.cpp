/*
예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 된다.
또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 한다.

심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성하라.
단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있다.
*/

#include <iostream>
#include<algorithm>
#include<set>
#include<cmath>
using namespace std;
int UC(int, int);
int arr[100001];
int main() //2776kb	16ms
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	int N;
	cin >> N;
	set<int> d_set;
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr, arr + N);

	//차이 받기(중복된 값은 필요없으므로 set로 받음)
	for (int j = 0; j < N - 1; j++)
		d_set.insert(arr[j + 1] - arr[j]);

	set<int>::iterator it = d_set.begin();
	set<int>::iterator next = it;
	next++;
	int res = 100000001;
	while (next != d_set.end())
	{
		res = min(res, UC(*it++, *next++));
	}
	if (res == 100000001)
		cout << 0;
	else
		cout << (arr[N - 1] - arr[0]) / res + 1 - N;
	return 0;

}

int UC(int a, int b)
{
	if (a%b == 0)
		return b;
	return UC(b, a%b);
}