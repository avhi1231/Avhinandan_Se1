//Write a program to find out the max from given number (E.g., No: -1562 Max number is 6)
#include <stdio.h>

void main()
{
	int A, B, C;

	printf("Enter the numbers A, B and C: ");
	scanf("%d %d %d", &A, &B, &C);

	// finding max using compound expressions
	if (A >= B && A >= C)
		printf("%d is the largest number.", A);

	else if (B >= A && B >= C)
		printf("%d is the largest number.", B);

	else
		printf("%d is the largest number.", C);
}
