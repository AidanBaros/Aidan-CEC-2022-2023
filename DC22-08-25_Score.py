scores = []

print("enter 5 scores")
for i in range(5):
    inputs = input(" -- ")
    scores.append(int(inputs))

print(scores)
for j in range(5):
    if scores[j] == 0:
        print("you need to practice")

scores.sort()

print(scores)

print(scores[0], scores[-1])
