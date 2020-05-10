
/*
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 
바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.

별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다.
숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

메모리  제한: 4MB

*/
#include <iostream>
#include<algorithm>
using namespace std;
//1984kb	20ms
int main()
{
	int N;
	cin.tie(0);
	ios::sync_with_stdio(0);
	cin >> N;
	int num[3], cur = 0;
	int maxx[2][3] = { 0, };
	int minn[2][3] = { 0, };
	for (int i = 0; i < 3; i++)
	{
		cin >> num[i];
		maxx[cur][i] = num[i];
		minn[cur][i] = num[i];
	}
	cur ^= 1; //현재 행이 어딘지(0 or 1)
	for (int i = 1; i < N; i++)
	{
		for (int j = 0; j < 3; j++)
			cin >> num[j];
		maxx[cur][0] = max(maxx[cur ^ 1][0], maxx[cur^1][1]) + num[0];
		maxx[cur][1] = max(maxx[cur][0] - num[0], maxx[cur ^ 1][2]) + num[1];
		maxx[cur][2] = max(maxx[cur ^ 1][1], maxx[cur ^ 1][2]) + num[2];
		
		minn[cur][0] = min(minn[cur ^ 1][0], minn[cur ^ 1][1]) + num[0];
		minn[cur][1] = min(minn[cur][0] - num[0], minn[cur ^ 1][2]) + num[1];
		minn[cur][2] = min(minn[cur ^ 1][1], minn[cur ^ 1][2]) + num[2];

		cur ^= 1;
	}
	cout << max(max(maxx[cur ^ 1][0], maxx[cur^1][1]),maxx[cur^1][2]) << " " << min(min(minn[cur ^ 1][0], minn[cur ^ 1][1]),minn[cur^1][2]);

	return 0;
}