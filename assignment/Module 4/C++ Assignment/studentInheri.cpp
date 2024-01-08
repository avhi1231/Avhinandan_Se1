#include<iostream>
using namespace std;
class Person{
	public:
		string name;
		int age;
		write()
		{
			cout<<"\nEnter Name Of Person: ";
			cin>>name;
			cout<<"\nEnter Age Of Person : ";
			cin>>age;
		}
		read()
		{
			cout<<"\nName Of Person : "<<name;
			cout<<"\nAge Of Person : "<<age;
		}
};
class Student : public Person{
	public:
		float percentage;
		input()
		{
			cout<<"\n Enter Percentage of Student :";
			cin>>percentage;
		}
		output()
		{
			cout<<"\nPercentage of Student : "<<percentage;
		}
};
class Teacher : public Student{
	public:
		int salary;
		get()
		{
			cout<<"\nEnter Salary Of the Teacher :";
			cin>>salary;
		}
		show()
		{
			cout<<"\nTeacher Salary : "<<salary;
		}
};
int main()
{
	Teacher obj;
	obj.write();
	obj.input();
	obj.get();
	obj.read();
	obj.output();
	obj.show();
}
