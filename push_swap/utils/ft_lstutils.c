/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstutils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 21:52:46 by eberling          #+#    #+#             */
/*   Updated: 2025/12/11 16:31:36 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void    lst_affect_index(t_list *list)
{
    t_list  *current;
    t_list  *runner;
    int  counter;

    if (!list)
        return ;

    current = list;
    counter = 0;
    while(current != NULL && current->next != NULL)
    {
        runner = list;
        while (runner != NULL)
        {
            if (current->content < runner->content)
                current->index = counter++;
            else
                runner->index = counter++;
            runner = runner->next;
        }
        current = current->next;
    }
}

t_list	*ft_lstgetmin(t_list *list)
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
