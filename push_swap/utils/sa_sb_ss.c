/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sa_sb_ss.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 10:08:27 by eberling          #+#    #+#             */
/*   Updated: 2025/12/05 11:29:38 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
    Swap the first 2 elements at the top of stack
*/
void ft_swap(t_list **list)
{
    int i;
    t_list *first;
    t_list *second;

    i = 0;
    if (*list == NULL || (*list)->next == NULL)// WRONG CONDITION TO BE CORRECTED
    {
        printf("un seul element");
        return ;
    }
    
    first = *list;
    second = (*list)->next;
    second = first;
    first = second;
    second->prev = first;
    first->next = second;
}

void ft_sa(t_list **a)
{
    ft_swap(&a);

}

// int ft_sb(t_list a, t_list b)
// {
    
// }

// int ft_ss(t_list a, t_list b)
// {
    
// }