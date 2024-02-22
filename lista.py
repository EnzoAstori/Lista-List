lista = []

while True:
    
    
    print(' \nSelecione uma opção \n')
    put = input('[i]nserir , [a]pagar, [l]istar, [s]air: ')


    
    if put == 'i':
        item = input('Item: ')
        lista.append(item)
        print(f'{lista=}')
        
            
       
    elif put == 'a':
        if lista == []:
            print('Lista Vazia')
            continue
        
        indice = input('Digite o indice que deseja apagar: ')
        indice_int = int(indice)
        
        
        if indice_int <= len(lista):
            lista.pop(indice_int)
        else:
            print('Digite um indice valido ')
        
       
    elif put == 'l':
        if lista == []:
                print('Lista Vazia')
                
       
        
        for numero, item_lista in enumerate(lista,start=1):
            print(numero, item_lista)
            
            
    
    elif put == 's':
        break
    

    else:
        print('Digite uma opção valida') 