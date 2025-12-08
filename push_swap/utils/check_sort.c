/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 10:20:48 by eberling          #+#    #+#             */
/*   Updated: 2025/12/08 23:12:26 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"


int check_sort(t_list *list)
{
    t_list  *current;
    
    current = list;
    while(current != NULL && current->next != NULL)
    {
        if (current->content > current->next->content)
            return (0);
        current = current->next;
    }
    
    return (1);
}
