/*
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<algorithm>
using namespace std;
int arr[500001];
int N;
bool check(int);
//sol1)메모리:3936kb 시간:308ms	
int main()
{
	int M, mm, i = 0, j = 0;//for문 안에 int i=0선언해서 하는 것보다 먼저 i=0선언해주고 for문 돌리는게 더 빠름(312ms->308ms)
	cin >> N;
	for (; i < N; i++)
		scanf("%d", &arr[i]);
	sort(arr, arr + N);
	cin >> M;
	for (; j < M; j++)//위에 쓰던i를 i=0으로 초기화해주고 이 for문에 또 i로 돌리니 엄청 느려짐(308ms ->  576ms) -> 그냥 변수 하나 더 미리 선언해서 쓰자
	{
		scanf("%d", &mm);
		printf("%d ", check(mm));
	}
	return 0;
}
bool check(int num)
{
	int l = 0, r = N - 1, m = 0;
	while (l <= r)
	{
		m = (l + r) / 2;
		if (arr[m] == num)
			return 1;
		else if (arr[m] < num)
			l = m + 1;
		else
			r = m - 1;
	}
	return 0;
}
//sol2) 메모리:3936kb 시간:288ms	
/*
#include<iostream>
#include<algorithm>
using namespace std;
int arr[500001];
int main()
{
int N, M, tmp, i = 0, j = 0;
cin >> N;
for (; i < N; i++)
scanf("%d", &arr[i]);
sort(arr, arr + N);
cin >> M;
for (; j < M; j++)
{
scanf("%d", &tmp);
if (arr[lower_bound(arr, arr + N, tmp) - arr] != tmp)//직접 이분검색 구현 대신 lower_bound 내장함수 활용
printf("0 ");
else
printf("1 ");
}
return 0;
}

*/


/*
//다른사람 코드(이분검색X)
//메모리: 21516kb 시간: 320ms
#include <bits/stdc++.h> //이건 대회에서 빨리 풀기 위해 많이 쓴다고함(모든 헤더 미리 컴파일)
using namespace std;
int n, m;
bool c[20000001]; //값 범위가 -1천만~1천만이라서 2천만으로 할당한듯
int main() {
cin >> n;
while (n--) {
scanf("%d", &m);
c[m + 10000000] = true; //음수값을 고려해서 받은 값(m)에 +1천만 한듯
}
cin >> n;
while (n--) {
scanf("%d", &m);
printf("%d ", c[m + 10000000] ? 1 : 0);//조건연산자 활용
}
}
*/