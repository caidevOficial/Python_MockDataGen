import json
import pandas as pd

test2 = pd.DataFrame({"A": [1, 2, 3], "B": ["Python", "Java", "SQL"]})

list_int = [
            1234, 12345, 2345, 23456, 345
        ]
list_str = [
            "Python", "Java", "SQL", "Golang", "Scala"
        ]

test = {
    "test_table": {
        "field_1": list_int,
        "field_2": list_str
    }
}

# with open('original_test.json', 'w+') as jsonFile:
#     jsonFile.write(json.dump(test, sort_keys=True, indent=4, separators=(',', ':')))



test = pd.DataFrame(test)
# ‘split’, ‘records’, ‘index’, ‘table’
# test2.to_json('test2.json', orient='records', indent=4)
#test.to_json('test.json', orient='columns', indent=4)
#test = test.concat(pd.Series(list_str))
print(test)