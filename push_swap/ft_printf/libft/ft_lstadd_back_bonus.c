/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 21:29:34 by eberling          #+#    #+#             */
/*   Updated: 2025/12/05 15:18:39 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list *last;

	if (!new)
		return ;
	if (!lst || !*lst)
	{
		new->prev = NULL;
		*lst = new;
		return ;
	}
	last = ft_lstlast(*lst);

	new->prev = last;
	last->next = new;
}
