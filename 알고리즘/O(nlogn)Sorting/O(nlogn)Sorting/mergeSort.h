#pragma once
#include <iostream>
void merge(int a[], int left, int mid, int right)
{
	int i = left;//ù��° ��� ������
	int j = mid + 1; //�ι��� ��� ������
	int k = left; //�߰� �迭 ������
	int *N = new int[right+1]; //�߰� �迭

	for (int h = left; h <= right; h++) //�߰��迭�� �����迭 ����
		N[h] = a[h];

	while (i <= mid && j <= right)
	{
		//�� �� ���� �� ���� ����
		if (N[i] < N[j])
		{
			a[k] = N[i];
			i++;
		}
		else
		{
			a[k] = N[j];
			j++;
		}
		k++;
	}
	//���ʿ� ���� �κ��� �ִٸ� ó��(������ �̹� �ڸ��ϰ� �����Ƿ�)
	if (i <= mid)
	{
		for (; i <= mid; i++)
			a[k++] = N[i];
	}
	delete(N);
}
void mergeSort(int a[], int left, int right)//�պ�����
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		//����
		mergeSort(a, left, mid);
		mergeSort(a, mid + 1, right);
		//�պ�
		merge(a, left, mid, right);
	}
	
}