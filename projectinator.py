import argparse
import os
from pathlib import Path
import keyring
import requests

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

#        print("USR: " + self.git_user + " PW: " + self.git_pw)

        self.s = requests.Session()
        s = self.s
        s.auth = (self.git_user, self.git_pw)

#        s.headers.update({'x-test': 'true'})
        # both 'x-test' and 'x-test2' are sent
#        r = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

        s.headers.update({'Authorization': 'token %s' % self.api_token})

        c_r = s.post('https://api.github.com/graphql/marcusdiaz/test3', headers=s.headers)
        #POST /user/repos

        #self.r = requests.get('https://api.github.com/graphql')

        response_dict = c_r.json()

        print("Keys: ")
        print(response_dict.keys())

        print(response_dict['message'])

#        print(response_dict['headers'])
    
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
        #self.git.createRemoteRepo()

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
    #my_proj.create()





