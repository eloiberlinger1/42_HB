/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_main.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 09:32:29 by eberling          #+#    #+#             */
/*   Updated: 2025/12/12 17:42:06 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
(TO CHECK )

In a mathematical point of view for Radix sorting K represent
the number of pass needed to get a sorted list
this value is related to the value of the max index so depend on
the number of elements on the list.
*/
static int	get_k(t_list **a)
{
	int	k;
	int	bk;

	k = ft_lstgetmax(*a)->index;
	bk = 0;
	while (k > 0)
	{
		k = k >> 1;
		bk++;
	}
	return (bk);
}

void	radix_sort(t_list **a, t_list **b)
{
	int	k;
	int	n;
	int	k_i;
	int	n_i;

	k_i = 0;
	k = get_k(a);
	n = ft_lstsize(*a);
	while (k_i < k)
	{
		n_i = 0;
		while (n_i < n)
		{
			if (((((*a)->index >> k_i)) & 1) == 0)
				pb(a, b);
			else
				ra(a);
			n_i++;
		}
		while (*b)
			pa(a, b);
		k_i++;
	}
}

void	sort_main(t_list **a, t_list **b)
{
	(void)b;
	if (ft_lstsize(*a) > 5)
	{
		radix_sort(a, b);
	}
}
