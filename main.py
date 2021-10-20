def citire_lista1():
    int_lista1 = []
    str_lista1 = input('Dati numere ')
    str_elemente = str_lista1.split(' ')
    for elemente in str_elemente:
        int_lista1.append(int(elemente))

    return int_lista1

def citire_lista_2():
    int_lista2 = []
    str_lista2 = input('Dati numere ')
    str_elemente = str_lista2.split(' ')
    for elemente in str_elemente:
        int_lista2.append(int(elemente))

    return int_lista2

def cititre_lista_3():
    int_lista3 = []
    str_lista3 = input('Dati numere ')
    str_elemente = str_lista3.split(' ')
    for elemente in str_elemente:
        int_lista3.append(int(elemente))

    return int_lista3


def acelasi_nr_elemente_pare(lista1, lista2):
    '''
    Verifica daca cele doua liste au acelasi numar de elemente pare
    :param lista1: prima lista de int-uri
    :param lista2: a 2-a lista de int-uri
    :return: true- daca cele doua liste au acelasi numar de elemente pare, false in caz contrar
    '''


    pare_lista_1 = 0
    pare_lista_2 = 0

    pare = 0
    index = 0
    while index != len(lista1):
        if lista1[index] % 2 ==0:
            pare +=1
        index = index +1

    pare_lista_1 = pare
    pare= 0
    index = 0
    while index != len(lista2):
        if lista2[index] % 2 == 0:
             pare = pare+1
        index = index+1

    pare_lista_2 = pare

    if pare_lista_1 == pare_lista_2:
        return True
    else:
        return False

def test_acelasi_nr_elemente_pare():
    assert acelasi_nr_elemente_pare([12, 22, 36, 424], [22, 23, 36, 55 ,424]) == False

def intersectie_liste(lista1, lista2):
    '''
    Determina o lista obtinuta din intersectia a doua liste
    :param lista1: prima lista initiala de int-uri
    :param lista2: a 2-a lista initiala de int-uri
    :return: returneaza o lista care contine elementele obtinute in urma intersectie dintre lista1 si lista2
    '''
    lista_intersectie = []

    for element in lista1:
        aparitii = 0
        #verific daca elementul din lista 1 se afla si in lista2
        for element_2 in lista2:
            if element == element_2:
                aparitii = aparitii + 1

        if aparitii !=0:
            #verific daca elementul se afla deja in lista_intersectie
            ok = True
            for element_3 in lista_intersectie:
                if element == element_3:
                    ok = False
            if ok == True:
                lista_intersectie.append(element)

    return lista_intersectie


def test_intersectie_liste():
    assert intersectie_liste([1, 4, 5, 6], [15, 20, 4, 8, 6]) == [4, 6]


def palindroame_obtinute_in_urma_concatenarii(lista1, lista2):
    '''
       Determina palindroamele obtinute prin concatenarea elementelor de pe acelasi pozitii in doua liste

       :param lista1: prima lista initiala de int-uri
       :param lista2: a 2-a lista initiala de int-uri
       :return: returneaza o lista obtinuta care contine toate palindroamele obtinute prin concatenarea elementelor de pe aceleasi
       pozitii din lista 1 si lista2
       '''

    lista_palindroame = []
    if len(lista1)<= len(lista2):
        lungime = len(lista1) -1
    else:
        lungime = len(lista2)-1


    index = 0
    while lungime >= index:
        element_1 = str(lista1[index])
        element_2 = str(lista2[index])
        element_concatenat = element_1+element_2
        int_element_concatenat = int(element_concatenat)
        #verific daca int_element_concatenat este palindrom
        copie_element = int_element_concatenat
        invers = 0
        while copie_element!= 0:
            cifra = copie_element%10
            invers=invers*10 + cifra
            copie_element = copie_element // 10
        if invers == int_element_concatenat:
            lista_palindroame.append(int_element_concatenat)
        index = index +1

    return lista_palindroame

def test_palindroame_obtinute_in_urma_concatenarii():
    assert palindroame_obtinute_in_urma_concatenarii([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert palindroame_obtinute_in_urma_concatenarii([11, 5, 5], [11, 6, 5]) == [1111, 55]

def lista_inlocuita_cu_oglindit(lista, lista3):
    '''
    Determina o lista obtinuta prin inlocuirea elementelor dintr-o alta lista cu oglinditul lor daca respecta conditia:regulă: elementele sunt divizibile
    cu toate elementele dintr-o a2a lista. Dacă nu îndeplinesc regula, păstrați elementul așa cum e.
    :param lista1: prima lista initiala de int-uri
    :param lista2: a 2-a lista initiala de int-uri
    :param lista3: a 3-a lista initiala de int-uri
    :return: returneaza o alta lista obtinuta prin verificarea conditiei de mai sus
    '''

    lista_oglindite = []

    for element in lista:
        ok = True
        for numar in lista3:
            if element % numar !=0:
                ok = False

        if ok == True:
            invers = 0
            copie = element
            while copie !=0:
                cifra = copie%10
                invers = invers*10 + cifra
                copie = copie // 10
            lista_oglindite.append(invers)
        else:
            lista_oglindite.append(element)

    return lista_oglindite

def test_lista_inlocuita_cu_oglindit():
    assert lista_inlocuita_cu_oglindit([12, 22, 36, 363], [1, 2, 3, 4]) == [21, 22, 63, 363]
    assert lista_inlocuita_cu_oglindit([22, 23, 36, 55, 363], [1, 2, 3, 4]) == [22, 23, 63, 55, 363]



def main():
    while True:
        print('1. Citire lista1')
        print('2. Citire lista2')
        print('3. Verifica daca cele doua liste au acelasi numar de elemente pare')
        print('4. Afiseaza o lista ce reprezinta intersectia listelor citite')
        print('5. Afiseaza palindroamele obtinute prin concatenarea elementelor de pe aceleasi pozitii in cele doua liste')
        print('6. Inlocuieste in cele doua liste toate elementele cu oglinditul lor daca elementele sunt divizibile cu toate'
              'elemente dintr-o a treia lista care se citeste de la tastatura')
        print('x. Iesire din program')
        optiune = input('Dati optiune')
        if optiune == '1':
            lista1 = citire_lista1()
        elif optiune == '2':
            lista2= citire_lista_2()
        elif optiune == '3':
            raspuns = acelasi_nr_elemente_pare(lista1, lista2)
            if raspuns == True:
                print('DA')
            else:
                print('NU')
        elif optiune == '4':
            lista_intersectie = intersectie_liste(lista1, lista2)
            print(lista_intersectie)
        elif optiune == '5':
            lista_palindroame = palindroame_obtinute_in_urma_concatenarii(lista1, lista2)
            print(lista_palindroame)
        elif optiune == '6':
            lista3 = cititre_lista_3()
            lista_oglindite_1 = lista_inlocuita_cu_oglindit(lista1,lista3)
            print(lista_oglindite_1)
            lista_oglindite_2 = lista_inlocuita_cu_oglindit(lista2, lista3)
            print(lista_oglindite_2)
        elif optiune == 'x':
            break

test_lista_inlocuita_cu_oglindit()
test_palindroame_obtinute_in_urma_concatenarii()
test_intersectie_liste()
test_acelasi_nr_elemente_pare()
main()