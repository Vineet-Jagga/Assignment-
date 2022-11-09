def count_friends(friends):
    count = {}
    for friend_group in friends:
        if len(friend_group) == 1:
            friend = friend_group[0]
            count[friend] = count.get(friend, 0)
            continue
        for friend in friend_group:
            count[friend] = count.get(friend, 0) + 1
    return count


friends = ([2, 3], [3, 4], [5],[2,6],[2,4],[6,1])
print(count_friends(friends))
#   Here in the output 
#   { (person id) : (no of friends that person has) }