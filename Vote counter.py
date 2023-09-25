# 13th project - Vote counter
# Purpose: Use dictionary for counting votes

votes = ['Trump', 'Trump', 'Biden', 'Biden', 'Trump', 'Biden','Biden', 'Trump', 'Biden', 'Biden', 'Biden', 'Biden', 'Trump', 'Trump', 'Biden','Trump', 'Biden', 'Trump', 'Trump', 'Biden','Trump','Trump', 'Trump', 'Biden',]

vote_counter ={}

for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

print(vote_counter)