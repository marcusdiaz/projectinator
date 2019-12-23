import argparse
import os
from pathlib import Path
import keyring
import requests

print ("Starting Projectinator")

class Git():
    """Class to interact with git"""

    def __init__(self, project):
        print("Starting init")
        self.project = project
        self.git_pw = keyring.get_password('github.com2','marcus.diaz@gmail.com')
        print(self.git_pw)

        self.r = requests.get('https://api.github.com/graphql')

        print("Request:" + self.r.json())
    
    def init():
        """Do local git init"""
        pass
    
    def createRemoteRepo():
        """Create remote git repo"""
        pass

    def addAll():
        pass

    def commit():
        pass

    def push():
        pass


class Project():
    """Class to manage projects"""

    def __init__(self, name):
        self.name = name
        self.git = Git(self)
    
    def create(self):
        #First create a new directory with the project name
        print("Creating new project - " + self.name)
        os.mkdir(self.name)

        #Change to that directory
        os.chdir(self.name)

        #Create a new README.md
        Path('./README.md').touch()

        #Create a new repo in the remote repo host (github.com)
        self.git.createRemoteRepo()

        #Do a local git init
        self.git.init()

        #Do a git add .
        self.git.addAll()

        #Do git commit
        self.git.commit()

        #Do git push
        self.git.push()

        #Start code .

        pass

#Parse command line args

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("args", nargs=argparse.REMAINDER)
args = parser.parse_args()

if(args.command == 'create'):
    my_proj = Project(args.args[0])
    my_proj.create()





