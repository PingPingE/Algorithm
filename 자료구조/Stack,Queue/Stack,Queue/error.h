#pragma once
#include <iostream>
static inline void error(char* msg) //error 처리
{
	std::cout << msg << std::endl;//해당 메세지를 출력하고
	exit(1); //종료
}