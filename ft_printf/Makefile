NAME = libftprintf.a
CC = cc
CFLAGS = -Wextra -Wall -Werror
DFLAGS = -g
C_FILES =  ft_printf.c ft_printhex.c ft_printchar.c ft_printnbr.c

O_FILES = $(C_FILES:.c=.o)
LIBFT_D = libft/
LIBFT_A = libft.a
LIBFT_PATH = $(LIBFT_D)$(LIBFT_A)

all: $(LIBFT_A) $(NAME)

$(LIBFT_A):
	make -C $(LIBFT_D) all
	make -C $(LIBFT_D) bonus

$(NAME) : $(O_FILES) $(LIBFT_PATH)
	cp $(LIBFT_PATH) $(NAME)
	ar rcs $(NAME) $(O_FILES)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

fclean_all: clean
	rm -f $(NAME)
	make -C $(LIBFT_D) fclean

clean:
	rm -f $(O_FILES) $(O_BONUS_FILES)
	make -C $(LIBFT_D) clean

fclean: fclean_all

re: fclean all

.PHONY : all clean fclean re fclean_all
