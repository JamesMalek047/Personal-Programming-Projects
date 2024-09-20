

#include <stdio.h>

void fibonacci(){
    int n;
    printf("Enter # of terms: ");
    scanf("%d", &n);
    int a = 0, b = 1, c;
    for (int i = 0; i < n; i++) {
        printf("%d ", a);
        c = b;
        b = b + a;
        a = c;
    }
}

int main() {
    fibonacci();
    return 0;
}

