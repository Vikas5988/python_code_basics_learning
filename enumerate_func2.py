# List of scores
scores = [45, 78, 92, 63, 88, 55, 91]

print("Using enumerate() with if condition:")
for position, score in enumerate(scores,start=1):
    if score >= 75:
        print("Student at position " + str(position) + " passed with score: " + str(score))
    else:
        print("Student at position " + str(position) + " failed with score: " + str(score))
