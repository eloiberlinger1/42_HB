/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 08:55:18 by eberling          #+#    #+#             */
/*   Updated: 2025/05/15 08:55:19 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	i;
	int	*result;

	if (min >= max)
		return (NULL);
	i = 0;
	result = malloc(sizeof(int) * (max - min));
	while (i < (max - min))
	{
		result[i] = min + i;
		i++;
	}
	return (result);
}

/* #include <stdio.h>
int main(void)
{
	int i = 0;
	int *array = ft_range(50, 100);

	while (i <= 50)
		printf("%d \n", array[i++]);
	
	return 0;
}
 */