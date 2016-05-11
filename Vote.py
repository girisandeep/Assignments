#!/usr/bin/python
#import fileinput
#for line in fileinput.input():
vote = {('A B'),('B C'),('C F'),('D F')}
worth = {('A 1'),('B 2'),('C 7'),('D 9')}
finalList = sorted(vote.union(worth))
VoteCount ={}
votes={}
finalVoteCount ={}
for entry in finalList:
    words = entry.split()
    key = words[0]
    if not VoteCount.has_key(key):
        VoteCount[key] = []
    VoteCount[key].append(words[1])
#for key in VoteCount:
#    print VoteCount[key]
for candidates in VoteCount:
    Candidate = VoteCount[candidates][1]
    if not votes.has_key(Candidate):
        votes[Candidate] = []
    votes[Candidate].append(VoteCount[candidates][0])
    
vote_sum = 0

for k, v  in votes.iteritems():
    for n in v:
        vote_sum += int(n)
    if not finalVoteCount.has_key(k):
        finalVoteCount[k] = []
    finalVoteCount[k].append(vote_sum)
    vote_sum = 0

print max(finalVoteCount, key=finalVoteCount.get) + " is the winner"