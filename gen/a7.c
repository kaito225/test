#include <stdio.h>
#include <math.h>
#define kosuu 3
int i,j;
double a[kosuu],b[kosuu],c,d,e,f,u,p;
printf("�x�N�g������͂��Ȃ���a�Ab�̏�");
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
printf("a�x�N�g��*b�x�N�g��=%lf,a�x�N�g��*b�x�N�g��/��Βl�ia�x�N�g��*b�x�N�g���j��%lf\n",c,p)