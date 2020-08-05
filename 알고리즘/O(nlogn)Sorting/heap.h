#pragma once
#include <iostream>
using namespace std;
//�ִ��� ����
inline void sift_down(int a[], int current, int last)
{
	int largest = current; //�θ���� �ʱ�ȭ
	while ((current*2)+1 <= last)//�ڽĳ�尡 ������
	{
		int left = (current*2) + 1; //���� �ڽ�
		int right = (current*2) + 2; //������ �ڽ�
		if ( a[left] > a[largest]) // �����ڽ��� largest���� ū ���� ���� ��
		{
			largest = left;
		}
		if (right <= last && a[right] > a[largest]) //������ �ڽ��� �ְ�, largest���� ū ���� ���� ��
		{
			largest = right;
		}
		if (largest != current)//largest���� �ٲ��� ���
		{
			//largest�ڸ��� current �ڸ��� �ٲ���
			int temp = a[largest];
			a[largest] = a[current];
			a[current] = temp;
			//current�� ����
			current = largest;
		}
		else//�ִ����� �̹� �ϼ��� ���(largest���� �״���� ���)
			return;
	}

}
inline void heapify(int a[], int size) //Bottom-up
{
	int end = size - 1; 
	int current = end / 2; //�θ��� ������(�ؿ��� ����)
	while(current >= 0)
		sift_down(a, current--, end);
}
void heap(int a[], int size)
{
	heapify(a, size); //�ִ������� ����
	for(int i = size - 1; i > 0; i--)//����
	{
		//���� ����� ��带 ���� ������ ���� �ٲ��ش�.
		int temp = a[0];
		a[0] = a[i];
		a[i] = temp;
		//���� �������Ѵ�.
		heapify(a,i);
	}

}