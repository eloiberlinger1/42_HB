/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_array.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/10 23:30:34 by eberling          #+#    #+#             */
/*   Updated: 2025/05/11 18:44:54 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int		ft_strlen(char *str);
void	ft_putchar(char c);

int	**gen_array(void)
{
	int	**array;
	int	i;

	array = (int **) malloc(6 * 24);
	i = 0;
	while (i < 6)
	{
		array[i] = (int *) malloc(6 * 4);
		++i;
	}

	return (array);
}

int	**get_2d_array(int *array)
{
	int	**resultarr;
	int	l;
	int	c;

	l = 0;
	resultarr = gen_array();
	while (l < 6)
	{
		c = 0;
		while (c < 6)
		{
			if (l == 0 && (c > 0 && c < 6 - 1))
				resultarr[l][c] = array[c - 1];
			if (l == 6 - 1 && (c > 0 && c < 6 - 1))
				resultarr[l][c] = array[c + 3];
			if (c == 0 && (l > 0 && l < 6 - 1))
				resultarr[l][c] = array[l + 7];
			if (c == 6 - 1 && (l > 0 && l < 6 - 1))
				resultarr[l][c] = array[l + 11];
			c++;
		}
		l++;
	}
	return (resultarr);
}

int	*convert_to_int(char *str)
{
	int	i;
	int	j;
	int	*numbers;
	int	str_size;

	i = 0;
	j = 0;
	numbers = (int *) malloc(100);
	str_size = ft_strlen(str);

	while (i < str_size)
	{
		if (str[i] >= '1' && str[i] <= '4')
		{
			numbers[j] = str[i] - '0';
			j++;
		}
		i++;
	}

	return (numbers);
}

int	**get_array(char *str)
{
	int	*array1d;
	int	**array2d;

	array1d = convert_to_int(str);
	array2d = get_2d_array(array1d);

	return (array2d);
}
