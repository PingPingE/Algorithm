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
	
	//차이 받기
	for (int j = 0; j < N - 1; j++)
		d_set.insert(arr[j + 1] - arr[j]);

	set<int>::iterator it= d_set.begin();
	set<int>::iterator next = it;
	next++;
	int res = 100000001;
	while (next!=d_set.end())
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