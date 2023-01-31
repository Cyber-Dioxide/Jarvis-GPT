
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main() {
int check = 12;
char aik[10];
//char *char_ptr;
int *int_ptr;

int_ptr = &check;

printf("[INT_PTR] variable is at %p, value: %s , val 2 = %d\n" , int_ptr , &int_ptr , int_ptr);
strcpy(aik , "[=ADDING=]");
//char_ptr = aik;
printf("[CHAR_PTR] variable is at %p, value: %s , val 2 = %s\n" , aik , *aik , aik&);
return 0;
}