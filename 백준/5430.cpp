/*
두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<string>
#include<time.h>
using namespace std;
int main()//2772kb	68ms
{
	//아래 두 줄 없으면 2500kb	184ms
	cin.tie(0);
	ios_base::sync_with_stdio(0); 
	int T;
	cin >> T;
	while (T--)
	{
		string p, buf;
		char tmp;//찌꺼기 담을 곳([,)
		int arr[100001], n, i = 0, j = 0;
		cin >> p >> n;
		for (; i < n; i++)
			cin >> tmp >> arr[i];
		cin >> buf;//찌꺼기
		bool pp = 0;
		int front = 0;//원상태에서 D몇개
		int end = 0;//뒤집은상태에서 D몇개
		while (j<p.size())
		{
			if (p[j] == 'R')
				pp = !pp; //false -> true, true->false
		
			else
			{
				if (end + front == n)//arr.size()가 0이면
				{
					end = -1;
					break;
				}

				if (pp == 1)//뒤집힌 상태면
				{
					end++; //뒤에서 부터
				}
				else
					front++;
			
			}
			j++;
		}
		if (end != -1)
		{
			cout << "[";

			if (pp)
			{
				int k = n-end-1;
				for(;k>=front; k--)
				{ 
					cout << arr[k];
					if ((k - 1) >= front)
						cout << ',';
				}
			}
			else
			{
				int k = front;
				for (; k < n - end; k++)
				{
					cout << arr[k];
					if ((k + 1) < n - end)
						cout << ',';
				}
				
			}
			cout << "]\n";	
		}
		else
		{
			cout << "error\n";
		}
		
	}
	return 0;
}

//다른 사람 코드
/*
//60ms로 통과한 코드
#include <iostream>
#include <string>
using namespace std;

int T, N, i, f, e, rv, arr[100000];
string str, buf;
char tmp;

int main()
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	cin >> T;
	while (T--)
	{
		cin >> str >> N;
		for (i = 0; i<N; i++)
			cin >> tmp >> arr[i];
		cin >> buf;

		rv = f = 0;
		e = N;
		for (char ch : str)
			if (ch == 'R') rv ^= 1;
			else if (rv) e--;
			else f++;

			if (f>e)
				cout << "error\n";
			else if (f == e) cout << "[]\n";
			else
			{
				cout << "[";
				if (rv)
				{

					for (i = e - 1; i > f; i--)
						cout << arr[i] << ',';
					cout << arr[i];
				}
				else
				{
					for (i = f; i < e - 1; i++)
						cout << arr[i] << ',';
					cout << arr[i];
				}
				cout << "]\n";
			}
	}
}*/