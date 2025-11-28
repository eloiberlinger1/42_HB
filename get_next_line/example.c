/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   example.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 09:38:42 by nluchini          #+#    #+#             */
/*   Updated: 2025/11/28 15:51:52 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*str;
	size_t	i;
	size_t	s1_len;
	size_t	s2_len;

	if (!s1 || !s2)
		return (NULL);
	s1_len = 0;
	s2_len = 0;
	while (s1[s1_len])
		s1_len++;
	while (s2[s2_len])
		s2_len++;
	i = 0;
	str = (char *)malloc(s1_len + s2_len + 1);
	if (!str)
		return (NULL);
	while (*s1)
		str[i++] = *s1++;
	while (*s2)
		str[i++] = *s2++;
	str[i] = '\0';
	return (str);
}

static char	*ft_get_line(char *line)
{
	char	*tmp;
	size_t	i;

	i = 0;
	while (line[i] && line[i] != '\n')
		i++;
	if (line[i] == '\n')
		i++;
	tmp = (char *)malloc((i + 1) * sizeof(char));
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

static char	*ft_read(char *static_buff, int fd)
{
	char	*line;
	char	*tmp;
	int		bytes_read;

	line = ft_strjoin(static_buff, "");
	if (line == NULL)
		return (NULL);
	if (ft_strchr(line, '\n') != NULL)
		return (line);
	bytes_read = read(fd, static_buff, BUFFER_SIZE);




	while (bytes_read > 0)
	{
		static_buff[bytes_read] = '\0';
		tmp = ft_strjoin(line, static_buff);
		if (!tmp)
			return (free(line), NULL);
		free(line);
		line = tmp;
		if (ft_strchr(line, '\n') != NULL)
			return (line);
		bytes_read = read(fd, static_buff, BUFFER_SIZE);
	}



	
	if (bytes_read == -1)
		return (free(line), NULL);
	return (line);
}

static int	ft_clean_buff(char *buffer)
{
	size_t	i;
	char	*bg;
	char	*end;

	bg = ft_strchr(buffer, '\n');
	if (!bg)
		return (buffer[0] = '\0', 0);
	bg++;
	if (*bg == '\0')
		return (buffer[0] = '\0', 0);
	end = ft_strchr(bg, '\0');
	if (!end)
		return (buffer[0] = '\0', 0);
	i = 0;
	while (bg != end)
		buffer[i++] = *bg++;
	buffer[i] = '\0';
	return (1);
}

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	char		*line;
	char		*res;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	line = ft_read(buffer, fd);
	if (line == NULL)
		return (buffer[0] = '\0', NULL);
	res = ft_get_line(line);
	free(line);
	if (res == NULL)
		return (buffer[0] = '\0', NULL);
	ft_clean_buff(buffer);
	if (res[0] == '\0')
	{
		free(res);
		buffer[0] = '\0';
		return (NULL);
	}
	return (res);
}

// char	*get_next_line(int fd)
// {
// 	static t_array	static_buffer;
// 	static char buffer[BUFFER_SIZE + 1];
// 	char			*line;

// 	if (fd < 0 || BUFFER_SIZE <= 0)
// 		return (NULL);
// 	if (static_buffer.data == NULL)
// 	{
// 		static_buffer.data = (char *)ft_realloc(NULL, (BUFFER_SIZE + 1));
// 		if (static_buffer.data == NULL)
// 			return (NULL);
// 		static_buffer.data[0] = '\0';
// 		static_buffer.size = 0;
// 		static_buffer.capacity = BUFFER_SIZE;
// 	}
// 	if (!ft_read_line(&static_buffer, fd))
// 		return (ft_free_buff(&static_buffer));
// 	line = ft_get_line(&static_buffer);
// 	if (line == NULL)
// 		return (ft_free_buff(&static_buffer));
// 	if (line[0] == '\0')
// 		return (free(line), ft_free_buff(&static_buffer));
// 	return (line);
// }

// #include <fcntl.h>
// #include <limits.h>
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <unistd.h>

// void	gnl(int fd, char *expected)
// {
// 	char	*line;

// 	line = get_next_line(fd);
// 	if (line == NULL && expected == NULL)
// 		printf("Test passed: got NULL as expected\n");
// 	else if (line != NULL && expected != NULL && strcmp(line, expected) == 0)
// 		printf("Test passed: got '%s' as expected\n", line);
// 	else
// 		printf("Test failed: got '%s', expected '%s'\n", line ? line : "NULL",
// 			expected ? expected : "NULL");
// 	free(line);
// }

// int	main(void)
// {

// 	int fd = open("multiple_nl.txt", O_RDONLY);
// 	/* 1 */ gnl(fd, "\n");
// 	/* 2 */ gnl(fd, "\n");
// 	/* 3 */ gnl(fd, "\n");
// 	/* 4 */ gnl(fd, "\n");
// 	/* 5 */ gnl(fd, "\n");
// 	/* 6 */ gnl(fd, NULL);
// 	close(fd);
// }
