from github import Github


def create_repository(repositpory):
    mytoken = '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'
    g = Github(mytoken)
    user = g.get_user()
    repo = user.create_repo(repositpory)
