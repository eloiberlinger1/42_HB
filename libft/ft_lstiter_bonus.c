/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/16 15:15:56 by eberling          #+#    #+#             */
/*   Updated: 2025/10/16 15:52:09 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!lst || !f)
		return ;
	while (lst)
	{
		f(lst->content);
		lst = lst->next;
	}
}

// #include <stdio.h>
// void test(void *c)
// {
// 	printf("-> NODE content = %s\n", (char *)c);
// }

// int main()
// {
// 	t_list *node1 = ft_lstnew("BONJOUR1");
// 	ft_lstadd_back(&node1, ft_lstnew("BONJOUR2"));
// 	ft_lstadd_back(&node1, ft_lstnew("BONJOUR3"));

// 	ft_lstiter(node1, test);
// }