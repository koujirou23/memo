from collections import OrderedDict
from deepdiff import DeepDiff
import json
import os
import difflib

def sort_jsonFile(json1, json2):
    with open(json1, encoding='utf-8') as file1, open(json2, encoding='utf-8') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        sorted_json1 = OrderedDict(sorted(data1.items(), key=lambda x: x[0]))
        sorted_json2 = OrderedDict(sorted(data2.items(), key=lambda x: x[0]))
        json.dump(sorted_json1, open('data1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
        json.dump(sorted_json2, open('data2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
        showDiff()

def showDiff():
    with open('data1.json', 'r') as f1, open('data2.json', 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

        diff = DeepDiff(json1, json2)

        # print(diff)
        print(diff.to_json(indent=4))

sort_jsonFile('json1.json', 'json2.json')