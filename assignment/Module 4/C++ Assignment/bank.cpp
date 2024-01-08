#include<iostream>
using namespace std;

class Bank{
	public:
		string name,type;
		int ac,amount,d,w,t;
		assign()
		{
			cout<<"\nEnter Name Of Depositor : ";
			cin>>name;
			cout<<" \nDepositor Name - "<<name;
			cout<<"\nEnter Account Number : ";
			cin>>ac;
			cout<<"\n Account No. - "<<ac;
			cout<<"\nEnter Type Of Account : ";
			cin>>type;
			cout<<" \nAccount Type - "<<type;
			cout<<"\nEnter your Current Amount - ";
			cin>>amount;
			cout<<"\nBalance Amount in A/c - "<<amount;
			
			
		}
		deposit()
		{
			cout<<"\nEnter Deposit Amount : ";
			cin>>d;
			cout<<d<<"   Deposit Succeful !";
			
		}
		withdraw()
		{
			
			t=amount+d;
			cout<<"\n Total Amount in A/c :"<<t;
			cout<<"\nEnter Withdraw Amount : ";
			cin>>w;
			cout<<w<<"    Withdraw Succeful !";
			cout<<"\nAvalabile Amount in A/c -  "<<t-w;
			
		}
		nam()
		{
			cout<<" \nDepositor Name - "<<name;
			cout<<"\nAvalabile Amount in A/c -  "<<t-w;
			
		}
};
int main()
{
	Bank obj;
	obj.assign();
	obj.deposit();
	obj.withdraw();
	obj.nam();
}
