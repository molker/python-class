# Exercise

class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList()
print(len(super_list))
# Just by inherting list, you can use the functions native to it
super_list.append(5)
print(super_list[0])
print(issubclass(SuperList, list))