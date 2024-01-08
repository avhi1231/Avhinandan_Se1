#include<iostream>
using namespace std;
class Person{
	private:
		string name,country;
		int age;
		public:
		set()
		{
			cout<<"\nEnter Your name : ";
			cin>>name;
			cout<<"\nEnter Your Age : ";
			cin>>age;
			cout<<"\nEnter your County :";
			cin>>country;
		}
		get()
		{
			cout<<"\nName  : "<<name;
			cout<<"\nAge  : "<<age;
			cout<<"\nCountry : "<<country;
		}
};
int main()
{
	Person obj;
	obj.set();
	obj.get();
}
