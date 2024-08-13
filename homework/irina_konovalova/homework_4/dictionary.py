# Словарь, ДЗ №4

new_dict = {tuple: (1, 3, 6, 7, 'None', 'text', 'False', 2.42), list: ['1', '3', '6', '7', 'None', 'text', 'False', '2.42', 'sdsdf', 'Таня', 'Ира', 'Аня', 'Соня', 'Вова'], dict: {'key1':'22', 'key2':'23', 'key3':'147', 'key4':'1', 'key5':'-2'}, set: {'12', '54', 'width', 'wide', 'long', 'deep'}}
print(new_dict)
print("The names of the keys in the dictionary: ", new_dict.keys())
new_dict['my_tuple'] = new_dict.pop(tuple)
new_dict['my_list'] = new_dict.pop(list)
new_dict['my_dict'] = new_dict.pop(dict)
new_dict['my_set'] = new_dict.pop(set)
# Tuple
print("             ")
print("********** Tuple **********")
print("Elements in the 'Tuple': ", new_dict["my_tuple"])
my_tuple_list = new_dict["my_tuple"]
elements_tuple = len(my_tuple_list)
print("Number of elements in the 'Tuple': ", elements_tuple)
print("Last element in the 'Tuple': ", my_tuple_list[-1])   # выведите на экран последний элемент
# List
print("             ")
print("********** List **********")
print("Elements in the 'List': ", new_dict["my_list"])
my_list = new_dict["my_list"]
elements_list = len(my_list)
print("Number of elements in the 'List': ", elements_list)

my_list.append(input("Add an entry: "))   # добавьте в конец списка еще один элемент
print(my_list)
elements_list = len(my_list)
print("Number of elements in the 'List': ", elements_list)
list_del = int(input("Введите цифру 2, чтобы удалить элемент №2: "))   # удалите второй элемент списка
if list_del == 2:
    del_pos_list = my_list[list_del-1]
    del my_list[list_del-1]
    print("Элемент №", list_del, ":", "'", del_pos_list, "'", " удален из списка")
else:
    print("Ввели неверный номер, элемент списка №2 не удален")

print(my_list)

# Dict
print("             ")
print("********** Dict **********")
print("Elements in the 'Dict': ", new_dict["my_dict"])
my_dict = new_dict["my_dict"]
elements_dict = len(my_dict)
print("Number of elements in the 'Dict': ", elements_dict)
check = 'i am a tuple'
my_dict[check] = " "
print("Словарь после добавления нового ключа 'i am a tuple'", my_dict)
getDel = str(input('Введите название ключа, который Вы хотите удалить: '))     # удалите какой-нибудь элемент
my_dict.pop(getDel)
print("Словарь после удаления записи: ", my_dict)

# Set
print("             ")
print("********** Set **********")
my_set = new_dict["my_set"]
print('Дано множество:', my_set)
num_set = int(input("Сколько записей Вы хотите добавить?: "))    # добавьте новый элемент в множество
for i in range(num_set):
    my_set.add(input("Введите число или слово: "))
print('Обновленное Множество:', my_set)
index_num = (input("Введите элемент, который хотите удалить: "))   # удалите элемент из множества
if index_num in my_set:
    my_set.discard(index_num)
    print("Элемент ", index_num, " удален из множества")
else:
    print("Такой элемент не найден")
print('Обновленное Множество:', my_set)

print("             ")
print("********** Updated dictionary **********")

print(new_dict)





