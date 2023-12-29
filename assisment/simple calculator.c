#include<stdio.h>
main()								
{
	int choice,a,b;
	
//For Display Menu

	printf("--------MENU-------");
	printf("\n1. Addition");
	printf("\n2. Subtraction");
	printf("\n3. Multiplication");
	printf("\n4. Division");
	printf("\n");
	printf("\nEnter Your Choice : ");
	scanf("%d",&choice);
	printf("Enter Your 1st Num: ");
	scanf("%d",&a);
	printf("Enter your Second Num: ");
	scanf("%d",&b);	
	if(choice==1)
	{
		printf("Addition : %d",a+b);
	}
	else
	{
		if(choice==2)
		{
			printf("Subtraction: %d",a-b);
		}
		else
		{
			if(choice==3)
			{
			printf("Multiplication: %d",a*b);
			}
			else
			{
				if(choice==4)
			{
				printf("Division: %d",a/b);
			}
			else
			{
				printf("Invaild choice !!! ");
			}
	}
}
}}
