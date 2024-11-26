def iteration_string(var):

    value_min = 0
    value_max = len(var)
    value = var[value_min]
    value_min+=1
    print(value_min)
    yield value

    return "Iterations Stopped"

# for i in iteration_string("Mahesh Guptha Challa"):
#     print(i)


import pandas as pd
import json

with open("test.json", "r") as f:
    data = json.load(f)
# df = pd.DataFrame(data)

for i in data['Rows']['Row']:
    print(i)
    # for j in i.items():
        # print(j)
        # break
    exit()        


# df    