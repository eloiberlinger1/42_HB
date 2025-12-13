/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 10:08:27 by eberling          #+#    #+#             */
/*   Updated: 2025/12/10 00:08:38 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
	Swap the first 2 elements at the top of stack
*/
void	ft_swap(t_list **list)
{
	t_list	*a;
	t_list	*b;
	t_list	*c;

	if (*list == NULL || (*list)->next == NULL)
	{
		printf("un seul element");
		return ;
	}
	a = *list;
	b = a->next;
	c = b->next;
	b->prev = NULL;
	b->next = a;
	a->prev = b;
	a->next = c;
	if (c != NULL)
		c->prev = a;
	*list = b;
}

void	sa(t_list **list)
{
	ft_printf("sa\n");
	ft_swap(list);
}

void	sb(t_list **list)
{
	ft_printf("sb\n");
	ft_swap(list);
}

void	ss(t_list **a, t_list **b)
{
	ft_printf("ss\n");
	ft_swap(a);
	ft_swap(b);
}
