/*
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

* 1 ≤ K ≤ N ≤ 5,000

*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<deque>//1984kb 68ms
using namespace std;
int main()
{
	int N, K;
	deque<int>dq;
	cin >> N >> K;
	for (int i = 1; i < N + 1; i++)
		dq.push_back(i);
	cout << "<";
	while (N > 1)
	{
		int tmp;
		for (int j = 0; j < K-1; j++)
		{
			tmp = dq.front();
			dq.push_back(tmp);
			dq.pop_front();
		}
		cout << dq.front()<<", ";
		dq.pop_front();
		N--;
	}
	cout << dq.front() << ">";

	return 0;
}
//다른사람 풀이
/*
#include<stdio.h>
int a[5001];
int main(){
    int n, m, t=0;
    scanf("%d%d", &n, &m);m--;
    for(int i=0; i<n; i++) a[i] = i+1;
    printf("<");
    for(int i=n; i>1; i--){
        (t+=m)%=(i);
        printf("%d, ", a[t]);
        for(int j=t; j<i; j++) a[j] = a[j+1];
    }
    printf("%d>", a[0]);
    return 0;
*/