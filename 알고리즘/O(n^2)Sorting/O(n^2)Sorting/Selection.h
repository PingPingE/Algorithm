#pragma once
void Selection(int arr[], int size)
{
	int max = 0, temp = 0; //최대값 선택정렬
	for (int i = size - 1; i >= 0; i--)//뒤에서부터
	{
		max = i;//index를 저장
		for (int j = i - 1; j >= 0; j--)
		{
			if (arr[j] > arr[max])// 더 큰 값이 있으면
				max = j; //해당값의 인덱스를 max로
		}
		//swap
		temp = arr[i];
		arr[i] = arr[max];
		arr[max] = temp;
	}
	//display
	cout << "Selection sorting : ";
	for (int k = 0; k < size; k++)
		cout << arr[k] << " ";
	cout << endl;
}