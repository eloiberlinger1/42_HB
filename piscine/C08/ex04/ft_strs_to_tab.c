/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strs_to_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 13:51:18 by eberling          #+#    #+#             */
/*   Updated: 2025/05/21 21:39:35 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "ft_stock_str.h"
#include "../ex05/ft_show_tab.c"

int	ft_strlen(char *str)
{
	int	i;
	int	counter;

	counter = 0;
	i = 0;
	while (str[i] != '\0')
	{
		counter++;
		i++;
	}
	return (counter);
}

char	*ft_strdup(char *src)
{
	int		size;
	int		i;
	char	*ptr;

	size = ft_strlen(src);
	ptr = (char *) malloc(size * sizeof(char) + 1);
	if (ptr == NULL)
		return (NULL);
	i = 0;
	while (src[i] != '\0')
	{
		ptr[i] = src[i];
		i++;
	}
	ptr[i] = '\0';
	return (ptr);
}

struct s_stock_str	*ft_strs_to_tab(int ac, char **av)
{
	struct s_stock_str	*elements;
	int					i;

	if (ac < 0)
		ac = 0;
	elements = (t_stock_str *) malloc(sizeof(t_stock_str) * (ac + 1));
	if (elements == NULL)
		return (NULL);
	i = 0;
	while (i < ac)
	{
		elements[i].size = ft_strlen(av[i]);
		elements[i].str = ft_strdup(av[i]);
		elements[i].copy = ft_strdup(av[i]);
		if (elements[i].str == NULL || elements[i].copy == NULL)
			return (NULL);
		i++;
	}
	elements[i].str = NULL;
	return (elements);
}
int	main(int argc,char *argv[])
{
	ft_show_tab(ft_strs_to_tab(argc, argv));
}
