#pragma once
#include <iostream>
using namespace std;
inline int partition(int a[], int left, int right)
{
	int L = left; //pivot ���� ������
	int R = right;//�� �� ������
	int pivot =left; // �� ó�� ���� pivot���� ����
	int temp = 0; //swap�� �� �ʿ��� ����

	while (L <= R)//L��R�� �������� ������
	{
		while (L <= right && a[L] < a[pivot])//���� �߿�! L�� right(������)�� ���ų� ������ ����+pivot���� ���� ��
			L++; //�տ��� �ڷ� �̵��ϹǷ�
		while (R > left && a[R] >= a[pivot]) // R�� left(ó������)���� Ŭ�� ����+pivot���� ū ��
			R--;//�ڿ��� ������ �̵��ϹǷ�

		if (L < R) //���� �ȳ�������
		{
			//R�� L swap
			temp = a[R];
			a[R] = a[L];
			a[L] = temp;
		}
	}
	//L�� R�� ���������� R�� pivot�ڸ� ���� swap
	temp = a[R];
	a[R] = a[pivot];
	a[pivot] = temp;
	return R;
	
}

void Quick(int a[], int left, int right)
{
	if (left < right)
	{
		int p = partition(a, left, right);
		//�����ؼ� ���
		Quick(a, left, p - 1);
		Quick(a, p + 1, right);
	}
	
}
