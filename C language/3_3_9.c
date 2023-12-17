#include <stdio.h>
/*structure declaration*/
struct employee{
    char    name[30];
    char    address[30];
    int     empno,age;
};
 
void main()
{
    /*declare structure variable*/
    struct employee emp;
     
    /*read employee details*/
    printf("\nEnter details :\n");
    printf("Name ?:");          gets(emp.name);
    printf("address ?:");        gets(emp.address);
    printf("Emp_number ?:");     scanf("%d",&emp.empno);
    printf("age ?:");            scanf("%d",&emp.age);
    
     
    /*print employee details*/
    printf("\nEntered detail is:");
    printf("Name: %s\t"   ,emp.name);
    printf("Address: %s\n",emp.address);
    printf("Id: %d\t"     ,emp.empno);
    printf("Age: %d\t"     ,emp.age);
    
}
