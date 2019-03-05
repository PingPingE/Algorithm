#pragma once
#include <iostream>
void merge(int a[], int left, int mid, int right)
{
	int i = left;//첫번째 블록 시작점
	int j = mid + 1; //두번재 블록 시작점
	int k = left; //추가 배열 시작점
	int *N = new int[right+1]; //추가 배열

	for (int h = left; h <= right; h++) //추가배열에 기존배열 복사
		N[h] = a[h];

	while (i <= mid && j <= right)
	{
		//둘 중 작은 값 먼저 대입
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
	//앞쪽에 남은 부분이 있다면 처리(뒷쪽은 이미 자리하고 있으므로)
	if (i <= mid)
	{
		for (; i <= mid; i++)
			a[k++] = N[i];
	}
	delete(N);
}
void mergeSort(int a[], int left, int right)//합병정렬
{
	if (left < right)
	{
		int mid = (left + right) / 2;
		//분할
		mergeSort(a, left, mid);
		mergeSort(a, mid + 1, right);
		//합병
		merge(a, left, mid, right);
	}
	
}