/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 09:48:46 by eberling          #+#    #+#             */
/*   Updated: 2025/10/15 10:52:03 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	int	i;

	if (!s || !f)
		return ;
	i = 0;
	while (s[i] != '\0')
	{
		f((unsigned int) i, (char *) &s[i]);
		i++;
	}
}

// void ft_test(unsigned int i, char *c)
// {
// 	if(i == 0 || i == 1)
// 		*c = '>';
// }

// #include <stdio.h>
// int main()
// {
// 	char test[] = "   This is a testing string";

// 	ft_striteri(test, ft_test);
// 	printf("%s\n", test);
// }
