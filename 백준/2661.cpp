/*
����)
���� 1, 2, 3���θ� �̷������ ������ �ִ�.������ ������ ������ �� ���� �κ� ������ ������ ���� ������, �� ������ ���� �����̶�� �θ���.�׷��� ���� ������ ���� �����̴�.

������ ���� ������ ���̴�.

33
32121323
123123213
������ ���� ������ ���̴�.

2
32
32123
1232123

���̰� N�� ���� �������� N�ڸ��� ������ ���� ���� ���� ���� ���� ��Ÿ���� ������ ���ϴ� ���α׷��� �ۼ��϶�.
���� ���, 1213121�� 2123212�� ��� ���� ���������� �� �߿��� ���� ���� ��Ÿ���� ������ 1213121�̴�.

�Է�)
�Է��� ���� N�ϳ��� �̷������.N�� 1 �̻� 80 �����̴�.

���)
ù ��° �ٿ� 1, 2, 3���θ� �̷���� �ִ� ���̰� N�� ���� ������ �߿��� ���� ���� ���� ��Ÿ���� ������ ����Ѵ�.������ �̷�� 1, 2, 3�� ���̿��� ��ĭ�� ���� �ʴ´�.
*/

#include<iostream>
#include<string>
using namespace std;
int N;
void isTrue(string);
bool stop = 0;
//1984kb	0ms
int main()
{
	cin >> N;
	isTrue("1");
	return 0;
}

void isTrue(string target)
{
	if (stop) return;
	int s = target.length() - 1;
	bool stat = 1;
	for (int m = 1; m <= target.length() / 2; m++)
	{
		string sub1 = target.substr(s - m, m);
		string sub2 = target.substr(s, m);
		if (sub1.compare(sub2) == 0)
		{
			stat = 0;
			break;
		}
		s--;
	}
	if (stat)
	{
		if (target.length() == N)
		{
			cout << target;
			stop = 1;
			return;
		}
		isTrue(target + "1");
		isTrue(target + "2");
		isTrue(target + "3");
	}
}

