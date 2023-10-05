from git import Repo

PATH_OF_GIT_REPO = '/tree/master.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'


def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin1')
        origin.push()
    except:
        print('Some error occurred while pushing the code')


x = input("yes")
if x.lower() == "yes":
    git_push()

