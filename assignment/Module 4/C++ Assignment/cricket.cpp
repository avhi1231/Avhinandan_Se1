#include<iostream>
using namespace std;
class Batsman{
	public:
		float tr,ar,avg,bp;
		input()
		{
			cout<<"\nEnter Total Runs : ";
			cin>>tr;
			cout<<"\nEnter Best Performance : ";
			cin>>bp;
		}
};
class Cricketer :public Batsman{
	public:
		
		average()
		{
			
			avg=tr/bp;
		}
		display()
		{
			cout<<"\nTotal Runs : "<<tr;
			cout<<"\nAverage : "<<avg;
			cout<<"\nBest Performance : "<<bp;
		}
		
};
int main()
{
	Cricketer obj;
	obj.input();
	obj.average();
	obj.display();
}
