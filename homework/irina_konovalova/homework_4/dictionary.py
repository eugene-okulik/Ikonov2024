# Словарь, ДЗ №4

new_dict = {tuple: ['1', '3', '6', '7', 'None', 'text', 'False', '2.42'], list: ['1', '3', '6', '7', 'None', 'text', 'False', '2.42', 'sdsdf', 'Таня', 'Ира', 'Аня', 'Соня', 'Вова'], dict: {'key1': '22', 'key2': '23', 'key3': '147', 'key4': '1', 'key5': '-2'}, set: ['Light', 'Height', 'width', 'wide', 'long', 'deep']}
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
list_del = int(input("Введите номер записи, которую хотите удалить: "))   # удалите второй элемент списка
del my_list[list_del-1]
print(my_list)

# Dict
print("             ")
print("********** Dict **********")
print("Elements in the 'Dict': ", new_dict["my_dict"])
my_dict = new_dict["my_dict"]
elements_dict = len(my_dict)
print("Number of elements in the 'Dict': ", elements_dict)
# добавьте элемент с ключом ('i am a tuple',) и любым значением
check = 'i am a tuple'
getCheck = str(input('Введите фразу "i am a tuple": '))
catch = my_dict.update({getCheck: input("Введите значение ключа: ")})
if getCheck == check: catch
if getCheck != check:
    print("Написали неверно")
print("Словарь после добавления записи:", my_dict)
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
    my_set.append(input("Введите число или слово: "))
print('Обновленное Множество:', my_set)
index_num = int(input("Введите номер элемента, который хотите удалить: "))   # удалите элемент из множества
my_set.pop(index_num-1)
print('Обновленное Множество:', my_set)

print("             ")
print("********** Updated dictionary **********")

print(new_dict)



