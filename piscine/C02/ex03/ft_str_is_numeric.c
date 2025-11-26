/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/01 18:46:10 by eberling          #+#    #+#             */
/*   Updated: 2025/05/04 21:46:25 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_numeric(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < '0' || str[i] > '9')
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

	char teststr[] = "+";
	int isalpha;

	isalpha = 0;
	
	isalpha = ft_str_is_numeric(teststr);

	printf("\n%d", isalpha);
}
*/