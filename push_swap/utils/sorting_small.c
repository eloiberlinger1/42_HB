/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_small.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 10:47:34 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 12:57:04 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void sort_three_elmts(t_list *current)
{
    if (current->content > current->next->content && current->content > current->next->next->content) //case [3, 1, 2]
        ft_rotate(&current);
    else if(current->next->content > current->next->next->content && current->next->content > current->content)
        ft_rev_rotate(&current);
    
    if(current->content > current->next->content)
    {
        ft_swap(&current);
    }
}

void    sort_small(t_list **a, t_list **b)
{
    t_list *current;
    printf("lstsize:%d\n", ft_lstsize(*a));
    printf("lstsize:%d\n", ft_lstsize(*b));

    current = *a;
    if (ft_lstsize(*a) == 3)
    {
        sort_three_elmts(current);
    }
    else
    {
        while (current != NULL && current->next != NULL)
        {
            if (current->content > current->next->content)
            {
                break ;
            }
            current = current->next;
        }
        
    }    
}