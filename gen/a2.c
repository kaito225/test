#include <stdio.h>
#include <math.h>
int main(void)
{ 
    double total,a,b,i;
    printf("a�Ab�̏��Œl������\n");
    scanf("%lf%lf",&a,&b);
    i=1; 
    total=0;
    for (;;) {
     if (a==b)
     {total=total+b;
     break; }
     total=total+a; 
     a=a+i;
    }
    printf("a����b�܂ł̑��a��%lf�ł���B\n",total);
    return 0;
}