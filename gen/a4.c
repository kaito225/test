#include <stdio.h>
#include <math.h>
int main(void)
{ 
    int a,b,total,c;
    a=1;b=1;total=0;
    for (;;) {if(1<=a<=50 && 1<=b<=50 && a<=b)
       { for(;;){c=pow(a,2)+pow(b,2);
           if(c>=1000 && c%13==0)
        {total=total+1;}
       b=b+1;
       if(b>50)
       {a=a+1;
       b=a;
       break;}}}
        if(a>50)
        {break;}
    }
    printf("a**2+b**2‚ª1000ˆÈã‚É‚È‚èA13‚Ì”{”‚É‚È‚éŒÂ”‚Í%d‚Å‚ ‚éB\n",total);
    return 0;
}