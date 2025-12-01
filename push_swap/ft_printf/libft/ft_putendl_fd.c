/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 10:58:51 by eberling          #+#    #+#             */
/*   Updated: 2025/10/15 11:18:25 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putendl_fd(char *s, int fd)
{
	while (*s)
		write(fd, s++, 1);
	write(fd, "\n", 1);
}
// #include <fcntl.h>  
// #include <stdio.h>
// int main(void)
// {
//     int fd;
//     char *message = "Bravo, c'est ecrit dans le fichier !";
//     fd = open("test.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
//     if (fd == -1)
//     {
//         perror("Erreur lors de l'ouverture du fichier");
//         return (1);
//     }
//     printf("Debut de l'ecriture dans test.txt (FD: %d)...\n", fd);
//     ft_putendl_fd(message, fd);
//     if (close(fd) == -1)
//     {
//         perror("Erreur lors de la fermeture du fichier");
//         return (1);
//     }
//     printf("Termine. Veuillez verifier le contenu de 'test.txt'.\n");
//     return (0);
// }