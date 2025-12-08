/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pa_pb.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/08 09:18:29 by eloi              #+#    #+#             */
/*   Updated: 2025/12/08 09:25:11 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

void ft_push(t_list **l1, t_list **l2)
{
    t_list  *temp;

    temp = ft_lstlast(*l2);
    temp = ft_lstlast(*l1);

    //check if b is not empty

    printf("t1 last value = %d\n", temp->content);
}