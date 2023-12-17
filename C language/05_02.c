#include<stdio.h>
void main(){
	int i,num[5],sum=0;
	for(i=0;i<5;i++){
		printf("Enter Your number here [%d] :",i);
		scanf("%d",&num[i]);
		sum+=num[i];
	}
//	for(i=0;i<5;i++){
		printf("%d \n",sum);
	}

