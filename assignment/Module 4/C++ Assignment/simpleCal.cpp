#include<iostream>
using namespace std;
class cal{
	public:
		int choice,a,b;
		fun()
		{
			cout<<"Enter 1 for + \n Enter 2 for - \n Enter 3 for * \n Enter 4 for /";
			cout<<"\nEnter your choice :";
			cin>>choice;
			cout<<"Enter 1 Value : ";
			cin>>a;
			cout<<"Enter 2 Value : ";
			cin>>b;
			if(choice==1)
			{
				cout<<"Addition : "<<a+b;
			}
			else
			{
				if(choice==2)
				{
					cout<<"Subtraction : "<<a-b;
				}
				else
				{
					if(choice==3)
					{
						cout<<"Multiplication : "<<a*b;
					}
					else
					{
						if(choice==4)
						{
							cout<<"Division :"<<a/b;
						}
						else
						{
							cout<<"Invaild Choice !! ";
						}
					}
				}
			}
		}
};

int main()
{
	cal obj;
	obj.fun();
}
