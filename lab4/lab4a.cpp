// Elimination of Left recursion


// Left recursion: A -> Aa|b
// Elimination rules:
// Rule 1: A -> bA'
// Rule 2: A' -> aA' | e

#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    int i=0,k=0,n=0;
    char c,ch;
    char a[10];
    printf("Enter the production (Using equal sign like A=Ab|a): \n");
    scanf("%s%c",a,&ch);
    
    c=a[0];
    if(a[2] == c)
    { 
        printf("Left recursion found: \n");
        // Rule 2
        printf("%c' -> ",c);
        // Search all characters till we find | 
        for(k=3;k<strlen(a) && a[k] != '|';k++)
        { 
            printf("%c",a[k]);
        } 
        printf("%c' | e",c);

        // Rule 1
        n=k; i=0;
        printf("\n%c -> ",c);
        for(k=n+1; k<strlen(a) && a[k]!='\0'; k++)
        {
            printf("%c",a[k]);
        }
        printf("%c'\n",c);
    }
    else
    {
        printf("No left recursion\n");
    } 
    return 0;
}
