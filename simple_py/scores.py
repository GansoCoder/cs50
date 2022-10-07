nr_scores = input("How many scores do you have: ")
scores = []

i = 0
while i < int(nr_scores):
    scores.append(input("Score " + str(i+1) + ": "))
    i += 1

j = 0
st = 0
while j < len(scores):
    st = st + int(scores[j])
    j += 1

avg = st / int(nr_scores) 
print("Average: " + str(avg))