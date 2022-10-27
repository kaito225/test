#include <stdio.h>
#include <math.h>
int main(void)
{ 
    int a,b,n;
    double napier;
    napier=1.0;
    b=1;
    printf("シグマのnの回数をしてしてください");
    scanf("%d",&n);
    for (a=1;a<n;a++) {b*=a;
    napier+=1.0/b;}
    printf("e=%fである。\n",napier);
    return 0;
}