# Defining Node
class Node:

    """A Node in a Trie"""

    # Defining Node.method
    def __init__(self, char):

        # Defining Node.char
        self.char = char

        # Defining Node.end
        self.end = [False, 0]

        # Defining Node.child
        self.child = {}





# Defining Trie
class Trie:

    """A Trie of Nodes"""

    # Defining Trie.method
    def __init__(self):

        # Define Trie.root (empty Node)
        self.root = Node('')

    # Defining Trie.add(x)
    def add(self, x, c):

        # Begin at root Node
        node = self.root

        # For each character in x
        for char in x:

            if char in node.child:

                # If a Node exists, move to that Node
                node = node.child[char]

            else:

                # If not, create a node for that character and move to that Node
                tmp = Node(char)
                node.child[char] = tmp
                node = tmp

        # The end of the Node has Node.end = True
        node.end = [True, c]

    # Defining Trie.find(x)
    def find(self, x):

        # Begin at root Node
        node = self.root

        # for each character in x
        for char in x:

            if char in node.child:

                # If a Node exists, move to that Node
                node = node.child[char]

            else:

                # If not, return False
                return [False]

        # Return node.end
        return node.end

    # Defining Trie.prefix(prefix)
    def prefix(self, prefix):

        # Begin at root node
        node = self.root

        # For each character in prefix
        for char in prefix:

            if char in node.child:

                # If Node exists, move to that Node
                node = node.child[char]

            else:

                # If not, return False
                return False

        # If all Node have not empty Node.child, return True
        return True





# Defining the boggle function
def calculateboggle(i, j, boggleb, boxbool, buffer, dict, Trie, length):

    if Trie.find(buffer)[0] and buffer not in dict and len(buffer) > 2:

        index = []

        # Get the index of a boxbool on '1'
        for a in range(len(boxbool)):

            for b in range(len(boxbool[a])):

                if boxbool[a][b] == 1:

                    index.append((4 * a) + b)

        # If buffer valid, and not in already, add to dict
        dict[buffer.title()] = index

        # add len(buffer) to length
        if len(buffer) not in length:

            length.append(len(buffer))

    if Trie.prefix(buffer) == False:

        # If buffer not a valid prefix, return
        return

    if len(buffer) == 16:

        # If boggle fully traversed, return
        return

    for x in range(i - 1, i + 2):

        for y in range(j - 1, j + 2):

            # If neighbour in boggle and not traversed
            if x > -1 and x < 4 and y > -1 and y < 4 and boxbool[x][y] == 0:

                # Add '1' to boxbool
                boxbool[x][y] = 1

                # Run boggle
                calculateboggle(x, y, boggleb, boxbool, buffer + boggleb[x][y], dict, Trie, length)

                # If boggle is done, remove '1' from boxbool
                boxbool[x][y] = 0





# Populating Trie
def populate(Trie):

    # Open dictionary
    dictionary = open('dictionary/dictionary.txt', 'r')

    # For entry index
    c = 0

    while True:

        # Read line for dictionary
        x = dictionary.readline().rstrip('\n')

        c += 1

        if not x:

            # If end of file, return
            return

        # Add x to Trie
        Trie.add(x, c)





# Filling boxbool of '0'
def fill(boxbool):

    for i in range(4):

        for j in range(4):

            # For each box, boxbool[i][j] = 0
            boxbool[i][j] = 0





# Getting definition index
def definition(Trie, entry):

    index = Trie.find(entry.upper())

    # If Trie.find == True
    if index[0]:

        # Return index
        return index[1]

    return False





# Getting definition detail for entry
def finddefinition(index):

    # Open dictionary
    dictionary = open('dictionary/definition.txt', 'r')

    # For index
    c = 0

    while True:

        # Read line for dictionary
        x = dictionary.readline().rstrip('\n')

        c += 1

        # If def line reached, return it
        if c == index:

            return x





