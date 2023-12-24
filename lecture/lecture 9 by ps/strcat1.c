#include<stdio.h>
main()
{
	char a[30];
	char b[30];
	printf("Enter String 1: ");
	scanf("%s",&a);
	printf("Enter String 2: ");
	scanf("%s",&b);
	printf("\n%s",strcat(a,b));		
}
