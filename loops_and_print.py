def enumerate_list(lista):
    lista1=[]
    for index,string in enumerate(lista):
        if string:
            lista1.append(f"{len(lista1)}. {string}")
    return lista1
colors= ["Red", "Green", "", "White", "Black"]
enumerated_colors=enumerate_list(colors)
print(enumerated_colors)

def enumerate_backwards(lista):
    lista1=[]
    for index,string in enumerate(lista):
        if string:
            lista1.append(f"{len(lista1)}. {string[::-1]}")
    return lista1
colors= ["Red", "Green", "", "White", "Black"]
enumerated_colors=enumerate_backwards(colors)
print(enumerated_colors)
