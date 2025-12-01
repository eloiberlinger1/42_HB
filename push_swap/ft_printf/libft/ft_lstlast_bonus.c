/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 15:35:03 by eberling          #+#    #+#             */
/*   Updated: 2025/10/16 15:58:12 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next != NULL)
		lst = lst->next;
	return (lst);
}

// #include <stdio.h>
// int main()
// {
//     t_list *list_head = NULL;
//     t_list *node1 = ft_lstnew("Premier");
//     t_list *node2 = ft_lstnew("Second");
//     ft_lstadd_front(&list_head, node2);
//     ft_lstadd_front(&list_head, node1);
// 	// pouruquoi pas possible de voir le contenu de l'element
//     t_list *result = ft_lstlast(node2);
//     printf("%s\n", (char*)result->content);
// }