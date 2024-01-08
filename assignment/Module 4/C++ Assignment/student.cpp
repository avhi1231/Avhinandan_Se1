#include<iostream>
using namespace std;
class Student{
	private:
		string name,clas;
		int roll,marks;
		public:
			Student()
			{
				cout<<"\nEnter Student name : ";
				cin>>name;
				cout<<"\nEnter Student Class : ";
				cin>>clas;
				cout<<"\nEnter Roll Number : ";
				cin>>roll;
				cout<<"\nEnter Marks (0-100) ";
				cin>>marks;
			}
			calculate()
			{
				if (marks >= 90)
				{
				cout<<"A+";
      			}
				else if (marks >= 80)
				{
				    cout<<"A";
				}
				else if (marks >= 70) 
				{
				cout<<"B";
				}
				else if (marks >= 60)
				{
				    cout<<"C";
				} 
				else
				{
				cout<<"D";
      			}
			}
		display()
		{
      cout << "\n\nName: " << name;
      cout << "Class: " << clas;
      cout << "Roll Number: " << roll;
      cout << "Marks: " << marks;
      cout << "Grade: " << calculate();
		}
		 
};
int main()
{
	Student obj;
	obj.calculate();	
	obj.display();
}

