/*)
문제)
길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다. 
벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져 있으며, 각 칸에는 아래 그림과 같이 1부터 2N까지의 번호가 매겨져 있다.

벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동한다. 
i번 칸의 내구도는 Ai이다. 위의 그림에서 1번 칸이 있는 위치를 "올라가는 위치", N번 칸이 있는 위치를 "내려가는 위치"라고 한다.

컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려고 한다. 로봇은 올라가는 위치에만 땅에서 올라가고, 내려가는 위치에서만 땅으로 내려갈 수 있다. 
내려가는 위치에 로봇이 있는 경우 로봇은 반드시 땅으로 내려가야 한다. 로봇이 어떤 칸에 올라가거나 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다. 
내구도가 0인 칸에는 로봇이 올라갈 수 없다.

로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다.

컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다. 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.

벨트가 한 칸 회전한다.
가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.

입력)
첫째 줄에 N, K가 주어진다. 둘째 줄에는 A1, A2, ..., A2N이 주어진다.

출력)
몇 번째 단계가 진행 중일때 종료되었는지 출력한다.
*/
#include<iostream>
#include<deque>
using namespace std;
int count_zero();
int N, K;
//1984kb	128ms
struct belt {
	int durability = 0;
	bool robot = 0;
}; 
deque<belt> A;
int main()
{
	cin >> N >> K;
	for (int i = 0; i < 2 * N; i++)
	{
		belt tmp;
		scanf_s("%d", &tmp.durability);
		A.push_back(tmp);
	}
	int time = 0;
	while (count_zero()<K)
	{
		++time;
		
		//belt 회전
		belt tmp = A.back();
		A.pop_back();
		A.push_front(tmp);

		A[N - 1].robot = 0;
		//이동 가능 여부 체크
		for (int i = N-2; i >= 0; i--)
		{
			if (!A[i].robot) continue;
			if (!A[i + 1].robot && A[i + 1].durability > 0)
			{
				A[i].robot = 0;
				A[i + 1].durability--;
				if (i + 1 == N - 1)
					continue;
				A[i + 1].robot = 1;
			}
		}

		if (!A[0].robot && A[0].durability>0)
		{
			A[0].robot = 1;
			A[0].durability--;
		}
	}
	cout << time;
	return 0;
}
int count_zero()
{
	int cnt = 0;
	for (int i = 0; i < 2 * N; i++)
	{
		if (A[i].durability == 0)
			cnt++;
	}
	return cnt;
}