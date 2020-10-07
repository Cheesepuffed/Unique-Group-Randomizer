# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from MemberClass import Member
import random

# Asks user how many groups they want to make, ensures the value is an integer above 0
def ask_num_of_groups():
    while True:
        try:
            groups = int(input("How many groups do you want?\n"))
        except ValueError:
            print("Error: Please enter an integer\n")
            continue
        if groups <= 0:
            print("Error: Please enter a number greater than 0\n")
        else:
            break
    return groups

# makes the member list with commas separating each member
def make_memberlist():
    longlist = str(input("Please paste everyone's names ensuring each name is separated by a comma (,)\n"))
    return longlist.split(",")

# creates finallist in main where the list returned contains members with groups of True and False values
def make_memberlist_with_grouplist(memberlist,groups):
    memberlist_final = []
    for x in memberlist:
        memberlist_final.append(Member(x, groups))
    return memberlist_final

# searches finallist in make_random_groups to check if the selected member has been in the group before
# returns True if the person has already been in the group
def search_finallist(list,name,group):
    for x in range(len(list)):
        if list[x].name == name and list[x].grouplist[group]:
            return True
    return False

#
def search_group(list,name):
    for x in range(len(list)):
        if list[x] == name:
            return True
        else:
            return False

# finds member's index in finallist in make_random_groups
def find_member_index(final_list,name):
    for x in range(len(final_list)):
        if final_list[x].name == name:
            return x

# determines the max number of people in each group
def find_group_max(final_list,groups):
    group_max = len(final_list)/groups
    if len(final_list)%groups > 0:
        return group_max + 1
    else:
        return group_max

# makes the random groups
def make_random_groups(groups):
    global final_list
    random.shuffle(final_list)
    unpicked_list = final_list.copy()
    group_max = find_group_max(final_list,groups)
    #used to help figure out if group is full
    groups_filled = []
    for x in range(groups):
        groups_filled.append([])
    # if function generates impossible list of infinite loop, will know to restart
    error_restart = 0

    nameofpicked = ""

    # have to figure out a way to make the global list update while removing only from unpicked list
    while len(unpicked_list) > 0:
        picked_number = random.randint(0,len(unpicked_list) - 1)
        #print("Picked number: " + str(picked_number))
        random_group = random.randint(0,groups - 1)
        nameofpicked = unpicked_list[picked_number].name
        # if unpicked_list[picked_number].grouplist[x] == False:
        #print("checking group " + str(random_group + 1) + " for " + nameofpicked)
        # print(not(search_finallist(final_list,nameofpicked,x)))
        # print(len(groups_filled[x]) < group_max)
        if (not (search_finallist(final_list, nameofpicked, random_group))) and (len(groups_filled[random_group]) < group_max):
            final_list[find_member_index(final_list, nameofpicked)].grouplist[random_group] = True
            # print(final_list[find_member_index(final_list,nameofpicked)].grouplist[x])
            groups_filled[random_group].append(nameofpicked)
            #print("Added " + nameofpicked + " to group " + str(random_group + 1) + "\n")
            del unpicked_list[picked_number]
            # print("break---------")
            error_restart = 0
        error_restart += 1
        if error_restart == 100:
            print("seed doesn't work, try running the program again")
            exit()
    return groups_filled

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numberOfGroups = ask_num_of_groups()

    final_list = make_memberlist_with_grouplist(make_memberlist(),numberOfGroups)

    for round in range(numberOfGroups):
        print("\n\nRound " + str(round + 1) + "------------------------------")
        group_index = 1
        listofgroups = make_random_groups(numberOfGroups)
        for group in listofgroups:
            print("\nGroup " + str(group_index) + "---------------")
            for name in group:
                print(name)
            group_index += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
