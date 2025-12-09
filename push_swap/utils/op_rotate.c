/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_rotate.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:25:45 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 21:33:18 by eberling         ###   ########.fr       */
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

void	ft_rrotate(t_list **a, t_list **b)
{
	ft_rotate(a);
	ft_rotate(b);
}

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

void	ft_rrev_rotate(t_list **a, t_list **b)
{
	ft_rev_rotate(a);
	ft_rev_rotate(b);
}
