/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 09:37:49 by eberling          #+#    #+#             */
/*   Updated: 2025/11/11 12:50:36 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	contains(char c, char *set)
{
	if (set == NULL)
        return (0);
	while (*set)
		if (c == *set++)
			return (1);
	return (0);
}

int	ft_strlen(const char *s)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
		i++;
	return (i);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	s1_len;
	size_t	s2_len;
	size_t	i;
	size_t	i_ret;
	char	*ret;

	s1_len = ft_strlen(s1);
	s2_len = ft_strlen(s2);
	ret = malloc(((s1_len + s2_len) + 1) * sizeof(char));
	if (ret == NULL)
		return (NULL);
	i = -1;
	while (++i < s1_len)
		ret[i] = s1[i];
	i_ret = i;
	i = -1;
	while (++i < s2_len)
		ret[i_ret + i] = s2[i];
	ret[i_ret + i] = '\0';
	return (ret);
}

char	*get_remainder(char *line)
{
	int		i;
	char	*rest;
	char	*ptr;

	ptr = line;
	i = 0;
	while (*ptr != '\n' && *ptr != '\0')
		ptr++;
	if (*ptr == '\0')
		return (NULL);
	ptr++;	
	rest = malloc(ft_strlen(ptr) + 1);
	while (ptr[i] != '\0')
	{
		rest[i] = ptr[i];
		i++;
	}
	rest[i] = '\0';
	return (rest);
}

char	*ft_cut_line(char *result)
{
	int		i;
	int		len;
	char	*line;

	i = 0;
	while(result[i] != '\n' && result[i] != '\0')
		i++;
	len = i;
	if(result[i] == '\n')
		len++;
	line = malloc(len + 1);
	i = 0;
	while (result[i] != '\n')
	{
		line[i] = result[i];
		i++;
	}
	line[i] = '\0';
	return (line);
}


char	*get_next_line(int fd)
{
	static char		*result;
	int				read_i;
	char			buffer[BUFFER_SIZE + 1];
	char			*tmp;
	char			*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	read_i = 1;
	if (result == NULL)
    {
        result = malloc(1);
        if (result == NULL)
            return (NULL);
		result[0] = '\0';
    }
	while ((result == NULL || !contains('\n', result)) && read_i > 0)
	{
		read_i = read(fd, buffer, BUFFER_SIZE);
		if (read_i == -1)
		{
			free(result);
			result = NULL;
			return (NULL);
		}
		buffer[read_i] = '\0';
		tmp = result;
		result = ft_strjoin(tmp, buffer);
		free(tmp);
	}
	if (read_i == -1)
		return (NULL);
	tmp = result;
	line = ft_cut_line(result);
	result = get_remainder(tmp);
	free(tmp);
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