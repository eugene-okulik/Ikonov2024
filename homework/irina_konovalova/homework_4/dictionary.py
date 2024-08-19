# Словарь, ДЗ №4

new_dict = {tuple: (1, 3, 6, 7, None, 'text', False, 2.42), list: [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'Ира', 'Вова'], dict: {'key1': '22', 'key2': '23', 'key3': '147', 'key4': '1', 'key5': '-2'}, set: {'12', '54', 'width', 'wide', 'long', 'deep'}}
print(new_dict)
print("The names of the keys in the dictionary: ", new_dict.keys())
new_dict['tuple'] = new_dict.pop(tuple)
new_dict['list'] = new_dict.pop(list)
new_dict['dict'] = new_dict.pop(dict)
new_dict['set'] = new_dict.pop(set)
# Tuple
print("             ")
print("********** Tuple **********")
my_tuple_list = new_dict["tuple"]
elements_tuple = len(my_tuple_list)
print(my_tuple_list[-1])   # выведите на экран последний элемент

# List
print("             ")
print("********** List **********")
list = new_dict["list"]
elements_list = len(list)
list.append("aaa")   # добавьте в конец списка еще один элемент
print(list)
list_del = 2   # удалите второй элемент списка
if list_del == 2:
    del_pos_list = list[list_del - 1]
    del list[list_del - 1]
print(list)

# Dict
print("             ")
print("********** Dict **********")
print(new_dict["dict"])
dict = new_dict["dict"]
check = 'i am a tuple'
dict[check] = " "
print("Добавлен ключ 'i am a tuple': ", dict)
getDel = "key4"     # удалите какой-нибудь элемент
dict.pop(getDel)
print("Удален один элемент ", dict)

# Set
print("             ")
print("********** Set **********")
set = new_dict["set"]
num_set = int(1)    # добавьте новый элемент в множество
for i in range(num_set):
    set.add("18/8/2024")
print('Добавлен один элемент: ', set)
index_num = ("deep")   # удалите элемент из множества
if index_num in set:
    set.discard(index_num)
print('Один элемент удален: ', set)
print("             ")
print("********** Updated dictionary **********")
print(new_dict)
