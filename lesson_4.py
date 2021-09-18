# Метод sort
# product = ['milk', 'Apple','watermelon', 'banana', 'shugar', 'apple', 'Banana']
# product.sort()
# print(product)


# numbers = [9,6,5,3,0,124,122,76]
# numbers.sort() #сортирует список навсегда 
# print(numbers)
# my_list = ['asdf','!@#','124']
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True) # reverse - аргумент метода, который по умолчанию False
# print(my_list) # reverse - меняет порядок сортировки в обратном напралении, если передать True

# функция sorted
# numbers = [9,6,5,3,0,124,122,76]
# print(sorted(numbers))
# print(numbers)
# sorter_numbers = sorted(numbers)
# print(sorter_numbers)


# numbers = [1,2,3,4,5,6,7,8,9]
# numbers.reverse()
# print(numbers)


# len in list определяет количество элементов в списке
# users = ['admin', 'operator', 'manager', 'Jonh', 'Olga', 'Askar']
# print(len(users))




# max(), min(), sum() выводит маленькую, большую либо сумму
# numbers = [1,5,4,8,2,9,4,76, -15]
# print(min(numbers))



# цикл - for
#while- цикл может быть бесконечным 
# ИТЕРАЦИЯ - это один цикл или одно повторение вашего цикла 
# В pthon есть итерируемые объектыЮ которых можно использовать в цикле for
# например: str, list.
names = ['Askar', 'Ali', 'Diana', 'Bilal', 'Aitegin']
for name in names:
    print(name)
a = 1

while name in names:
    b = input('Как тебя зовут? ')
    print('Привет', b, ', Добро пожаловать')