/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_rotate.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:25:45 by eberling          #+#    #+#             */
/*   Updated: 2025/12/10 00:16:09 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	ft_rotate(t_list **lst)
{
	t_list	*old_head;
	t_list	*tail;

	if (!lst || !*lst || !(*lst)->next)
		return ;
	tail = ft_lstlast(*lst);
	old_head = *lst;
	*lst = (*lst)->next;
	(*lst)->prev = NULL;
	tail->next = old_head;
	old_head->next = NULL;
	old_head->prev = tail;
}

void	ra(t_list **list)
{
	ft_printf("ra\n");
	ft_rotate(list);
}

void	rb(t_list **list)
{
	ft_printf("rb\n");
	ft_rotate(list);
}

void	rr(t_list **a, t_list **b)
{
	ft_printf("rr\n");
	ft_rotate(a);
	ft_rotate(b);
}
