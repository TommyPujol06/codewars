grades = list(map(float, input().split()))
weight = list(map(float, input().split()))

n = len(grades)
mean = 0.0

for m, w in zip(grades, weight):
    mean += m * w

print(f"The student final grade is {round(mean, 1)}")
