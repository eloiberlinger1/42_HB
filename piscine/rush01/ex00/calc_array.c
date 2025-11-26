#include <stdio.h>
#include <stdlib.h>
#include "ft_putchar.c"
#include "check_side.c"

int	is_valid(int **array, int l, int c, int k);

//debug
void	display_array(int **array);

int solve_backtrack(int **array, int l, int c, int k)
{
	if(l == 5)
		return 1;
	else if( c == 5)
		return solve_backtrack(array, l+1, 1, 0);
	else if(array[l][c] != 0)
		return solve_backtrack(array, l, c+1, 0);

	k = 1;
	while (k < 5)
	{
		if(is_valid(array, l, c, k))
		{
			if(solve_backtrack(array, l, c+1, k))
			{
				printf("trouve : %d", k);
				return (1);
			}
			array[l][c] = 0;
		}
		k++;
	}
	array[l][c] = 0;
	return (0);
}



// DEBUG
int **gen_array(void)
{
	int **array;
	int i;

	array = (int**)malloc(6*24);
	i = 0;
	while(i < 6)
	{
		array[i] = (int*) malloc(6*4);
		++i;
	}

	return array;
}
void	ft_putchar(char c);
void display_array(int **array)
{
	int l;
	int c;

	l = 0;
	while(l < 6)
	{
		c = 0;
		while(c < 6)
		{
			ft_putchar(array[l][c] + '0');
			ft_putchar(' ');
			c++;
		}
		ft_putchar('\n');
		l++;
	}
}


int main(void)
{
	int **array = gen_array();
	int l;
	int c;

	int testarray[6][6] = {
		{0,4,3,2,1,0},
		{4,0,2,3,4,1},
		{3,0,0,0,0,2},
		{2,0,0,0,0,2},
		{1,0,0,0,0,2},
		{0,1,2,2,2,0},
	};

/* 	int testarray[6][6] = {
		{0,4,3,2,1,0},
		{4,1,2,3,4,1},
		{3,2,3,4,1,2},
		{2,3,4,1,2,2},
		{1,4,1,2,3,2},
		{0,1,2,2,2,0},
	}; */

	//copying everything to test
	l = 0;
	while(l < 6)
	{
		c = 0;
		while(c < 6)
		{
			array[l][c] = testarray[l][c];
			c++;
		}
		l++;
	}
	//copying everything to test ---- to deldete
	
	
	display_array(array);
	
	printf("\n%d \n", is_valid(array, 1, 1, 1));

	solve_backtrack(array, 1, 1, 0);

	display_array(array);

	return 0;
}
