/*Write a C++ program to implement a class called Bank Account that has
private member variables for account number and balance. Include
member functions to deposit and withdraw money from the account.*/
#include<iostream>
using namespace std;
class Bank_Account{
	private:
		int ac,balance,depo;
		public:
			deposit()
			{
				cout<<"\nEnter Your A/c No.: ";
				cin>>ac;
				cout<<"\nEnter Deposit amount : ";
				cin>>depo;
				cout<<"\nA/c No. : "<<ac<<"\nDeposit Amount :"<<depo;
			}
			withdraw()
			{
				int wit;
				cout<<"\nEnter Withdraw Amount : ";
				cin>>wit;
				balance=depo-wit;
				cout<<wit<<"  Withdraw Succefully ! \n";
				cout<<"Remainding A/c Balance "<<balance;
			}
};
int main()
{
	Bank_Account obj;
	obj.deposit();
	obj.withdraw();
}
