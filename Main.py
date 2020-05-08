def inseri(valor):
    l.append(valor)

def remove(valor):
    l.remove(valor)

def mensagem(l):
    lista = []
    for i in l:
        if (i.isdigit()):
            lista.append(int(i))

    lista.sort()

    lista = [str(i) for i in lista]
    string = ' '.join(lista)
    print(string)

l = []
temp = []
l = input().split(" ")
temp.append(" ")

while not(temp[0] == "final"):
    temp = input().split(" ")
    if(temp[0] == "inserir"):
        inseri(temp[1])
    elif(temp[0] == "remover"):
        remove(temp[1])
    elif(temp[0] == "parcial"):
        mensagem(l)
    elif(temp[0] == "final"):
        mensagem(l)


