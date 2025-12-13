/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_push.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:18:29 by eloi              #+#    #+#             */
/*   Updated: 2025/12/10 09:45:03 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
Take the first element at the top of b and put it at the top of a.
*/
void	ft_push(t_list **a, t_list **b)
{
	t_list	*first_a;

	if (*a == NULL)
	{
		printf("a est vide pas de vleur a prendre pour mettre dans b");
		return ;
	}
	first_a = *a;
	*a = (*a)->next;
	if (*a != NULL)
		(*a)->prev = NULL;
	ft_lstadd_front(b, first_a);
}

void	pa(t_list **a, t_list **b)
{
	ft_printf("pa\n");
	ft_push(b, a);
}

void	pb(t_list **a, t_list **b)
{
	ft_printf("pb\n");
	ft_push(a, b);
}
