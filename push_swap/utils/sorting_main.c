/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_main.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 09:32:29 by eberling          #+#    #+#             */
/*   Updated: 2025/12/12 15:30:08 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
(TO CHECK )

In a mathematical point of view for Radix sorting K represent the number of pass needed to get a sorted list
this value is related to the number of bits of the index of the biggest element of the list

because we make binary pass

*/
int get_K(t_list **a)
{
	int	k;
	int	K;

	k = ft_lstgetmax(*a)->index;
	K = 0;
	while (k > 0)
	{
		k = k >> 1;
		K++;
		printf(
			"sadasd"
		);
	}
	return (K);
}

void radix_sort(t_list **a, t_list **b)
{
	(void)b;
	
	printf("\n\nK = %d\n\n", get_K(a));
}

void	sort_main(t_list **a, t_list **b)
{
	t_list	*current;

	(void)b;

	if (ft_lstsize(*a) > 5)
	{
		current = *a;

		radix_sort(&current, b);
	}
}
