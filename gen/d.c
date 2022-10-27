#include <stdio.h>
#include <math.h>
#include <complex.h>
int main(void)
{ 
    double a,b,c,D,h;
    printf("abc‚Ì’l‚ð“ü‚ê‚æ“ñŽŸ•û’öŽ®a*pow(x,2.0)+b*x+c‚Ì’l‚Å‚ ‚é");
    scanf("%lf%lf%lf",&a,&b,&c);
    h=0;
    D=b*b-4*a*c;
    if (D>=0)
    {   double x,x1,x2;
        a*pow(x,2.0)+b*x+c==h;
        x1=(-b+sqrt(D))/2/a;
        x2=(-b-sqrt(D))/2/a;
        if (x1==x2)
        {printf("x=%lf",x1);}
        else
        {printf("x=%lf,%lf\n",x1,x2);}
    }
    else 
    {
        double x,x1a,x1b,x2a,x2b;
        x1a=-b/2/a;
        x1b=+sqrt(-D)/2/a;
        x2a=-b/2/a;
        x2b=-sqrt(-D)/2/a;
        if (x1a+x1b==x2a+x2b)
        printf("x=%lf+%lfi\n",x1a,x2b);
        else
        printf("x=%lf+%lfi,%lf%lfi\n",x1a,x1b,x2a,x2b);
    }
    return 0;
}