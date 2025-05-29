"""
Belle Biery
5/29/25
Dictionary that extends a given json file for interfile calling of one data structure
"""

import json


class JsonParser(dict):

    def __init__(self, file):
        self.fileGets = 0
        self.fileName = file
        fileObj = open(file, "r")
        self = json.loads(fileObj.read())
        fileObj.close()

    def getFile(self, file=None):
        # Check if specific file is provided
        if file == None:
            file = self.fileName
        self.fileGets += 1
        # open file
        fileObj = open(file, "r")
        # update the data
        self.update(json.loads(fileObj.read()))
        # close the file
        fileObj.close()

    def updateFile(self, file=None):
        # check if specified file is provided
        if file == None:
            file = self.fileName
        # open the file
        fileObj = open(file, "w")
        # write to the file
        fileObj.write(json.dumps(self, indent=4))
        # close the file
        fileObj.close()

    # update data before repr
    def __repr__(self):
        self.getFile()
        return super().__repr__()

    # update data before getting item
    def __getitem__(self, key):
        self.getFile()
        return super().__getitem__(key)

    # update data before setting item and update file after
    def __setitem__(self, key, value):
        self.getFile()
        super().__setitem__(key, value)
        self.updateFile()
