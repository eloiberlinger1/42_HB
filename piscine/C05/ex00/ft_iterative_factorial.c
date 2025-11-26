/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/09 10:51:54 by eberling          #+#    #+#             */
/*   Updated: 2025/05/12 19:21:40 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	i;
	int	tt;

	if (nb < 0)
		return (0);
	tt = 1;
	i = 1;
	while (i <= nb)
		tt *= (i++);
	return (tt);
}
/* #include <stdio.h>

int main(){
	printf("%d\n", ft_iterative_factorial(5));
} */