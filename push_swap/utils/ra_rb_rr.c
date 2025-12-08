/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ra_rb_rr.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:25:45 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 00:15:53 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void ft_rotate(t_list **lst)
{
    t_list *old_head;
    t_list *tail;

    if (!lst || !*lst)
        return ;

    tail = ft_lstlast(*lst);
    old_head = *lst;
    *lst = (*lst)->next;
    (*lst)->prev = NULL;
    tail->next = old_head;
    old_head->next = NULL;
    old_head->prev = tail;
    
//    1 2 3 4 5

//    5 1 2 3 4
}
