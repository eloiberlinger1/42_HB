/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/04/30 23:24:50 by eberling          #+#    #+#             */
/*   Updated: 2025/05/06 00:11:37 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	while (i < size)
	{
		j = 0;
		while (j < size - 1)
		{
			if (tab[j] > tab[j + 1])
			{
				temp = tab[j];
				tab[j] = tab[j + 1];
				tab[j + 1] = temp;
			}
			j++;
		}
		i++;
	}
}
/*
#include <stdio.h>

int main(void){

	int test[7] = {7,3,8,4,5,6,1};
	int test[7] = {3,7,8,4,5,6,1};
	//intended 1234567

	ft_sort_int_tab(test, 7);

	int i = 0;
	while(i < 7){
		printf("%d\n", test[i]);
		i++;
	}

	return 0;
}
*/
