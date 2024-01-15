"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:
answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]

"""
"""
Question for interviewer is it oaky for me to use the counter method from collections to create a hashmap?
💡 This works however, Its not an effecient solution => We need to look for a better solution
"""
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
from collections import Counter

def find_players_with_zero_losses(array):
    winners, losers = [], []

    for i in range(len(array)):
        winners.append(matches[i][0])
   
    for l in range(len(array)):
        losers.append(matches[l][1])

    winners_only = []
    for i in winners:
        if i in losers or i in winners_only:
            continue
        else:
            winners_only.append(i)

    losers_who_lost_exactly_one_match = Counter(losers)
    filtered_dict = {key: value for key, value in losers_who_lost_exactly_one_match.items() if value == 1}
    return [sorted(winners_only), sorted(filtered_dict.keys())]


print(find_players_with_zero_losses(matches))
