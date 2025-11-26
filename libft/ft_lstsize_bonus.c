/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 14:57:22 by eberling          #+#    #+#             */
/*   Updated: 2025/10/16 15:59:43 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	c;

	if (!lst)
		return (0);
	c = 0;
	while (lst)
	{
		lst = lst->next;
		c++;
	}
	return (c);
}

// #include <stdio.h>
// int main()
// {
//     t_list *list_head = NULL;
//     t_list *node1 = ft_lstnew("Premier"); 
//     t_list *node2 = ft_lstnew("Second");
//     ft_lstadd_front(&list_head, node2);
//     ft_lstadd_front(&list_head, node1);
//     printf("%d\n", ft_lstsize(node1));
// }