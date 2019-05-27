import sys

class Elem():

    def __init__(self, nome, ante = None, prox = None):
        self.nome = nome
        self.ante = None
        self.prox = None


class ListaDuplEncad():
    cabeca = None
    cauda = None

    def add(self, elem):
        novo_elem = Elem(elem)
        # Se a lista estiver vazia
        if(self.cabeca == None):
            self.cabeca = novo_elem
            self.cabeca.prox = novo_elem
            self.cabeca.ante = novo_elem
            self.cauda = novo_elem
            self.cauda.prox = novo_elem
            self.cauda.ante = novo_elem
            return True
        # Se ja tiver elementos
        else:
            # Comparando com a cabeca
            if(novo_elem.nome == self.cabeca.nome):
                return False
            else:
                aux = self.cabeca.prox
                # Percorrendo o resto da lista
                while(aux.nome != self.cabeca.nome):
                    if(aux.nome == novo_elem.nome):
                        return False
                    else:
                        aux = aux.prox
                # Inserindo o elemento
                self.cauda.prox = novo_elem
                self.cabeca.ante = novo_elem
                novo_elem.ante = self.cauda
                novo_elem.prox = self.cabeca
                self.cauda = novo_elem
                return True

    def remove(self, elem):
        novo_elem = Elem(elem)
        # Se so tiver um elemento na lista
        if(self.cabeca == self.cauda):
            if(novo_elem.nome == self.cabeca.nome):
                self.cabeca = None
                self.cauda = None
                return True
            return False
        else:
        # Se o elemento a ser removido for a cabeca
            if(novo_elem.nome == self.cabeca.nome):
                self.cabeca.prox.ante = self.cauda
                self.cauda.prox = self.cabeca.prox
                self.cabeca = self.cabeca.prox
                return True
        # Se o elemento a ser removido for a cauda
            elif(novo_elem.nome == self.cauda.nome):
                self.cauda.ante.prox = self.cabeca
                self.cabeca.ante = self.cauda.ante
                self.cauda = self.cauda.ante
                return True
        # Se for qualquer outro
            else:
                aux = self.cabeca.prox
                while(aux.nome != self.cauda.nome):
                    if(novo_elem.nome == aux.nome):
                        aux.ante.prox = aux.prox
                        aux.prox.ante = aux.ante
                        return True
                    else:
                        aux = aux.prox
            return False

    def show(self, elem):
        show_elem = Elem(elem)
        # Se o lemento for a cabeca
        if(show_elem.nome == self.cabeca.nome):
            return self.cabeca
        # Se for qualquer outro
        else:
            aux = self.cabeca.prox
            while(aux.nome != self.cabeca.nome):
                if(show_elem.nome == aux.nome):
                    return aux
                else:
                    aux = aux.prox
        # Se o elemento nao estiver na lista
        return None

    def showAll(self):
        print(self.cabeca.nome)
        aux = self.cabeca.prox
        while (aux.nome != self.cabeca.nome):
            print(aux.nome)
            aux = aux.prox


def main(args):
    # Ilustrando uso de argumentos de programa
    print("#ARGS = %i" %len((args)))
    print("PROGRAMA = %s" %(args[0]))
    print("ARG1 = %s, ARG2 = %s" %(args[1], args[2]))

    # Abrindo os arquivos
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2],'w')
    lista = ListaDuplEncad()

    for line in input.readlines():
        line = line.replace('\n', "")
        line = line.split(" ", 1)
        if line[0] == "ADD":
            if lista.add(line[1]):
                output.write("[ OK  ] ADD " + line[1] + "\n")
            else:
                output.write("[ERROR] ADD " + line[1] + "\n")
        elif line[0] == "SHOW":
            if lista.show(line[1]) is None:
                output.write("[ERROR] ?<-" + line[1] + "->?" "\n")
            else:
                aux = lista.show(line[1])
                output.write("[ OK  ] " + aux.ante.nome + "<-" + aux.nome + "->" + aux.prox.nome + "\n")

        elif line[0] == "REMOVE":
            if lista.remove(line[1]):
                output.write("[ OK  ] REMOVE " + line[1] + "\n")
            else:
                output.write("[ERROR] REMOVE " + line[1] + "\n")

    # Fechando os arquivos
    input.close()
    output.close()
    #Finalizando programa

if __name__ == '__main__':
    main(sys.argv)