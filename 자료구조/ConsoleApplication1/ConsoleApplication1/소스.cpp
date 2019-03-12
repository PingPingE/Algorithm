#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int N, arr[1000];
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	sort(arr, arr+N);
	cout << arr[N - 2] + arr[N - 1];

	return 0;
}