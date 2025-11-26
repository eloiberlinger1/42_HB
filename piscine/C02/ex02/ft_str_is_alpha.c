/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 14:36:28 by eberling          #+#    #+#             */
/*   Updated: 2025/05/07 10:05:02 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_alpha(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 'A' || str[i] > 'z')
		{
			return (0);
		}
		else if (str[i] > 'Z' && str[i] < 'a')
		{
			return (0);
		}
		i++;
	}
	return (1);
}

/*
#include <stdio.h>

int main(void){

	char teststr[] = "boSDA.Sur";
	int isalpha;

	isalpha = 0;
	
	isalpha = ft_str_is_alpha(teststr);

	printf("\n%d", isalpha);
}
*/