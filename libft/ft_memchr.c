/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/12 13:46:31 by eberling          #+#    #+#             */
/*   Updated: 2025/10/22 21:21:04 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *ptr, int value, size_t num)
{
	size_t			i;
	unsigned char	*nptr;

	nptr = (unsigned char *)ptr;
	i = 0;
	while (i < num && nptr[i] != (unsigned char)value)
		i++;
	if (i < num)
		return ((void *)&nptr[i]);
	return (NULL);
}
