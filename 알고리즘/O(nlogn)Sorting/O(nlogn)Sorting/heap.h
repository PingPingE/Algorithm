#pragma once
#include <iostream>
using namespace std;
//최대힙 구현
inline void sift_down(int a[], int current, int last)
{
	int largest = current; //부모노드로 초기화
	while ((current*2)+1 <= last)//자식노드가 있으면
	{
		int left = (current*2) + 1; //왼쪽 자식
		int right = (current*2) + 2; //오른쪽 자식
		if ( a[left] > a[largest]) // 왼쪽자식이 largest보다 큰 값을 가질 때
		{
			largest = left;
		}
		if (right <= last && a[right] > a[largest]) //오른쪽 자식이 있고, largest보다 큰 값을 가질 떼
		{
			largest = right;
		}
		if (largest != current)//largest값이 바꼈을 경우
		{
			//largest자리와 current 자리를 바꿔줌
			int temp = a[largest];
			a[largest] = a[current];
			a[current] = temp;
			//current값 갱신
			current = largest;
		}
		else//최대힙이 이미 완성된 경우(largest값이 그대로인 경우)
			return;
	}

}
inline void heapify(int a[], int size) //Bottom-up
{
	int end = size - 1; 
	int current = end / 2; //부모노드 시작점(밑에서 부터)
	while(current >= 0)
		sift_down(a, current--, end);
}
void heap(int a[], int size)
{
	heapify(a, size); //최대힙으로 빌드
	for(int i = size - 1; i > 0; i--)//정렬
	{
		//가장 꼭대기 노드를 가장 마지막 노드와 바꿔준다.
		int temp = a[0];
		a[0] = a[i];
		a[i] = temp;
		//힙을 리빌드한다.
		heapify(a,i);
	}

}