/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pa_pb.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:18:29 by eloi              #+#    #+#             */
/*   Updated: 2025/12/08 18:18:18 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

// Take the first element at the top of b and put it at the top of a.
void ft_push(t_list **a, t_list **b)
{
    t_list *first_a;
    if (*a == NULL)
    {
        printf("a est vide pas de vleur a prendre pour mettre dans b");
        return ;
    }

    ft_lstadd_front(b, *a);
    first_a = *a;
    
    // supprimer premier elemenet de a
    *a = (*a)->next;
    (*a)->prev = NULL;
}