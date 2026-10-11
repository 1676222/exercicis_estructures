    """
    llista enllaçada
    
    Exemples
A LeetCode, pos indica l'índex del node al qual apunta l'últim node (−1 vol dir que no hi ha cicle). La vostra funció no rep pos: només rep head.

Llista	pos	Resultat	Explicació
[3, 2, 0, -4]	1	True	L'últim node (-4) apunta al node amb valor 2.
[1, 2]	0	True	L'últim node apunta al primer.
[1]	-1	False	No hi ha cicle.


Restriccions
La llista té entre 0 i 10⁵ nodes.
−10⁵ ≤ node.val ≤ 10⁵.
Els valors es poden repetir. Dos nodes diferents poden tenir el mateix valor.
No es pot modificar la llista: ni els valors (val) ni els punters (next).
    """

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


class Solution:
    def hasCycle(self, head):
        return hasCycle(head)