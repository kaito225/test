#include <stdio.h>
#include <math.h>
int main(void)
{  double i,round(double);
    double x,cs,xh,xl,x2;
    i=0.0001;x=0.0;
    for (;;) {
    cs=cos(x/2);
    x=x+0.1;
    if(cs<0.0)
    {
    for(;;)
    {xh=x;
    xl=x-i;
    x=(xh+xl)/2;
    cs=round(cos(x/2)*100000)/100000;
    if(cs==0.0)
    {break;}
    }
    break;
    }
    }
    printf("cos(x/2)=0‚É‚È‚é‚Æ‚«x‚Ì’l‚Í%lf‚Å‚ ‚éB\n",x);
    return 0;
}