/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   display_array.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/10 12:41:46 by eberling          #+#    #+#             */
/*   Updated: 2025/05/11 18:45:14 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

void	ft_putchar(char c);

void	display_array(int **array)
{
	int	l;
	int	c;

	l = 0;
	while (l < 6)
	{
		c = 0;
		while (c < 6)
		{
			ft_putchar(array[l][c] + '0');
			ft_putchar(' ');
			c++;
		}
		ft_putchar('\n');
		l++;
	}
}