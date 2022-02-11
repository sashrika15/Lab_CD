// Elimination of Left Factoring

// Left Factoring: A -> ab1 | ab2
// Elimination: 
// A -> aA'
// A' -> b1 | b2

#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    int i=0, idx;
    char c,ch,initial;
    char a[10];
    int b1=0,b2=0;
    printf("Enter the production (Using equal sign like A=Ab|a): \n");
    
    scanf("%s%c",a,&ch);
    
    initial=a[0];
    c=a[2];
    for(int k=3; k<strlen(a); k++) {
        if(a[k]=='|')
            { idx = k;
            break;
            }
    }

    if(c==a[idx+1]) {
        printf("Left Factoring found\n");
        // Rule 1
        printf("%c -> ",initial);
        for(int i=2,j=idx+1; j<strlen(a); i++,j++) {
            if(a[i]==a[j])
                printf("%c",a[i]);
            else
            {
                b1=i;
                b2=j;
            }
        }
    printf("%c'\n",initial);

    // Rule 2
    printf("%c' -> ",initial);

    for(int i=b1;i<idx;i++){
        printf("%c",a[i]);
        }
    
    printf("|");
    for(int i=b2;i<=strlen(a);i++){
        printf("%c\n",a[i]);
        }
    }

    else {
        printf("No left factoring\n");
    }
    
    return 0;
}
