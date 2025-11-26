#include "array_checker.c"

int check_all_col_top(int **array)
{
    int t;

    t = 1;
    while(t < 5)
        if(!check_col_top(array, t++))
            return (0);
	return (1);
}

int check_all_col_btm(int **array)
{
    int t;

    t = 1;
    while(t < 5)
        if(!check_col_btm(array, t++))
            return (0);
	return (1);
}

int check_all_lines_right(int **array)
{
    int t;

    t = 1;
    while(t < 5)
        if(!check_line_right(array, t++))
            return (0);
	return (1);
}

int check_all_lines_left(int **array)
{
    int t;

    t = 1;
    while(t < 5)
        if(!check_line_left(array, t++))
            return (0);
	return (1);
}

int	is_valid(int **array, int l, int c, int k)
{
    int before;

	before = array[l][c];
	array[l][c] = k;
	if(!check_all_col_top(array)){
		array[l][c] = before;
		return (0);
	}
	if(!check_all_col_btm(array)){
		array[l][c] = before;
		return (0);
	}
	if(!check_all_lines_right(array)){
		array[l][c] = before;
		return (0);
	}
	if(!check_all_lines_left(array)){
		array[l][c] = before;
		return (0);
	}

	return (1);
}
