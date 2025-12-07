/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sa_sb_ss.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eloi <eloi@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 10:08:27 by eberling          #+#    #+#             */
/*   Updated: 2025/12/07 17:34:48 by eloi             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
    Swap the first 2 elements at the top of stack
*/
void ft_swap(t_list **list)
{
    t_list *a;
    t_list *b;
    t_list *c;

    if (*list == NULL || (*list)->next == NULL)
    {
        printf("un seul element");
        return ;
    }
    
    a = *list;
    b = a->next;
    c = b->next;
    b->prev = NULL;
    a->prev = b;
    b->next = a;
    a->next = c;
    if (c != NULL)
        c->prev = a;
}

void ft_sa(t_list **a)
{
    ft_swap(a);
}

// int ft_sb(t_list a, t_list b)
// {
    
// }

// int ft_ss(t_list a, t_list b)
// {
    
// }