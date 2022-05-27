class Node(object):
    """Objeto de nó base.
     Cada nó armazena chaves e valores. As chaves não são exclusivas para cada valor e, como tais, os valores são
     armazenado como uma lista em cada chave.
    Atributos:
        order (int): O número máximo de chaves que cada nó pode conter.
    """
    def __init__(self, order):
        """Os nós filhos podem ser convertidos em nós pais definindo self.leaf = False. Nós pais
         simplesmente atue como um meio para atravessar a árvore."""
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def add(self, key, value):
        """Adiciona um par de valores-chave ao nó."""
        # Se o nó estiver vazio, basta inserir o par de valores-chave.
        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return None

        for i, item in enumerate(self.keys):
            # Se a nova chave corresponder à chave existente, adicione à lista de valores.
            if key == item:
                self.values[i].append(value)
                break

            # Se a nova chave for menor do que a chave existente, insira a nova chave à esquerda da chave existente.
            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break

            # Se a nova chave for maior do que todas as chaves existentes, insira a nova chave à direita de todas
            # chaves existentes.
            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])

    def split(self):
        """Divide o nó em dois e os armazena como nós filhos."""
        left = Node(self.order)
        right = Node(self.order)
        mid = self.order // 2

        left.keys = self.keys[:mid]
        left.values = self.values[:mid]

        right.keys = self.keys[mid:]
        right.values = self.values[mid:]

        # Quando o nó é dividido, defina a chave pai para a chave mais à esquerda do nó filho direito.
        self.keys = [right.keys[0]]
        self.values = [left, right]
        self.leaf = False

    def is_full(self):
        """Retorna True se o nó estiver cheio."""
        return len(self.keys) == self.order

    def show(self, counter=0):
        """Imprime as chaves em cada nível."""
        print(counter, str(self.keys))

        # Imprime recursivamente a chave dos nós filhos (se houver).
        if not self.leaf:
            for item in self.values:
                item.show(counter + 1)

class BPlusTree(object):
    """Objeto de árvore B +, consistindo de nós.
     Os nós serão automaticamente divididos em dois quando estiverem cheios. Quando ocorre uma divisão, uma chave
     'flutuar' para cima e ser inserido no nó pai para atuar como um pivô.
    Atributos:
        order (int): O número máximo de chaves que cada nó pode conter.
    """
    def __init__(self, order=8):
        self.root = Node(order)

    def _find(self, node, key):
        """ Para um determinado nó e chave, retorna o índice onde a chave deve ser inserida e o
         lista de valores nesse índice."""
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i

        return node.values[i + 1], i + 1

    def _merge(self, parent, child, index):
        """Para um nó pai e filho, extraia um pivô do filho para ser inserido nas chaves
         do pai. Insira os valores do filho nos valores do pai.
        """
        parent.values.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break

    def insert(self, key, value):
        """Insere um par de valores-chave após passar para um nó folha. Se o nó folha estiver cheio, divida
         o nó folha em dois.
        """
        parent = None
        child = self.root

        # Percorra a árvore até que o nó folha seja alcançado.
        while not child.leaf:
            parent = child
            child, index = self._find(child, key)

        child.add(key, value)

        # Se o nó folha estiver cheio, divida o nó folha em dois.
        if child.is_full():
            child.split()

            # Depois que um nó folha é dividido, ele consiste em um nó interno e dois nós folha. Estes