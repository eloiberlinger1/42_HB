/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 14:35:30 by eberling          #+#    #+#             */
/*   Updated: 2025/12/05 15:31:04 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	t_list *current;

	if (!lst || !new)
		return ;

	if (*lst == NULL)
	{
		new->next = NULL;
        new->prev = NULL;
	}
	else
	{
		current = *lst;
		new->next = current;
		current->prev = new;
		new->prev = NULL;
	}
	*lst = new;
}
