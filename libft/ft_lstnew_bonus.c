/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 13:49:17 by eberling          #+#    #+#             */
/*   Updated: 2025/10/15 15:07:51 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list *ret;
	
	ret = (t_list *) malloc(sizeof(t_list));
	if(!ret)
		return (NULL);
	ret->content = ft_strdup(content);
	if(!ret->content)
	{
		free(ret);
		return (NULL);
	}
	ret->next = NULL;
	return (ret);
}

// #include <stdio.h>
// int main()
// {
// 	t_list *test = ft_lstnew("Bonjouge");
// 	printf("%s\n", (char *)test->content);
// }