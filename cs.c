// #include <cs50.h>
#include <stdio.h>
int main(void)
{
    int height;
    int row;
    int coloum, space;
    do
    {
        height = 7;
    } while (height < 1 || height > 8);

    for (row = 0; row < height; row++)
    {
        for (space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        for (coloum = 0; coloum <= row; coloum++)
        {
            printf("#");
        }
        printf("\n");
    }
}