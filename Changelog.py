class Change:
    def __init__(self, change: str, author: str, issue_number: int = None, pr_number: int = None):
        self.change = change
        self.author = author
        self.issue_number = issue_number
        self.pr_issue = pr_number

    def get_string(self) -> str:
        return f"{self.change}{f' [#{self.issue_number}]' if self.issue_number else ''}{f' [#{self.pr_issue}]' if self.pr_issue else ''} by {self.author}"


class ChangeCategory:
    def __init__(self, category_name: str):
        self.category_name = category_name
        self.changes = []

    def add_change(self, change: Change):
        self.changes.append(change)


class Changelog:
    categories = None

    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)
