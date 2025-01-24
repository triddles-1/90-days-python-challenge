from github import Github
my_git = Github("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")
for repo in my_git.user().get_repos():
    print(repo.name)