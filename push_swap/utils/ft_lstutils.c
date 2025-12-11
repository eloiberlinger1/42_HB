/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstutils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 21:52:46 by eberling          #+#    #+#             */
/*   Updated: 2025/12/11 10:23:16 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

t_list  *ft_lstgetmin(t_list *list)
{
    int min;
    t_list *current;
    t_list *smallest;

    if (!list)
        return (NULL);

    current = list;
    min = current->content;
    smallest = current;
    while (current != NULL)
    {
        if(current->content < min)
        {
            min = current->content;
            smallest = current;
        }
        current = current->next;
    }
    return (smallest);
}
