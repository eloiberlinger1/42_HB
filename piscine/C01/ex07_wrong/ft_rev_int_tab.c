/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/04/30 23:05:00 by eberling          #+#    #+#             */
/*   Updated: 2025/05/03 21:20:02 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_rev_int_tab(int *tab, int size)
{
	int	*first;
	int	*last;
	int	temp;

	first = tab;
	last = tab + size - 1;
	while (first < last)
	{
		temp = *first;
		*first = *last;
		*last = temp;
		first++;
		last--;
	}
}

int main() {

	int array[] = {1, 2000, 3, 4, 550, 1, 2000, 3};

	ft_rev_int_tab(array, 5);


	int i = 0;

	while (i < 5) {

		printf("%d ", array[i]);
		i++;
	}


	return 0;
}
