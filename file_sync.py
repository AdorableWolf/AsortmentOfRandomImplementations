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
    
def getFileDifference(root1, root2, fileChangesFromSystem1, fileChangesFromSystem2):
    if not root1 and not root2:
        return fileChangesFromSystem1, fileChangesFromSystem2

    if not root1 or not root2:
        fileChangesFromSystem1.append(root2)
        fileChangesFromSystem2.append(root1)
        return fileChangesFromSystem1, fileChangesFromSystem2

    if root1.hash != root2.hash:
        fileChangesFromSystem1.append(root2)
        fileChangesFromSystem2.append(root1)

        root1_children = root1.children
        root2_children = root2.children

        len_difference = abs(len(root1_children) - len(root2_children))

        if len(root1_children) > len(root2_children):
            root2_children = root2_children + [None for i in range(len_difference)]
        elif len(root2_children) > len(root1_children):
            root1_children = root2_children + [None for i in range(len_difference)]
        
        for child1, child2 in zip(root1_children, root2_children):
            getFileDifference(child1, child2, fileChangesFromSystem1, fileChangesFromSystem2)
    
    return fileChangesFromSystem1, fileChangesFromSystem2

#Driver code for the above algorithm
if __name__ == '__main__':

    # create a directory structure on the first computer
    root_directory = MerkleFile()
    root_directory.is_dir = True

    file1 = MerkleFile()
    file1.is_dir = False
    file1.add_file_to_directory(root_directory)
    file1.set_content("owl city rocks!")

    file2 = MerkleFile()
    file2.is_dir = False
    file2.add_file_to_directory(root_directory)
    file2.set_content("owl city rocks again!")

    directory_2 = MerkleFile()
    directory_2.is_dir = True
    directory_2.add_file_to_directory(root_directory)

    file3 = MerkleFile()
    file3.is_dir = False
    file3.add_file_to_directory(directory_2)
    file3.set_content("owl city rocks!")

    # create a directory structure on the second computer
    root_directory_2 = MerkleFile()
    root_directory_2.is_dir = True

    file1_2 = MerkleFile()
    file1_2.is_dir = False
    file1_2.add_file_to_directory(root_directory_2)
    file1_2.set_content("owl city rocks!")

    file2_2 = MerkleFile()
    file2_2.is_dir = False
    file2_2.add_file_to_directory(root_directory_2)
    file2_2.set_content("owl city rocks again!")

    directory_2_2 = MerkleFile()
    directory_2_2.is_dir = True
    directory_2_2.add_file_to_directory(root_directory_2)

    file3_2 = MerkleFile()
    file3_2.is_dir = False
    file3_2.add_file_to_directory(directory_2_2)
    # This is the only file that is different
    file3_2.set_content("owl city rocks! pop")

    fileChangesFromSystem1, fileChangesFromSystem2 = getFileDifference(
        root_directory, root_directory_2, [], []
    )

    #Print Changes
    for fileObject in fileChangesFromSystem1:
        if (fileObject.content != ""):
            print(fileObject.content)
    