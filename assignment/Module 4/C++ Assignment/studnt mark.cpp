//Write a C++ Program display Student Mark sheet using Multiple inheritance
#include <iostream>
using namespace std;
class Student
{
    public:
    char a[30];
    int roll;
    get()
    {
        cout<<"\nEnter the name :";
        cin>>a;
        cout<<"\nEnter the roll.no :";
        cin>>roll;
    }
};
class Mark
{
    public:
    int mark[4],i;
    in()
    {
        cout<<"\nEnter the marks :"<<endl;
        for(i=0;i<4;i++)
        {
            cin>>mark[i];
        }
    }
};
class Process:public Student,public Mark
{
    public:
    int t;
    float avg;
    calc()
    {
        t=mark[0]+mark[1]+mark[2]+mark[3];
        avg=t/4;
    }
    dis()
    {
        cout<<"\nName :"<<a;
        cout<<"\nRoll.no :"<<roll;
        cout<<"\nMarks entered :";
        for(i=0;i<4;i++)
        {
            cout<<mark[i]<<" ";
        }
        cout<<"\nTotal marks:"<<t;
        cout<<"\nAverage :"<<avg;
    }
};
int main()
{
    cout<<"\nStudent marks list";
    Process obj;
    obj.get();
    obj.in();
    obj.calc();
    obj.dis();    
}
