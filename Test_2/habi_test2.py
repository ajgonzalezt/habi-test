#%%
def process_chain(cadena_numeros):
    str_list = str(cadena_numeros)
    str_splited = str_list.split('0')
    #ordena cada uno de los elementos de la lista
    sorted_list = [sorted(x) for x in str_splited]
    for i in range(len(sorted_list)):
        #elimina los elementos vacios de la lista
        if sorted_list[i] == []:
            sorted_list[i]=['x']
    print(' '.join([''.join(x) for x in sorted_list]))
    return 

def main ():
    while True:
        cadena_numeros = input('Ingrese la cadena de numeros que desea separar y ordenar')
        try:
            int(cadena_numeros)
        except:
            print('Por favor ingrese una cadena de numeros')
            continue
        process_chain(cadena_numeros)
        return
        

#%%
#examples
process_chain('321')
print('_________________________')
process_chain('32321065400112030')
print('_________________________')
process_chain('325100012031293')
print('_________________________')
process_chain('329010281203123')
print('_________________________')
process_chain('0321046231423012365123')
# %%
