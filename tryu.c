// Your First C++ Program

#include <stdio.h>

int main() {
    int arr[]={1,2,3,4,6} ;
    int * r= arr;
    printf("%p, %d", r+1,*(r+1)) ;
    return 0;
}