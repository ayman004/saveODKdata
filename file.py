from git import Repo

repo_dir = 'saveODKdata'
repo = Repo(repo_dir)
file_list = [
    "C:\Users\ayman\Downloads\GG51_1706AF1807_results.csv"
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()