/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/12/01 09:39:38 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*ft_get_line(char *line)
{
	char	*tmp;
	int		i;

	i = 0;
	while(line[i] && line[i] != '\n')
		i++;
	if (line[i] == '\n')
		i++;
	tmp = malloc(i + 1);
	if (!tmp)
		return (NULL);
	i = 0;
	while (*line && *line != '\n')
		tmp[i++] = *line++;
	if (*line == '\n')
		tmp[i++] = *line++;
	tmp[i] = '\0';
	return (tmp);
}

static char *ft_read(char *buffer, int fd)
{
	int			read_i;
	char		*line;
	char		*tmp;

	line = ft_strjoin(buffer, "");
	if (line == NULL)
		return (NULL);
	if (contains('\n', line))
		return (line);
	read_i = read(fd, buffer, BUFFER_SIZE);
	while (read_i > 0)
	{
		buffer[read_i] = '\0';
		tmp = ft_strjoin(line, buffer);
		if (!tmp)
			return (free(line), NULL);
		free (line);
		line = tmp;
		if (contains('\n', buffer))
			return (line);
		read_i = read(fd, buffer, BUFFER_SIZE);
	}
	if (read_i == -1)
		return (free(line), NULL);
	return (line);
}

// char	*ft_strchr(const char *str, int ch)
// {
// 	char	*ret;

// 	ret = (char *)str;
// 	while (*ret != '\0')
// 	{
// 		if (*ret == (char)ch)
// 			return (ret);
// 		ret++;
// 	}
// 	if ((char)ch == '\0')
// 		return (ret);
// 	return (NULL);
// }

// static int	ft_clean_buff(char *buffer)
// {
// 	size_t	i;
// 	char	*bg;
// 	char	*end;

// 	bg = ft_strchr(buffer, '\n');
// 	if (!bg)
// 		return (buffer[0] = '\0', 0);
// 	bg++;
// 	if (*bg == '\0')
// 		return (buffer[0] = '\0', 0);
// 	end = ft_strchr(bg, '\0');
// 	if (!end)
// 		return (buffer[0] = '\0', 0);
// 	i = 0;
// 	while (bg != end)
// 		buffer[i++] = *bg++;
// 	buffer[i] = '\0';
// 	return (1);
// }

char	*get_next_line(int fd)
{
	char		buffer[BUFFER_SIZE + 1];
	char		*line;
	char		*begin;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	line = ft_read(buffer, fd);
	if (line == NULL)
		return (buffer[0] = '\0', NULL);
	begin = ft_get_line(buffer);
	free(line);
	if (begin == NULL)
		return(buffer[0] = '\0', NULL);
	//ft_clean_buff(buffer);
	if (begin[0] == '\0')
		return (free(begin), buffer[0] = '\0', NULL);
	return (begin);
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
