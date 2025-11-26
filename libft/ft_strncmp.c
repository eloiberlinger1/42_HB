/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/12 13:08:04 by eberling          #+#    #+#             */
/*   Updated: 2025/10/17 18:22:25 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *str1, const char *str2, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n && (str1[i] || str2[i]))
	{
		if ((unsigned char)str1[i] != (unsigned char)str2[i])
			return ((unsigned char)str1[i] - (unsigned char)str2[i]);
		i++;
	}
	return (0);
}
// #include <stdio.h>
// #include <string.h>
// int main() {
//     const char *s1 = "applesauce";
//     const char *s2 = "apple";
//     int result1 = strncmp(s1, s2, 5);
//     int result2 = strncmp(s1, s2, 6);
// 	printf("%d\n", result1);
// 	printf("%d\n", result2);
//     return 0;
// }