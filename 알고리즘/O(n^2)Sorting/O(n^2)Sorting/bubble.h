#pragma once
void Bubble(int arr[], int size)
{
	int temp= 0;
	for (int i = size-1; i >0; i--) //������ ����(�ڿ��� ���� ������)
	{
		for (int j =0; j<i; j++) //��������(�տ��� ����)
		{
			if (arr[j] > arr[j+1]) //�յ� �� 
			{ //�տ��� �� ũ�� swap
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