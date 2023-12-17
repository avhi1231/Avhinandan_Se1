#include<stdio.h>
void main(){
	int num;
	printf("Enter the number to check even or odd: ");
	scanf("%d",&num);
	if(num%2==0){
		printf("Even");
	}
	else{
		printf("Odd");
	}
}
