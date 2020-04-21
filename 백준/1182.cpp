/*
N���� ������ �̷���� ������ ���� ��,
ũ�Ⱑ ����� �κм��� �� �� ������ ���Ҹ� �� ���� ���� S�� �Ǵ� ����� ���� ���϶�
1<=N<=20
abs(S)<=1000000
*/
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
int cnt = 0;
int cnt_ = 0;
int arr[21];
int N, S;
void dfs(int, bool*, int);//�������� index(ù������ -1��), sum�� �����Ѱ� üũ, ��������� sum
int sol2(int, int, bool);
int main()
{
	scanf("%d%d", &N, &S);
	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	bool done[21];
	for (auto& i : done)
		i = false;
	dfs(-1, done, 0); //S�� 0�ΰ��, ���� �ʰ� �ٷ� cnt++�� �ع����Ƿ� ù ������ ǥ���ϱ� ���� cur_i=-1�� �ʱ�ȭ
	cnt = sol2(0, 0, 0);
	cout << cnt << ' ' << cnt_;
	return 0;
}
//sol1) 1984kb, 8ms
void dfs(int cur_i, bool *done, int cur_sum)
{

	if (cur_i != -1 && cur_sum == S)//���⼭ return�� �ع��� ���� ��������. ���信 �����ص� �� �����Ѵ�.
	{
		/*for(int i =0; i<N; i++)
		cout << done[i] << ' ';
		cout << endl;
		*/
		cnt_++;
	}
	if (cur_i == -1)
		cur_i = 0;
	else if (cur_i >= N)
		return;

	for (int i = cur_i; i<N; i++)
	{
		if (!done[i])
		{
			done[i] = true;
			dfs(i, done, cur_sum + arr[i]);
			done[i] = false;
		}
	}
}
//sol2) -> 1984kb, 4ms(�ð� ������ �پ��)
int sol2(int cur_i, int cur_sum, bool done) //���� index, ����sum, �ϳ��� ���տ� �����ߴ���
{
	if (cur_i == N) // �߰��� sum�� S��� return�ϸ� X ������ �� ���� return�ؾ���(�ڿ��� 0�� ���� �ְ�, -1, 1�̷����ϼ�����
		if (cur_sum == S && done)
			return 1;
		else
			return 0;
	return sol2(cur_i + 1, cur_sum, done + 0) + sol2(cur_i + 1, cur_sum + arr[cur_i], 1); //�κ����տ� ������, ����
}