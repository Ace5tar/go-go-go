"""
Belle Biery
MM/DD/YY
--Description--
--Sources--
"""

import json

class JsonParser(dict):

    def __init__(self, file):
        self.fileGets = 0
        self.fileName = file
        fileObj = open(file, 'r')
        self = json.loads(fileObj.read())
        

        fileObj.close()
        

    def getFile(self, file = None):
        if file == None: file = self.fileName
        self.fileGets +=1
        fileObj = open(file, 'r')
        self.update(json.loads(fileObj.read()))
        fileObj.close()

    def updateFile(self, file = None):
        if file == None: file = self.fileName
        fileObj = open(file,'w')
        fileObj.write(json.dumps(self, indent=4))
        fileObj.close()

    def __repr__(self):
        self.getFile()
        return super().__repr__()

    def __getitem__(self, key):
        self.getFile()
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        self.getFile()
        super().__setitem__(key, value)
        self.updateFile()


