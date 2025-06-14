import random
import math

def auto_gp(students, batch):
    group_names = ["Lion", "Falcon", "Cobra", "Tiger", "Eagle", "Shark", "Raven", "Fox", "Wolf"]
    random.shuffle(group_names)
    random.shuffle(students)
    group_size = math.ceil(len(students) / batch)

    groups = [students[i:i+group_size] for i in range(0, len(students), group_size)]

    for i, group in enumerate(groups):
        group_name = group_names[i % len(group_names)]
        print(f"Team {group_name}: {group}")
    


students = ["omid", "hasi", "helia", "julia", "saba", "ebrahim", "mohammad", "ali", "hasan", "hossein"]
batch = 4

auto_gp(students, batch)
