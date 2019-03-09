#pragma once
#include <iostream>
using namespace std;
inline int partition(int a[], int left, int right)
{
	int L = left; //pivot 다음 값부터
	int R = right;//젤 끝 값부터
	int pivot =left; // 젤 처음 값을 pivot으로 설정
	int temp = 0; //swap할 때 필요한 변수

	while (L <= R)//L과R이 엇갈리기 전까지
	{
		while (L <= right && a[L] < a[pivot])//범위 중요! L은 right(끝까지)와 같거나 작을때 까지+pivot보다 작은 값
			L++; //앞에서 뒤로 이동하므로
		while (R > left && a[R] >= a[pivot]) // R은 left(처음까지)보다 클때 까지+pivot보다 큰 값
			R--;//뒤에서 앞으로 이동하므로

		if (L < R) //아직 안끝났으면
		{
			//R과 L swap
			temp = a[R];
			a[R] = a[L];
			a[L] = temp;
		}
	}
	//L과 R이 엇갈렸으면 R과 pivot자리 값을 swap
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
		//분할해서 계산
		Quick(a, left, p - 1);
		Quick(a, p + 1, right);
	}
	
}
