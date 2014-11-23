#include <stdio.h>

void printEvenOrOdd(int x){
	if (x%2 == 0){
		printf("x is even\n");
	}
	else{
		printf("x is odd\n");	
	}
	
}
int main(void){
	int x = 7;
        printf("Hello, world!\n");
	printEvenOrOdd(x);
	if (x > 0 && x <10)
		printf(" ture\n");
	else
		printf("x is out of range.\n");
	printf("!x = %d\n", !x);
        return 0;


}
