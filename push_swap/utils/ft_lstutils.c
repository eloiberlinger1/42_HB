/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstutils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 21:52:46 by eberling          #+#    #+#             */
/*   Updated: 2025/12/12 12:45:30 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void	lst_affect_index(t_list *list)
{
	t_list	*current;
	t_list	*runner;
	int		rank_index;

	if (!list)
		return ;
	current = list;
	while (current != NULL)
	{
		rank_index = 0;
		runner = list;
		while (runner != NULL)
		{
			if (runner->content < current->content)
				rank_index++;
			runner = runner->next;
		}
		current->index = rank_index;
		current = current->next;
	}
}

t_list	*ft_lstgetmin(t_list *list)
{
	int		min;
	t_list	*current;
	t_list	*smallest;

	if (!list)
		return (NULL);
	current = list;
	min = current->content;
	smallest = current;
	while (current != NULL)
	{
		if (current->content < min)
		{
			min = current->content;
			smallest = current;
		}
		current = current->next;
	}
	return (smallest);
}

t_list	*ft_lstgetmax(t_list *list)
{
	int		max;
	t_list	*current;
	t_list	*biggest;

	if (!list)
		return (NULL);
	current = list;
	max = current->content;
	biggest = current;
	while (current != NULL)
	{
		if (current->content > max)
		{
			max = current->content;
			biggest = current;
		}
		current = current->next;
	}
	return (biggest);
}
