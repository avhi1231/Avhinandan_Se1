/*
= int num =25 
+=, -=,/=,*=
*/
#include<stdio.h>    
main()          
{
	int num,num1;
	printf("Enter your 1St number here :");
	scanf("%d",&num);
	printf("Enter your 2nd number here :");
	scanf("%d",&num1);
	printf("This is your addition of two numbers : %d\n",num+=num1);   
	printf("This is Your Num : %d\n",num);
	printf("This is your Sub of two numbers : %d\n",num-=num1);   
	printf("This is Your Num : %d\n",num);
	printf("This is your multi of two numbers : %d\n",num*=num1);   
	printf("This is Your Num : %d\n",num);
	printf("This is your div of two numbers : %d\n",num/=num1);   
	printf("This is Your Num : %d\n",num);
}
