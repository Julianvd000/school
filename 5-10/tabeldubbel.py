studentenCijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]


def gemiddeldePerStudent(studentenCijfers):
    antw = []
    for i in studentenCijfers:
       antw.append(int(sum(i) / len(i)))

    return antw


def gemiddeldeVanAlleStudenten(studentenCijfers):
    antw = 0
    lst = []
    delen = len(studentenCijfers)
    for i in studentenCijfers:
       lst.append(sum(i) // len(i))
    antw = sum(lst) // delen

    return antw


print(gemiddeldePerStudent(studentenCijfers))

print(gemiddeldeVanAlleStudenten(studentenCijfers))
