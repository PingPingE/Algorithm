#include<iostream>
#include<deque>
using namespace std;
int count_zero();
int N, K;
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

		//이동 가능 여부 체크
		for (int i = N; i >= 0; i--)
		{
			if (!A[i].robot) continue;
			if (i == N)
				A[N].robot = 0;
			if (!A[i + 1].robot && A[i + 1].durability > 0)
			{
				A[i].robot = 0;
				A[i + 1].durability--;
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
		cout << A[i].durability << " " << A[i].robot << " => ";
		if (A[i].durability == 0)
			cnt++;
	}
	cout << endl;
	return cnt;
}