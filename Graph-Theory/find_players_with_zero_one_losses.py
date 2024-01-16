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


# print(find_players_with_zero_losses(matches))

def find_players(matches):
    # Create dictionaries to store wins and losses for each player
    wins = {}
    losses = {}

    # Iterate through matches
    for winner, loser in matches:
        # Update wins
        if winner in wins:
            wins[winner] += 1
        else:
            wins[winner] = 1

        # Update losses
        if loser in losses:
            losses[loser] += 1
        else:
            losses[loser] = 1

    # Find players who have not lost any matches
    not_lost_any = [player for player in wins if player not in losses]

    # Find players who have lost exactly one match
    lost_once = [player for player in losses if losses[player] == 1]

    # Sort the lists
    not_lost_any.sort()
    lost_once.sort()

    return [not_lost_any, lost_once]

# Example usage:
# matches = [[1, 2], [3, 1], [4, 2], [2, 5]]
result = find_players(matches)
print(result)

