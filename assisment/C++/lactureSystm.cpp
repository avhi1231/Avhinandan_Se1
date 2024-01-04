#include<iostream>
using namespace std;
class Lecture{
	public:
		string name,sub,cors,lec;
		int num,i;
					
		assign()
		{
	
		cout<<"*********Assign the Value**************\n";
		for(i=0;i<5;i++)
		{
			cout<<"\nEnter Name of the lecturer "<<i+1<<":\t";
			cin>>name;
			cout<<"\nEnter Name of the subject "<<i+1<<":\t";
			cin>>sub;
			cout<<"\nEnter Name of course "<<i+1<<":\t";
			cin>>cors;
			cout<<"\nEnter Number of lecturers "<<i+1<<":\t";
			cin>>num;
		}
		}
		detail()
		{
			cout<<"\n********Lecture Detail********";
			for(i=0;i<5;i++)
			{
			cout<<"\nAdd Lecture Detail "<<i+1<<":\t";
			cin>>lec;
			}
		}
		display()
		{
			cout<<"\n*******Display*********"
			for(i=0;i<5;i++)
			{
			cout<<"\nName of the lecturer "<<i+1<<":  "<<name;
			cout<<"\nLacture Detail "<<i+1<<":  "<<lec;
			}
		}
};
int main()
{
	Lecture obj;
	obj.assign();
	obj.detail();
	obj.display();
}
