#include <stdio.h>
#include <math.h>
int main(void)
{ 
    double x1,x2,y1,y2,x3,y3;
    printf("x‚ÌÀ•W‚ğ“ü‚ê‚Ä‚­‚¾‚³‚¢(x‚Ì”ÍˆÍ‚Í0<=x<=3.0‚Å‚ ‚é)");
    scanf("%lf",&x3);
    if (x3 >= 0 && x3 <= 1.2)
    {
    y1=0;
    y2=1.2;
    x1=0;
    x2=1.2;
    y3=(y2-y1)*(x3-x1)/(x2-x1)+y1;
    printf("y=%lf",y3);
    }
    else if (x3 > 1.2 && x3 <= 2.5)
    {
    y1=1.2;
    y2=6.25;
    x1=1.2;
    x2=2.5;
    y3=((y2-y1)/(x2-x1))*(x3-x1)+y1;
    printf("y=%lf",y3);
    }
    else if (x3 >2.5 && x3 <=3.0)
    { 
        y1=6.25;
        y2=9.0;
        x1=2.5;
        x2=3.0;
        y3=((y2-y1)/(x2-x1))*(x3-x1)+y1;
        printf("y=%lf",y3);
    }
    else
    {
        printf("”ÍˆÍŠO‚Å‚ ‚é‚à‚¤ˆê“x‘Å‚¿’¼‚µ‚Ä‚­‚¾‚³‚¢\n");
    }
    return 0;
}