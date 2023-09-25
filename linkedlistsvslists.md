**Linked Lists vs Lists ***
Lists store data contigously in memory while nodes of a linked list are dispersed in memory.
This memory layout affets access operation; contigous layout of lists allow us to index the list, thus access operation in the list is O(1) whereas, for a linked list we need to perform a traversal thus, it becomes O(n)

Note that, given the pointer of the node to be deleted/ inserted in a linked list it takes constant amount of time.
You can simply add or delete a node between two Nodes.

The access operation in lists, as we talked about earlier, is much faster as you can simply use the index of a list to access the value you need.

In linked lists, there is no concept of indexing. To reach a certain element in the list, we must traverse it from the beginning.

The access operation in lists, as we talked about earlier, is much faster as you can simply use the index of a list to access the value you need.

Deletion at tail for arrays like data structures is in O(n), but in python, the pop method for lists is able to do it in O(1).

