#pragma once
void Selection(int arr[], int size)
{
	int max = 0, temp = 0; //�ִ밪 ��������
	for (int i = size - 1; i >= 0; i--)//�ڿ�������
	{
		max = i;//index�� ����
		for (int j = i - 1; j >= 0; j--)
		{
			if (arr[j] > arr[max])// �� ū ���� ������
				max = j; //�ش簪�� �ε����� max��
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