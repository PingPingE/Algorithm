/*

11650번 응용 문제)
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
* 1 ≤ N ≤ 100,000
*  -100,000 ≤ xi, yi ≤ 100,000
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
	vector<tuple<int, int>>yx;
	int N, i = 0;
	for (cin >> N; i < N; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		yx.push_back(tuple<int, int>(b, a));//이번엔 정렬 과정에서 y가 먼저 확인되어야 하므로 (y,x)형태
	}
	sort(yx.begin(), yx.end()); //y를 먼저 확인해서 sorting
	for (int k = 0; k < N; k++)
		printf("%d %d\n", get<1>(yx[k]), get<0>(yx[k])); //출력은 뒷 원소(x) 먼저 
	return 0;
}