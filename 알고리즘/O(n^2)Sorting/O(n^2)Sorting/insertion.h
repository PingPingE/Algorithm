#pragma once
#include<iostream>
using namespace std;
void Insertion(int arr[], int size)
{
	int i = 0, j = 0;
	int val = 0;
	for (i = 1; i < size; i++)//������ ��
	{
		val = arr[i]; //val�� �������ش�.
		for (j = i - 1; j >= 0; j--)//val �տ� �ִ� ����� ��
		{
			if (arr[j] > val) //val���� ũ�� 
			{
				arr[j + 1] = arr[j]; //���ڸ� �ڷ� �̵�
			}
			else//val���� �۰ų� ������ break�ϰ� ��ĭ�ڿ� val����
			{
				//arr[j + 1] = val; <- ���⿡ ������ �� ����� �޶�����
				break;//val�� ���Խ����ְ� break �ϴ°Ŷ�
			}
				
		}
		arr[j + 1] = val;//break�ϰ� �������ͼ� val�� ���Խ�Ű�°Ŷ� ���� �ٸ���?
		
	}
	//display
	cout << "Insertion sorting : ";
	for (int k = 0; k < size; k++)
		cout << arr[k] << " ";
	cout << endl;
}
