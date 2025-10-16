/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 14:57:22 by eberling          #+#    #+#             */
/*   Updated: 2025/10/15 15:33:50 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
    int c;

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
//     t_list *node1 = ft_lstnew("Premier"); // node1 devient le 2ème après l'ajout
//     t_list *node2 = ft_lstnew("Second");  // node2 devient le 1er après l'ajout
//     ft_lstadd_front(&list_head, node2);
//     ft_lstadd_front(&list_head, node1);
//     printf("%d\n", ft_lstsize(node1));
// }