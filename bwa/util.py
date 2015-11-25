from typing import List, Any, Callable


def list_a_greater_than_list_b(a: List[Any], b: List[Any]) -> bool:
    for a_b in zip(a, b):
        if not (a_b[0] >= a_b[1]):
            return False
        else:
            return True

def list_a_less_than_list_b(a: List[Any], b: List[Any]) -> bool:
    for a_b in zip(a, b):
        if not (a_b[0] <= a_b[1]):
            return False
        else:
            return True



class HeapError(Exception):
    pass


class Heap:
    """
    heap in an array is:
    index k has left child at 2k and right child at 2k+1
    parent of k is k/2

    height will be log(# elements in tree)
    """

    def __init__(self, size: int) -> None:
        self.heap = [[None] for _ in range(size+1)] # type: List[Any]
        self.n = 0


    @classmethod
    def from_lists(cls, l: List[Any]) -> 'Heap':
        """
        alternative constructor for initializing from a list of lists
        :param l:
        :return: filled heap
        """

        heap = cls(len(l))
        for item in l:
            heap.insert(item, list_a_greater_than_list_b)

        return heap


    def insert(self, item: Any, a_greater_than_b: Callable[[Any, Any], bool]) -> None:
        """

        :param item:
        :param a_greater_than_b: function that compares first arg against second arg and returns first > second
        :return:
        """
        def bubble_up(index):
            if Heap.get_parent(index) == -1:
                # at root
                return
            if a_greater_than_b(self.heap[Heap.get_parent(index)], self.heap[index]):
                self.swap(index, Heap.get_parent(index))
                bubble_up(Heap.get_parent(index))

        if self.n >= len(self.heap):
            raise HeapError("heap overflow")
        else:
            self.n += 1
            self.heap[self.n] = item
            bubble_up(self.n)

    @staticmethod
    def get_parent(node: int) -> int:
        if node == 1:
            return -1
        else:
            return node // 2

    @staticmethod
    def young_child(node: int) -> int:
        return node * 2

    def swap(self, n1: int, n2: int) -> None:
        tmp = self.heap[n1]
        self.heap[n1] = self.heap[n2]
        self.heap[n2] = tmp


    def extract_minimum(self, a_greater_than_b: Callable[[Any, Any], bool]) -> Any:
        """
        removes minimum element from tree
        :return: minimum element
        """
        def bubble_down(index):
            child_index = Heap.young_child(index)
            min_index = index
            for i in range(2):
                if child_index + i <= self.n:
                    if a_greater_than_b(self.heap[min_index], self.heap[child_index + i]):
                        min_index = child_index + i
            if min_index != index:
                self.swap(index, min_index)
                bubble_down(min_index)

        if self.n <= 0:
            raise HeapError("empty heap")
        else:
            minimum = self.heap[1]
            self.heap[1] = self.heap[self.n]
            self.n -= 1
            bubble_down(1)

            return minimum


    def sort(self) -> None:
        sorted_heap = [] # type: List[Any]
        try:
            while True:
                sorted_heap.append(self.extract_minimum(list_a_greater_than_list_b))
        except HeapError:
            # heap is now empty, woot
            pass

        self.heap = sorted_heap


