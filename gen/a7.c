#include <stdio.h>
#include <math.h>
#define kosuu 3
int i,j;
double a[kosuu],b[kosuu],c,d,e,f,u,p;
printf("ベクトルを入力しなさいa、bの順");
for (i=0;i<kosuu;i++)
 {scanf("%lf",&a[i]);}
for (j=0;j<kosuu;j++)
 {scanf("%lf",&b[j]);}
i=0;j=0;
for (;;)
 {c=c+a[i]*b[j];
 i=i+1;j=j+1;
 if (j==kosuu)
 {break;}}
i=0;j=0;
for (;;)
{d=d+a[i]*a[i];
i=i+1;
if(i==kosuu)
{e=sqrt(d);
break;}}
for (;;)
{f=f+b[j]*b[j];
j=j+1;
if(j==kosuu)
{u=sqrt(f);
break;}}
p=c/u/e;
printf("aベクトル*bベクトル=%lf,aベクトル*bベクトル/絶対値（aベクトル*bベクトル）＝%lf\n",c,p)