def sumaLista(lista):
    if lista == []:
        return 0
    else:
        return sum(lista)
# sumaLista([1, 2, 3, 4, 5]) -> 15


def exitsElement(element, lista):
    if element in lista:
        return True
    else:
        return False
# existElement(2, [1, 2, 3, 4, 5]) -> True


def findElement(element, lista):
    if exitsElement(element, lista) in lista:
        return element
    else:
        return False

# findElement(2, [1, 2, 3, 4, 5]) -> 2


def reverseList(lista):
    if lista == []:
        return []
    else:
        rev = list(reversed(lista))
        return rev
# reverseList([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]


def multList(lista):
    if not lista:
        return 1
    else:
        return lista[0] * multList(lista[1:])
