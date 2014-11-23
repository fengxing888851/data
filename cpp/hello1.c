#include <stdio.h>

void newline(void){
        printf("\n");
}
int main(void){
/*	int a,b,c;
	printf("input a,b,c\n");
	scanf("%d%d%d",&a,&b,&c);
	printf("a=%d, b=%d, c=%d\n", a+b,b,c);
*/
	int a,b;
	printf("input a\n");
	scanf("%5d%3d", &a,&b);
	printf("a=%d,b=%d",a,b);
        printf("Hello, world!\n");
        newline();
        printf("hello\n");
        return 0;
}
