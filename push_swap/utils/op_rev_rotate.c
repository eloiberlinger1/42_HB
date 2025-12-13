/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_rotate.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 00:14:48 by eberling          #+#    #+#             */
/*   Updated: 2025/12/10 00:15:36 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	ft_rev_rotate(t_list **lst)
{
	t_list	*old_head;
	t_list	*tail;

	if (!lst || !*lst || !(*lst)->next)
		return ;
	tail = ft_lstlast(*lst);
	tail->prev->next = NULL;
	old_head = *lst;
	*lst = tail;
	(*lst)->prev = NULL;
	(*lst)->next = old_head;
	old_head->prev = (*lst);
}

void	rra(t_list **list)
{
	ft_printf("rra\n");
	ft_rev_rotate(list);
}

void	rrb(t_list **list)
{
	ft_printf("rrb\n");
	ft_rev_rotate(list);
}

void	rrr(t_list **a, t_list **b)
{
	ft_printf("rrr\n");
	ft_rev_rotate(a);
	ft_rev_rotate(b);
}
