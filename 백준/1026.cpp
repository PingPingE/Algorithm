/*
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0]*B[0] + ... + A[N-1]*B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

*N <=50
*0<= A,B <=100
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include <vector>
#include<algorithm>
using namespace std;
int A[51], B[51], N;
bool cmp(int, int);
int main()
{
	int result = 0;
	int j = 0, i = 0;
	cin >> N;
	for (; i < N; i++)
		scanf("%d", &A[i]);
	for (; j < N; j++)
		scanf("%d", &B[j]);
	sort(A, A + N,cmp);//A는 내림차순
	sort(B, B + N);//B는 오름차순
	for (int k = 0; k < N; k++)
		result += A[k] * B[k];//큰 수와 작은 수를 곱하면 최소가 되므로

	printf("%d",result);
	return 0;
}
bool cmp(int a, int b)//내림차순 정렬을 위해
{
	return a > b;
}
