/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 10:39:37 by eberling          #+#    #+#             */
/*   Updated: 2025/10/15 10:52:10 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_putchar_fd(char c, int fd)
{
	return (write(fd, &c, 1));
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
//     for (int i = 0; message[i] != '\0'; i++)
//         ft_putchar_fd(message[i], fd);
//     if (close(fd) == -1)
//     {
//         perror("Erreur lors de la fermeture du fichier");
//         return (1);
//     }
//     printf("Termine. Veuillez verifier le contenu de 'test.txt'.\n");
//     return (0);
// }