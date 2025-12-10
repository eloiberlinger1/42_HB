/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_small.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 10:47:34 by eberling          #+#    #+#             */
/*   Updated: 2025/12/10 10:11:56 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void	sort_three_elmts(t_list **current)
{
	t_list	*elt;

	elt = *current;
	if (elt->content > elt->next->content
		&& elt->content > elt->next->next->content) // case [3, 1, 2]
		ft_rotate(current);
	else if (elt->next->content > elt->next->next->content
		&& elt->next->content > elt->content)
		ft_rev_rotate(current);
	elt = *current;
	if (elt->content > elt->next->content)
		ft_swap(current);
}

static void	sort_more_three_l5(t_list **a, t_list **b)
{
	t_list *smallest;
	size_t a_size;
	size_t smallest_i;

	while (ft_lstsize(*a) > 3)
	{
		a_size = ft_lstsize(*a);
		smallest = ft_lstgetmin(*a);
		smallest_i = a_size - ft_lstsize(smallest);
		while ((*a)->content != smallest->content)
		{
			if ((smallest_i) <= a_size / 2)
				ra(a);
			if ((smallest_i) > a_size / 2)
				rra(a);
		}
		pb(a, b);
	}
	sort_three_elmts(a);
	while (ft_lstsize(*a) <= (int)a_size)
		pa(a, b);
}

void	sort_small(t_list **a, t_list **b)
{
	size_t	list_size;

	list_size = ft_lstsize(*a);
	if (list_size <= 3)
		sort_three_elmts(a);
	else if (list_size > 3 && list_size <= 5)
		sort_more_three_l5(a, b);
}
