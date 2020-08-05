#pragma once
void Bubble(int arr[], int size)
{
	int temp= 0;
	for (int i = size-1; i >0; i--) //정렬할 범위(뒤에서 부터 좁혀옴)
	{
		for (int j =0; j<i; j++) //정렬진행(앞에서 부터)
		{
			if (arr[j] > arr[j+1]) //앞뒤 비교 
			{ //앞에가 더 크면 swap
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	//display
	cout << "Bubble sorting : ";
	for (int k = 0; k < size; k++)
		cout << arr[k] << " ";
	cout << endl;
}