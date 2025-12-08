/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:55 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 00:16:53 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#ifndef FT_PUSH_SWAP_H
# define FT_PUSH_SWAP_H

# include "ft_printf/ft_printf.h"

void ft_swap(t_list **list);
void ft_push(t_list **l1, t_list **l2);
int check_sort(t_list *list);
void ft_rotate(t_list **lst);

#endif
