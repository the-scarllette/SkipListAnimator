from random import randint


# Generates a sorted skiplist with random values
def random_skiplist(max_value=15, min_length=3, max_len=15, height=3, length=0):
    if length <= 0:
        length = randint(min_length, max_len)
    elems = []
    for i in range(length):
        to_add = randint(1, max_value)
        while to_add in elems:
            to_add = randint(1, max_value)
        elems.append(to_add)
    return SkipList(elems=elems, height=height)


class SkipListNode:

    def __init__(self, data=None):
        self.data = data
        self.pointers = []
        return


class SkipList:

    def __init__(self, elems=[], height=3):
        self.height = height
        self.start_node = None
        self.length = 0

        if elems:
            elems.sort()
            for i in range(len(elems)):
                self.add(to_add=elems[i])
        return

    # Creates a skiplistnode holding the data to_add and appends it to the end of the skiplist
    def add(self, to_add):
        new_node = SkipListNode(data=to_add)
        self.length += 1

        if self.start_node is None:
            self.start_node = new_node
            self.start_node.pointers = [None for i in range(self.height)]
            return

        for i in range(self.height):
            if i == 0 or (randint(1, pow(2, i)) == 1):
                current_node = self.start_node
                while True:
                    next_node = current_node.pointers[i]
                    if next_node is None:
                        break
                    current_node = next_node
                current_node.pointers[i] = new_node
                new_node.pointers.append(None)
            else:
                break
        return

    # Prints a visual of the skiplist
    def print_nice(self):
        to_print = ["" for i in range(self.height)]

        current_node = self.start_node
        while current_node != None:
            i = 0
            N = len(current_node.pointers)
            while i < N:
                to_print[i] += (str(current_node.data) + "-")
                i += 1
            while i < self.height:
                for k in range(len(str(current_node.data)) + 1):
                    to_print[i] += "-"
                i += 1
            current_node = current_node.pointers[0]

        for line in to_print:
            print(line)
        return

    # Searches for a given piece of data in the skiplist.
    # If with_path is True, returns an array of 'directions' to get to the found element.
    def search(self, to_find=None, with_path=False):
        if to_find is None:
            return -1

        search_path = []

        k = self.height - 1
        current_node = self.start_node
        while True:
            if current_node is None:
                return -1
            if to_find == current_node.data:
                if with_path:
                    return search_path
                return current_node
            if to_find < current_node.data:
                return -1
            while k > 0:
                if current_node.pointers[k] == None or current_node.pointers[k].data > to_find:
                    search_path.append(-1)
                    k -= 1
                else:
                    break
            current_node = current_node.pointers[k]
            search_path.append(1)
