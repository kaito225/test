#include <stdio.h>
#include <math.h>
int main(void)
{ 
    int yakusuu,total;
    int j,i,n;
    printf("n�̒l\n");
    scanf("%d",&n);
    j=2;total=0;
    for (;;) {
        if(j<=n)
        {
    yakusuu=0;i=1;
    for (;;)
    {
        if(i<=j)
    {
        if(j%i==0)
    {
        yakusuu=yakusuu+1;
    }
    i=i+1;
    if(i>j){break;}
    }
    }
    if(yakusuu==2)
    {total=total+j;}
    j=j+1;
    }
    if (j>n){break;}
    }
    printf("n�܂ł̑f���̑��a��%d�ł���B\n",total);
    return 0;
}