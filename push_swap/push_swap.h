/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:55 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 11:15:51 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#ifndef FT_PUSH_SWAP_H
# define FT_PUSH_SWAP_H

# include "ft_printf/ft_printf.h"

int check_sort(t_list *list);

void ft_swap(t_list **list);
void ft_sswap(t_list **a, t_list **b);

void ft_push(t_list **l1, t_list **l2);

void ft_rotate(t_list **lst);
void    ft_rrotate(t_list **a, t_list **b);
void ft_rev_rotate(t_list **lst);
void ft_rrev_rotate(t_list **a, t_list **b);

void    sort_small(t_list **a, t_list **b);


#endif
