#!/usr/bin/python3
'''
Module 100-singly_linked_list
class Node that defines a node of a singly linked list
class SinglyLinkedList that defines a singly linked list
Singly linked list is printable one node number by a line.
Insertion to linked list is in a sorted order.
'''


class Node:
    '''
    Defines a node of a singly linked list

    Args:
        data (int): data to store in a node
        next_node: link to next node

    Functions:
        __init__(self, data, next_node=None)
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    '''

    def __init__(self, data, next_node=None):
        '''
        initialization of class Node

        Attributes:
            data: data to store in a node
            next_node: link to next node
        '''

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        Getter

        Returns: data
        '''

        return self.__data

    @data.setter
    def data(self, value):
        '''
        Setter

        Args:
            value: value to set data to
        '''

        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        Getter

        Returns: next_node
        '''

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        Setter

        Args:
            value: value to set next_node to
        '''

        if value is None:
            pass
        elif type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''
    Defines a singly linked list

    Args:
        head: head node of linked list

    Functions:
        __init__(self):
        __str__(self):
        sorted_insert(self, value)
    '''

    def __init__(self):
        '''
        initializes class SinglyLinkedList
        '''

        self.__head = None

    def __str__(self):
        '''
        prints the entire list in stdout
        one node number by line

        Returns: An empty string
        '''

        temp = self.__head
        while temp is not None:
            if temp.next_node is None:
                print("{}".format(temp.data), end="")
            else:
                print("{}".format(temp.data))
            temp = temp.next_node
        return ""

    def sorted_insert(self, value):
        '''
        function to insert a newnode in linked list in increasing order

        Args:
            value: value to be inserted
        '''

        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
