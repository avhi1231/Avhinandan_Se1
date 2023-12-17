#include<stdio.h>
#include<string.h>
main(){
	int  choce,i,ans;
	//char ans[3];
	float qui,total;
	while(1){
	printf("1 IDLI    1  psc   40  rs \n");
	printf("2 DOSA    1  psc   120 rs \n");
	printf("3 Pizza   1  psc   220 rs \n");
	printf("4 Pasta   1  bowl  550 rs \n");
	printf("Enter your order here : ");
	scanf("%d",&choce);
	printf("Enter how things do you want ? ");
	scanf("%f",&qui);
	switch(choce){
		case 1:
			total = qui*40;
			break;
		case 2:
			total = qui*120;
			break;
		case 3:
			total = qui*220;
			break;
		case 4:
			total = qui*550;
			break;
	}
	
	printf("Do you want to order something else ?\n");
	printf("for yes press = 0  \n  for no press = 1 \n");
	scanf("%d",&ans);
	if(ans==0){
	
	}else{
		printf("Thanks for your order ..\n");
		break;
		i++;
		return 1;
	}
	}
	printf(" \nThis is your total payable amount  %.2f",total);
}
