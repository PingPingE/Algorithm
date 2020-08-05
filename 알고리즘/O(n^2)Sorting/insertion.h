#pragma once
#include<iostream>
using namespace std;
void Insertion(int arr[], int size)
{
	int i = 0, j = 0;
	int val = 0;
	for (i = 1; i < size; i++)//삽입할 값
	{
		val = arr[i]; //val에 저장해준다.
		for (j = i - 1; j >= 0; j--)//val 앞에 있는 값들과 비교
		{
			if (arr[j] > val) //val보다 크면 
			{
				arr[j + 1] = arr[j]; //한자리 뒤로 이동
			}
			else//val보다 작거나 같으면 break하고 한칸뒤에 val대입
			{
				//arr[j + 1] = val; <- 여기에 있으면 왜 결과가 달라질까
				break;//val을 대입시켜주고 break 하는거랑
			}
				
		}
		arr[j + 1] = val;//break하고 빠져나와서 val을 대입시키는거랑 뭐가 다를까?
		
	}
	//display
	cout << "Insertion sorting : ";
	for (int k = 0; k < size; k++)
		cout << arr[k] << " ";
	cout << endl;
}
