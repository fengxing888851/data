#include <math.h>
#include <stdio.h>


double pi=3.1415;
double circleSquare(double x1, double x2, double y1, double y2){
        double square;
        double radius;
        radius = 0.5*sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
        square = pi*radius*radius;
        return square;
}
int increment(int x){
        x = x + 1;
        return x;
}
int main(void){
        double z = circleSquare(125,3.78,23,32);
        int i = 1, j = 2;
//      printf("sin(pi/2)=%f\nln1=%f\n", sin(pi/2), log(1.0));
        int y = increment(i);
        printf("%d\ncircleSquare=%f\n",y,z);
        return 0;
}
