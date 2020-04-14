/*

2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
* 1 ≤ N ≤ 100,000
* -100,000 ≤ xi, yi ≤ 100,000
*위치가 같은 두 점은 없다.

*/

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include <vector>
#include<tuple>
#include<algorithm>
using namespace std;
int main()
{
	vector<tuple<int, int>>xy;
	int N, i=0;
	for (cin >> N; i < N; i++)
	{
		int a, b;
		scanf("%d%d",&a, &b);//x,y를 차례로 받아서
		xy.push_back(tuple<int,int>(a,b));//tuple형태로 vector에 저장
	}
	sort(xy.begin(), xy.end()); //오름차순 정렬(튜플의 앞원소를 먼저 확인)
	for (int k = 0; k < N; k++)
		printf("%d %d\n", get<0>(xy[k]), get<1>(xy[k]));
	return 0;
}