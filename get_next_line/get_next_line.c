/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/28 15:42:20 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*get_line(char *line)
{
	char	*tmp;
	int		i;

	i = 0;
	while(line[i] && line[i] != '\n')
		i++;
	if (line[i] == '\n')
		i++;
	tmp = malloc(1);
	// a finir
}

static char *ft_read(char *buffer, int fd)
{
	int			read_i;
	char		*line;
	char		*tmp;

	read_i = 1;
	line = ft_strjoin(buffer, "");
	if (line == NULL)
		return (NULL);
	while (read_i > 0)
	{
		tmp = ft_strjoin(line, buffer);
		if (tmp == NULL)
			return (NULL);
		free (line);
		line = tmp;

		read_i = read(fd, buffer, BUFFER_SIZE);
		buffer[read_i] = '\0';

		if (contains('\n', buffer))
			return (line);
		
	}
	if (read_i == -1)
		return (free(line), NULL);
	return (line);
}

char	*get_next_line(int fd)
{
	char		buffer[BUFFER_SIZE + 1];
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);

	line = ft_read(buffer, fd)

	return (line);
}

int	main(void)
{
	int fd;
	fd = open("test.txt", O_RDONLY);

	if (fd == -1)
	{
		perror("Erreur lors de l'ouverture du fichier");
		return (1);
	}
	printf("\ngetnextlien result1 : \n\n%s\n\n", get_next_line(fd));
	printf("\ngetnextlien result2 : \n\n%s\n\n", get_next_line(fd));
	if (close(fd) == -1)
	{
		perror("Erreur lors de la fermeture du fichier");
		return (1);
	}
	printf("Termine.\n");
	return (0);
}
