class Member:
    #initiates member with a name and makes it false that they've entered all groups
    def __init__(self, name, groups):
        self.name = name
        self.grouplist = []
        for x in range(groups):
            self.grouplist.append(False)

    #note might need to change below -1 to just group
    def change_group_status(self,group):
        self.grouplist[group - 1] = True
