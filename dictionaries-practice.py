favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'asad': 'java'
    }

print(favourite_languages)

print(favourite_languages['sarah'].title())
print(favourite_languages.get('asad'))


for name, language in favourite_languages.items():
    print(f"{name} likes {language}")

#nesting
    
    dict_0 = {'color':'yellow', 'points':5}
    dict_1 = {'color':'red', 'points':15}

    dict_list = [dict_0, dict_1]

    print(dict_list[1])