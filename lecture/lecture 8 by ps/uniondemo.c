#include<stdio.h>
union myunoion
{
	int a;
	int b;
}
main()
{
	union myunoion u1;
	union myunoion u2;
	u1.a=10;
	u2.b=20;
	printf("A is : %d",u1.a);
	printf("A is : %d",u2.b);
}
