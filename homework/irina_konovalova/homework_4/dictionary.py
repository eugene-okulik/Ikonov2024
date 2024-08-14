# Словарь, ДЗ №4

new_dict = {tuple: (1, 3, 6, 7, None, 'text', False, 2.42), list: [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'Ира', 'Вова'], dict: {'key1':'22', 'key2':'23', 'key3':'147', 'key4':'1', 'key5':'-2'}, set: {'12', '54', 'width', 'wide', 'long', 'deep'}}
print(new_dict)
print("The names of the keys in the dictionary: ", new_dict.keys())
new_dict['tuple'] = new_dict.pop(tuple)
new_dict['list'] = new_dict.pop(list)
new_dict['dict'] = new_dict.pop(dict)
new_dict['set'] = new_dict.pop(set)
# Tuple
print("             ")
print("********** Tuple **********")
print("Elements in the 'Tuple': ", new_dict["tuple"])
my_tuple_list = new_dict["tuple"]
elements_tuple = len(my_tuple_list)
print("Last element in the 'Tuple': ", my_tuple_list[-1])   # выведите на экран последний элемент
# List
print("             ")
print("********** List **********")
print("Elements in the 'List': ", new_dict["list"])
list = new_dict["list"]
elements_list = len(list)
print("Number of elements in the 'List': ", elements_list)

list.append(input("Add an entry: "))   # добавьте в конец списка еще один элемент
print(list)
elements_list = len(list)
# print("Number of elements in the 'List': ", elements_list)
list_del = int(input("Введите цифру 2, чтобы удалить элемент №2: "))   # удалите второй элемент списка
if list_del == 2:
    del_pos_list = list[list_del-1]
    del list[list_del-1]
    print("Элемент №", list_del, ":", "'", del_pos_list, "'", " удален из списка")
else:
    print("Ввели неверный номер, элемент списка №2 не удален")
print(list)

# Dict
print("             ")
print("********** Dict **********")
print("Elements in the 'Dict': ", new_dict["dict"])
dict = new_dict["dict"]
elements_dict = len(dict)
print("Number of elements in the 'Dict': ", elements_dict)
check = 'i am a tuple'
dict[check] = " "
print("Словарь после добавления нового ключа 'i am a tuple'", dict)
getDel = str(input('Введите название ключа, который Вы хотите удалить: '))     # удалите какой-нибудь элемент
dict.pop(getDel)
print("Словарь после удаления записи: ", dict)

# Set
print("             ")
print("********** Set **********")
set = new_dict["set"]
print('Дано множество:', set)
num_set = int(input("Сколько записей Вы хотите добавить?: "))    # добавьте новый элемент в множество
for i in range(num_set):
    set.add(input("Введите число или слово: "))
print('Обновленное Множество:', set)
index_num = (input("Введите элемент, который хотите удалить: "))   # удалите элемент из множества
if index_num in set:
    set.discard(index_num)
    print("Элемент ", index_num, " удален из множества")
else:
    print("Такой элемент не найден")
print('Обновленное Множество:', set)

print("             ")
print("********** Updated dictionary **********")

print(new_dict)





