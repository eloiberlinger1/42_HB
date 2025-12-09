/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_small.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 10:47:34 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 21:09:10 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void sort_three_elmts(t_list **current)
{
    t_list *elt;

    elt = *current;
    if (elt->content > elt->next->content && elt->content > elt->next->next->content) //case [3, 1, 2]
        ft_rotate(current);
    else if(elt->next->content > elt->next->next->content && elt->next->content > elt->content)
        ft_rev_rotate(current);

    elt = *current;

    if(elt->content > elt->next->content)
    {
        ft_swap(current);
    }
}

void    sort_small(t_list **a, t_list **b)
{
    printf("lstsize:%d\n", ft_lstsize(*a));
    printf("lstsize:%d\n", ft_lstsize(*b));

    if (ft_lstsize(*a) <= 3)
    {
        sort_three_elmts(a);
    }
    else
    {
        // while (current != NULL && current->next != NULL)
        // {
        //     if (current->content > current->next->content)
        //     {
        //         break ;
        //     }
        //     current = current->next;
        // }
        
    }
}
