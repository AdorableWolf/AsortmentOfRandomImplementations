""" Implementing a file syncing algorithm for two computers that are connected
by a low bandwidth network --- Coding Question asked by Google"""

"""Interpretation of the question----
Since the network is low-bandwidth and unreliable, realtime syncing of the files is not possible
and error prone. Hence we need need a way to sync the entire directory file structure."""

#This could be implented using a Merkle Tree Data structure.

"""Three possible cases arise------
1. Whenever a change in the file is made, recalculate the hashes of the entire directory branch 
that file is part of.
2. Nodes witht the same hashes could be ignored from syncing. 
3. To sync changes, compare the Merkle Tree of both systems."""

from hashlib import md5

class MerkleFile(object):
    def __init__(self):
        self.content = ""
        self.hash = ""
        self.children = []
        self.parent = None
        self.is_dir = None
    
    def set_content(self, new_content):
        if self.is_dir:
            raise Exception("Can't set the contents of a directory")

        self.content = new_content
        self.recalculate_directory_hash()
    
    def recalculate_directory_hash(self):
        parent = self.parent

        if not self.is_dir:
            self.hash = md5(self.content.encode()).hexdigest()
        
        while parent:
            children = parent.children
            concat_hash = ""
            for child in children:
                concat_hash += child.hash
            
            parent.hash = md5(concat_hash.encode()).hexdigest()

            parent = parent.parent
    
    def add_file_to_directory(self, directory):
        directory.children.append(self)
        self.parent = directory
        self.recalculate_directory_hash()
    
