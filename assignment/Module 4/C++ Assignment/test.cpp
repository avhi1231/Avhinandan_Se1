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
    int mark[2],i;
    in()
    {
        cout<<"\nEnter the marks :"<<endl;
        for(i=0;i<2;i++)
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
        t=mark[0]+mark[1];
    }
    dis()
    {
        cout<<"\nName :"<<a;
        cout<<"\nRoll.no :"<<roll;
        cout<<"\nMarks entered :";
        for(i=0;i<2;i++)
        {
            cout<<mark[i]<<" ";
        }
        cout<<"\nTotal marks:"<<t;
       
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
