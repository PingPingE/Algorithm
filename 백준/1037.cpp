/*
��� A�� N�� ��¥ ����� �Ƿ���, N�� A�� ����̰�, A�� 1�� N�� �ƴϾ�� �Ѵ�.
� �� N�� ��¥ ����� ��� �־��� ��, N�� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

�Է�)
ù° �ٿ� N�� ��¥ ����� ������ �־�����. �� ������ 50���� �۰ų� ���� �ڿ����̴�.
��° �ٿ��� N�� ��¥ ����� �־�����. 1,000,000���� �۰ų� ����, 2���� ũ�ų� ���� �ڿ����̰�, �ߺ����� �ʴ´�.
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int N, arr[51];
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	sort(arr, arr + N);
	cout << arr[0] * arr[N - 1];
	return 0;
}