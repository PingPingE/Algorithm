#pragma once
#include <iostream>
static inline void error(char* msg) //error ó��
{
	std::cout << msg << std::endl;//�ش� �޼����� ����ϰ�
	exit(1); //����
}