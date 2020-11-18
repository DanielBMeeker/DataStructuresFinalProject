"""
Program: mapMeeker.py
Author: Daniel Meeker
Date: 11/12/2020

* OS: Windows 10
* IDE: Pycharm
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : This program demonstrates a map data structure
* by using Python's built in dictionary structure.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


class KeyNotFoundError(Exception):
    pass


class DuplicateKeyError(Exception):
    pass


class MapMeeker:
    def __init__(self):
        self.map = {}

    def __str__(self):
        return '{self.map}'.format(self=self)

    def __getitem__(self, item):
        return '{self.map}'.format(self=self)

    def find_key(self, key):
        """
        determines if the key already exists
        :param key: required
        :return: boolean
        """
        return key in self.map

    def find_value_of_key(self, key):
        """
        if the key exists it returns its value, otherwise raises exception
        :param key: required
        :return: value of key
        """
        if self.find_key(key):
            return self.map[key]
        else:
            raise KeyNotFoundError("Key does not exist")

    def insert(self, key, value):
        """
        If the key doesn't exist it creates a new key value pair otherwise raises exception
        :param key:
        :param value:
        :return:
        """
        if not self.find_key(key):
            self.map[key] = value
            return "Key Created"
        else:
            raise DuplicateKeyError("Key already exists")

    def remove(self, key):
        """
        Removes the key value pair if the key exists otherwise raises exception
        :param key:
        :return:
        """
        if self.find_key(key):
            del self.map[key]
        else:
            raise KeyNotFoundError("Key does not exist")

    def size(self):
        return len(self.map)


if __name__ == '__main__':
    mapping = MapMeeker()
    # print("Inserting key value pairs")
    print(mapping.insert("dmeeker@dmacc.edu", "Daniel Meeker"))
    print(mapping.insert("aglister@dmacc.edu", "Andy Lister"))
    print(mapping.insert("meruse@dmacc.edu", "Michelle Ruse"))
    # print("Attempting to duplicate Key")
    try:
        print(mapping.insert("dmeeker@dmacc.edu", "Daniel Meeker"))
    except DuplicateKeyError as e:
        print(e)
    # print("Finding if key exists and printing values")
    print(mapping.find_key("dmeeker@dmacc.edu"))
    print(mapping.find_value_of_key("dmeeker@dmacc.edu"))
    print(mapping.find_value_of_key("meruse@dmacc.edu"))
    # print("removing a key")
    mapping.remove("dmeeker@dmacc.edu")
    # print("removing a key that does not exist")
    try:
        mapping.remove("dmeeker@dmacc.edu")
    except KeyNotFoundError as e:
        print(e)
    # print("Searching for a key that doesnt exist")
    print(mapping.find_key("dmeeker@dmacc.edu"))
    print(mapping.insert("dmeeker@dmacc.edu", "Daniel Meeker"))
    try:
        mapping.find_value_of_key("abc")
    except KeyNotFoundError as e:
        print(e)
    # print("Removing all keys")
    mapping.remove("dmeeker@dmacc.edu")
    mapping.remove("aglister@dmacc.edu")
    mapping.remove("meruse@dmacc.edu")
    # print("Searching again for a key to make sure it was removed")
    try:
        mapping.find_key("aglister@dmacc.edu")
    except KeyNotFoundError as e:
        print(e)

