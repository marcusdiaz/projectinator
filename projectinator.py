import argparse
import os
from pathlib import Path
import requests
from github import Github

print ("Starting Projectinator")

class Git():
    """Class to interact with git"""

    def __init__(self, name):
        print("Starting init")
        self.name = name
        #self.git_pw = keyring.get_password('github.com2','marcus.diaz@gmail.com')
        self.git_pw = os.environ['GITPW']
        self.git_user = os.environ['GITUSR']
        self.api_token = os.environ['GITTKN']

        self.g = Github(self.api_token)
        
        self.repo_exists = False
        for repo in self.g.get_user().get_repos():
            print(repo.name)
            # to see all the available attributes and methods
            #print(dir(repo))
            if(repo.name == self.name):
              self.repo_exists = True

    def createRemoteRepo(self):
        """Create remote git repo"""
        if(not self.repo_exists):
            #Create new repo
            g.get_user().create_repo(self.name)
        else:
            print("Repo already exists! Not creating...")
        pass
        
    def init(self):
        """Do local git init"""
        cmd = "git init"
        print(cmd)
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('returned value:', returned_value)
        pass
    
    def addAll(self):
        cmd = "git add ."
        print(cmd)
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('returned value:', returned_value)
        pass

    def commit(self):
        cmd = "git commit -m 'Initial commit'"
        print(cmd)
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('returned value:', returned_value)
        pass

    def addRemote(self):
        cmd = "git remote add origin https://github.com/marcusdiaz/" + self.name
        print(cmd)
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('returned value:', returned_value)
        pass

    def push(self):
        cmd = "git push -u origin master"
        print(cmd)
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('returned value:', returned_value)
        pass


class Project():
    """Class to manage projects"""

    def __init__(self, name):
        self.name = name
        self.git = Git(self.name)
    
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
        self.git.addAll()
        self.git.commit()
        self.git.addRemote()
        self.git.push()

        #Start code .
        cmd = "code ."
        print(cmd)
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('returned value:', returned_value)

        pass

#Parse command line args

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("args", nargs=argparse.REMAINDER)
args = parser.parse_args()

if(args.command == 'create'):
    my_proj = Project(args.args[0])
    my_proj.create()


