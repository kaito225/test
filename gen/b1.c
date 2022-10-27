#include <stdio.h>
#include <math.h>
int main(void)
{ 
    double det,a[2][2],c;
    int i,j;
    printf("s—ñ2*2‚ğ“ü—Í‚¹‚æB\n");
    for (i=0;i<2;++i){
     for (j=0;j<2;++j){
      printf("A[%d][%d]=",i+1,j+1);
      scanf("%lf",&a[i][j]);}}
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0];
    if (det==0)
    {
        {printf("‹ts—ñ‚Í‘¶İ‚µ‚È‚¢\n");}
    }
    else 
    {  
        c=a[0][0];
        a[0][1]=-a[0][1]/det;
        a[1][0]=-a[1][0]/det;
        a[0][0]=a[1][1]/det;
        a[1][1]=c/det;
        printf("A^-1=( %lf %lf %lf %lf )\n",a[0][0],a[0][1],a[1][0],a[1][1]);
    }
    return 0;
}