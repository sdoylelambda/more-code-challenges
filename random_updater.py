import random
from datetime import datetime
import time
# import git # pip install gitpython


# git_dir = git.Repo('Path/to/repo') # update to local directory of the project

def git_commit():
    pass
    # print('git commit')
    # g = git.cmd.Git(git_dir)
    # g.commit()
    
    # repo.remotes.origin.pull()


def make_request():
    print('git PR')
    # g = git.cmd.Git(git_dir)
    # g.push()


def merge_request():
    print('PR merged')
    # g = git.cmd.Git(git_dir)
    # g.merge()


def random_updater():
    pass
    x = random.randint(0, 5)
    y = datetime.now()
    weekday = y.weekday()
    sleep_time = random.randint(1, 5) # Update to time in seconds range start, finish
    commit_count = 0

    if weekday < 6:
        pass

    if x % 2 == 0:
        r = x/2 + 2
        while r > 0:
            git_commit()
            time.sleep(sleep_time)
            r -= 1
            print('git commit')
            commit_count += 1

    
    else:
        while x > 0:
            git_commit()
            time.sleep(sleep_time)
            x -= 1
            print('git commit')
            commit_count += 1

    # Pull Request - Make and Merge
    if x == 5 or x == 3:
        make_request()
        time.sleep(sleep_time)
        merge_request()

    print(commit_count)
    


random_updater()