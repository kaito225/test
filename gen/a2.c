#include <stdio.h>
#include <math.h>
int main(void)
{ 
    double total,a,b,i;
    printf("a、bの順で値を入れよ\n");
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
    printf("aからbまでの総和は%lfである。\n",total);
    return 0;
}