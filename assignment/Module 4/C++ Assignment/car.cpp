/*Write a C++ program to create a class called Car that has private
member variables for company, model, and year. Implement member
functions to get and set these variables.*/
#include<iostream>
using namespace std;
class Car{
	private:
		string company,model;
		int year;
		public:
			get()
			{
				cout<<"\nEnter Company name : ";
				cin>>company;
				cout<<"\nEnter Model Number : ";
				cin>>model;
				cout<<"\nEnter year : ";
				cin>>year;
			}
			set()
			{
				cout<<"\nCar Company name : "<<company;
				cout<<"\nModel No. : "<<model;
				cout<<"\nEnter Year : "<<year;
			}
};
int main()
{
	Car obj;
	obj.get();
	obj.set();
}
