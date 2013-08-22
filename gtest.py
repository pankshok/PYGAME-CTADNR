#! /usr/bin/env python

import os, sys
import re
#import pydot


#1) get list of .py files
#2) get import strings from each file
#3) map {file, list_of_imported_files}
#4) generate dot file
#5) load dot file and write png

class CImportGrapher(object):
    def __init__(self, work = "./"):
        self.work = work
        self.filelist = None
        self.filterList = [

    def getFileList(self):
        def filterFileList(self, files, fltr):
            res = []
            for f in files:
                if re.match(fltr, f):
                    res.append(f)
            return res
                    
        fltr = r"\w+\.py"
        
        self.filelist = filterFileList(self, os.listdir(self.work), fltr)
    
    
        
    def getImportMapping(self):
        '''
        getImportMapping() --> dict {"file.py" : ["import1", "import2", ... ]}
        
        '''
        def extractImports(self, src):
            '''
            extractImports(src) --> list
            
            Takes path to source file and returns list of import strings.
            
            '''
            importStringList = []
            with open(src, 'r') as f:
                for string in f:
                    for fltr in self.filterList:
                        if re.match(fltr, string):
                            importStringList.append(string)
            return importStringList

        def processImportStringList(self, importStringList):
            for s in importStringList:
                if s.startwith("import"):
                    print("IMPORT: " + s)
                elif s.startwith("from" ):
                    print("FROM: " + s)
                else:
                    print("ERROR: WAAT")
            
        mapDict = {pfile : extractImports(self, self.work + pfile) for pfile in self.filelist} 
        print(mapDict)
        processImportStringList(self.importStringList)


#graph = pydot.graph_from_dot_file("test.dot")
#graph.write_png("out.png")

if __name__ == "__main__":
    work = "spacegame/sources/"
    #"/home/most/programming/projects/pygame-study/spacegame/sources/"
    ig = CImportGrapher(work)
    ig.getFileList()
    ig.getImportMapping()
    #Ig.generateDotFile()
    #ig.readDotFile()
    #ig.writePNG()
    