def ft_count_harvest_recursive():

    days = int(input("Days until harvest: "))

    def counter(i):
        if (i not in range(1, days + 1)):
            print("Harvest time!")
            return
        else:
            print(f"Day {str(i)}")
            counter(i + 1)

    counter(1)
