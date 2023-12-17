#include<stdio.h>
main()
{
	int n,i=1,ev=0,od=0,evsum=0,odsum=0;
	printf("Enter the End Number : ");
	scanf("%d",&n);
	while(i<=n)
	{
		if(i%2==0)
		{
			printf("\n%d : This number is Even !",i);
			ev++;
			evsum += i;
		}
		else
		{
			printf("\n%d : This number is Odd !",i);
			od++;
			odsum += i;
		}
		i++;
	}
	printf("Even Count : %d\n",ev);
	printf("Odd Count : %d\n",od);
	printf("Even Sum : %d\n",evsum);
	printf("Odd Sum : %d\n",odsum);
}
