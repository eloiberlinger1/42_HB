/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/12 18:26:28 by eberling          #+#    #+#             */
/*   Updated: 2025/05/12 20:41:56 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_factorial(int nb)
{
	if (nb == 0)
		return (1);
	if (nb < 0)
		return (0);
	if (nb == 1)
		return (nb);
	else
		return (nb * ft_recursive_factorial(nb - 1));
}
/* 

#include <stdio.h>
int main(void){
	printf("%d \n", ft_recursive_factorial(5));
} */