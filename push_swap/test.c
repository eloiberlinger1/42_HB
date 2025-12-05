/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_list
{
	int				content;
	struct s_list	*next;
	struct s_list	*prev;
}					t_list;


t_list	*ft_lstnew(int content);
void	ft_lstadd_front(t_list **lst, t_list *new);
int		ft_lstsize(t_list *lst);
t_list	*ft_lstlast(t_list *lst);
void	ft_lstiter(t_list *lst, void (*f)(int));
void	ft_lstadd_back(t_list **lst, t_list *new);
void	ft_lstdelone(t_list *lst, void (*del)(int));
void	ft_lstclear(t_list **lst, void (*del)(int));
t_list	*ft_lstmap(t_list *lst, int(*f)(int), void (*del)(int));


void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list *last;

	if (!new)
		return ;
	if (!lst || !*lst)
	{
		new->prev = NULL;
		*lst = new;
		return ;
	}
	last = ft_lstlast(*lst);

	new->prev = last;
	last->next = new;
}

void    ft_lstadd_front(t_list **lst, t_list *new)
{
        if (!lst || !new)
                return ;
        new->next = *lst;
        *lst = new;
}


void    ft_lstclear(t_list **lst, void (*del)(int))
{
        t_list  *current;
        t_list  *next;

        if (!lst)
                return ;
        current = *lst;
        while (current)
        {
                next = current->next;
                ft_lstdelone(current, del);
                current = next;
        }
        *lst = NULL;
}

void    ft_lstdelone(t_list *lst, void (*del)(int))
{
        if (!lst || !del)
                return ;
        del(lst->content);
        free(lst);
}


void    ft_lstiter(t_list *lst, void (*f)(int))
{
        if (!lst || !f)
                return ;
        while (lst)
        {
                f(lst->content);
                lst = lst->next;
        }
}


t_list  *ft_lstlast(t_list *lst)
{
        if (!lst)
                return (NULL);
        while (lst->next != NULL)
                lst = lst->next;
        return (lst);
}

t_list  *ft_lstmap(t_list *lst, int(*f)(int), void (*del)(int))
{
        t_list  *new_list_head;
        t_list  *new_list;
        int             new_content;

        if (!lst || !f || !del)
                return (NULL);
        new_list_head = NULL;
        while (lst)
        {
                new_content = f(lst->content);
                new_list = ft_lstnew(new_content);
                if (!new_list)
                {
                        del(new_content);
                        ft_lstclear(&new_list_head, del);
                        return (NULL);
                }
                if (new_list_head == NULL)
                        new_list_head = new_list;
                else
                        ft_lstadd_back(&new_list_head, new_list);
                lst = lst->next;
        }
        return (new_list_head);
}

t_list  *ft_lstnew(int content)
{
        t_list  *ret;

        ret = (t_list *) malloc(sizeof(t_list));
        if (!ret)
                return (NULL);
        ret->content = content;
        ret->next = NULL;
        ret->prev = NULL;
        return (ret);
}


int     ft_lstsize(t_list *lst)
{
        int     c;

        if (!lst)
                return (0);
        c = 0;
        while (lst)
        {
                lst = lst->next;
                c++;
        }
        return (c);
}

int main()
{
    t_list *l1 = NULL;
    l1 = ft_lstnew(10);
    
    ft_lstadd_back(&l1, ft_lstnew(20));
    ft_lstadd_back(&l1, ft_lstnew(30));
    
    printf("value : %d\n", l1->next->next->prev->prev->content);

    return 0;
}