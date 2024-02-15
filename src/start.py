from hello_function import hello

print("Введите имя, чтобы начать игру")

name = input("Как вас зовут: ")
result = hello(name)
print(result + " \nДобро пожаловать!")
