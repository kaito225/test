#include <stdio.h>
#include <math.h>
int main(void)
{ 
    double total,a,b,i;
    printf("aAb‚Ì‡‚Å’l‚ğ“ü‚ê‚æ\n");
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
    printf("a‚©‚çb‚Ü‚Å‚Ì‘˜a‚Í%lf‚Å‚ ‚éB\n",total);
    return 0;
}