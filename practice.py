your_list = []

l1 = int(input("enter you 1st number"))
l2 = int(input("enter you 2st number"))
l3 = int(input("enter you 3st number"))
l4 = int(input("enter you 4st number"))
l5 = int(input("enter you 5st number"))

your_list.append(l1)
your_list.append(l2)
your_list.append(l3)
your_list.append(l4)
your_list.append(l5)

copy_list=your_list.copy()
copy_list.reverse()

if your_list==copy_list:
    print("your list is pallindrom")
else:
    print(" your list is not pallindrom")

