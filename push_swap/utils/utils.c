/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 11:34:56 by eberling          #+#    #+#             */
/*   Updated: 2025/12/16 11:40:23 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

int	contains(char *s, char c)
{
	while (*s)
	{
		if (*s++ == c)
			return (1);
	}
	return (0);
}

int	ft_check_dobble(t_list *list)
{
	t_list	*current;
	t_list	*runner;

	current = list;
	while (current != NULL && current->next != NULL)
	{
		runner = current->next;
		while (runner != NULL)
		{
			if (runner->content == current->content)
				return (1);
			runner = runner->next;
		}
		current = current->next;
	}
	return (0);
}
