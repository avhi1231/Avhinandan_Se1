#include<stdio.h>
myfun(num)
{
	
	int i,fact=1;
	for(i=1;i<=num;i++)
	{
		fact=fact*i;
	}
	printf("Factorial is : %d",fact);
	
}
main()
{
	int x;
	printf("Enter Number: ");
	scanf("%d",&x);
	myfun(x);
}
