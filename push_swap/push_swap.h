/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:55 by eberling          #+#    #+#             */
/*   Updated: 2025/12/12 18:34:00 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "ft_printf/ft_printf.h"

t_list *parse_main(int argc, char **argv);
int		check_sort(t_list *list);
t_list	*ft_lstgetmax(t_list *list);
t_list  *ft_lstgetmin(t_list *list);

void	ft_swap(t_list **list);
void	sa(t_list **list);
void	sb(t_list **list);
void	ss(t_list **a, t_list **b);

void	ft_push(t_list **l1, t_list **l2);
void	pa(t_list **a, t_list **b);
void	pb(t_list **a, t_list **b);

void	ft_rotate(t_list **lst);
void	ra(t_list **list);
void	rb(t_list **list);
void	rr(t_list **a, t_list **b);

void	ft_rev_rotate(t_list **lst);
void	rra(t_list **list);
void	rrb(t_list **list);
void	rrr(t_list **a, t_list **b);

void	sort_small(t_list **a, t_list **b);
void	sort_main(t_list **a, t_list **b);
void    lst_affect_index(t_list *list);


#endif