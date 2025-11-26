#include <stdio.h>
#include <stdlib.h>


int	check_line_left(int **array)
{
	int	l;
	int	c;
	int	max;
	int counter;
	int correct_lines;

	l = 1;
	while (l < 5)
	{
		c = 2;
		max = array[l][1];
		counter = 1;
		while(c < 5)
		{
			if(array[l][c] > max)
			{
				counter++;
				max = array[l][c];
			}
			c++;
		}

		printf("arr[%d] has %d view where key value was %d \n",l,counter, array[l][0]);

 		if(counter == array[l][0])
			correct_lines++;
		l++;
	}
	if(correct_lines == 4)
		return (1);
	return (0);
}


int	check_line_right(int **array)
{
	int	l;
	int	c;
	int	max;
	int counter;
	int correct_lines;

	l = 1;
	while (l < 5)
	{
		c = 4;
		max = array[l][3];
		counter = 1;
		while (c > 1)
		{
			if(max == 4)
				break;
			if(array[l][c] > max)
			{
				counter++;
				max = array[l][c];
			}
			c--;
		}

		printf("arr[%d] has %d view where key value was %d \n",l,counter, array[l][5]);

 		if(counter == array[l][5])
			correct_lines++;
		l++;
	}
	if(correct_lines == 4)
		return (1);
	return (0);
}


int	check_col_top(int **array, int c)
{
	int i;
    int max;
	int diffCounter;

	i = 2;
	diffCounter = 1;
	max = array[1][c];
	if(max == 4 && array[0][c] == 1)
		return 1;
	while(array[i][c] != 4)
	{
		if(array[i][c] > max)
		{
			max = array[i][c];
			diffCounter++;
		}
		else if(array[c][i] == 0){// Make true if 0
			diffCounter = array[c][0]-1;
			break;
		}
		i++;
	}
	diffCounter++;
	if(diffCounter == array[0][c])
		return (1);
	return (0);
}

int	check_col_btm(int **array, int c)
{
	int i;
    int max;
	int diffCounter;

	i = 3;
	diffCounter = 1;
	max = array[4][c];
	if(max == 4 && array[5][c] == 1)
		return 1;
	while(array[i][c] != 4)
	{
		if(array[i][c] > max)
		{
			max = array[i][c];
			diffCounter++;
		}
		else if(array[c][i] == 0){// Make true if 0
			diffCounter = array[c][0]-1;
			break;
		}
		i--;
	}
	diffCounter++;
	if(diffCounter == array[5][c])
		return (1);
	return (0);
}

int check_line_rep(int **array, int l)
{
	int i;
	int c;

	i = 1;
	while(i <= 4)
	{
		c = i + 1;
		while(c <= 4)
		{
			if(array[l][i] == array[l][c] && array[l][i] != 0){
				return (0);
			}
			c++;
		}
		i++;
	}
	return (1);
}