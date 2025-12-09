/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_small.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 10:47:34 by eberling          #+#    #+#             */
/*   Updated: 2025/12/10 00:19:48 by eberling         ###   ########.fr       */
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
	{
		ft_swap(current);
	}
}

static void sort_more_three_l5(t_list **a, t_list **b)
{
	t_list *smallest;
	size_t a_size;
	size_t smallest_i;

	a_size = ft_lstsize(*a);

	while (a_size > 3)
	{
		smallest = ft_lstgetmin(*a);
		smallest_i = a_size - ft_lstsize(smallest);

		printf("index du plus petit : %d\n", (int)(smallest_i));
		if (a_size == 4)
		{
			if ((smallest_i) == 1)
				ft_rotate(a);
			if ((smallest_i) == 2)
			{
				ft_rotate(a);
				ft_rotate(a);
			}
			if ((smallest_i) == 3)
				ft_rev_rotate(a);
			pb(a, b);
			sort_three_elmts(a);
			//pa(a, b);     PLANTE POURQUOI
		}
		if (a_size == 5)
		{
			if ((smallest_i) >= 2) 
			{
				ft_rev_rotate(a);
				ft_rev_rotate(a);
			}
		}
		(void)b;
		//ft_push(&smallest, b);
		a_size--;
	}
	
}

void	sort_small(t_list **a, t_list **b)
{
	size_t	list_size;

	list_size = ft_lstsize(*a);
	printf("lstsize:%d\n", ft_lstsize(*a));
	printf("lstsize:%d\n", ft_lstsize(*b));

	if (list_size <= 3)
		sort_three_elmts(a);
		
	else if (list_size > 3 && list_size <= 5)
		sort_more_three_l5(a, b);

}
