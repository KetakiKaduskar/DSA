def jobSequence(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    maxDead = max(job[1] for job in jobs)
    result = [-1 for _ in range(maxDead)]
    maxProfit = 0

    for job in jobs:
        for i in range(job[1], -1, -1):
            print(job[1], i)
            if result[i - 1] == -1:
                result[i - 1] = job[0]
                maxProfit += job[2]
                break

    return result, maxProfit

jobs = []
while True:
    inp = input()
    if inp == "":
        break
    jobs.append(list(map(int, inp.split())))

print(jobSequence(jobs))