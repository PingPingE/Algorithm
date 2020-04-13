#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<algorithm>
using namespace std;
int arr[1000001];
int main()
{
	int N;
	cin >> N;
	int tmp = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		arr[i] = tmp;
	}
	sort(arr, arr + N);
	for (int i = 0; i < N; i++)
		printf("%d\n", arr[i]);

	return 0;
}