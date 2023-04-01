name = "Luis Enrique"
last_name = 'Castro Aguilar'
age = '25'

print(name)
print(last_name)
print(age)

full_name = name + " " + last_name
print(full_name)

quote = "I'm KIKE"
print(quote)

quote2 = ' She said "Hello"  '
print(quote2)

# format
template = "Hola, mi nombre es " + name + " mi pellido es " + last_name + " y tengo " + age + " años "
print('v1 ', template)

template = "Hola, mi nombre es {} y mi apellido es {} tengo {} años".format(name, last_name, age)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} mi edad es {age}"
print('v3', template)