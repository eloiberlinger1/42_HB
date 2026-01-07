# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

void putstr(char *str)
{
	int i = 0;
	while(str[i])
		write (1, &str[i++], 1);
}

int wordcount(char *str)
{
	int i = 0;
	int inword = 0;
	int count = 0;

	while (str[i])
	{
		if (str[i] == ' ' || str[i] == '\t')
		{
			if (inword == 1)
			{
				inword = 0;
				count ++;
			}
		}
		else
		{
			inword = 1;
		}
		i++;
	}
	if (inword == 1)
		return (count + 1);
	return (count);
}

int getwordsize(int index, char *str)
{
	int i =0;
	while (str[index + i] != ' ' && str[index + i] != '\t' && str[i + index])
		i++;
	return (i);
}

void rotstring(char *str)
{
	int i = 0;
	int j = 0;
	int k = 0;
	int words_count = wordcount(str);
	char **words_list = malloc(words_count * sizeof(char *));
	char *word;
	int wordsize;

	while (str[i])
	{
		wordsize = getwordsize(i, str);
		if (wordsize == 0)
		{
			i++;
			continue;
		}

		if (str[i] != ' ' && str[i] != '\t')
		{
			j = 0;
			word = malloc(wordsize + 1);
			while (j < wordsize)
			{
				word[j++] = str[i++];
			}
			word[j] = '\0';
			words_list[k++] = word;
		}
		else
		{
			i++;
		}

	}
	i = 1;

	while (i < words_count)
	{
		putstr(words_list[i]);
		putstr(" ");
		free(words_list[i]);
		i++;
	}

	putstr(words_list[0]);
	free(words_list[0]);
	free(words_list);

}


int main(int argc, char **argv)
{

	if (argc > 1)
	{
		rotstring(argv[1]);
	}

}
