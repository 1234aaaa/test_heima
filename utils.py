import json
import os


def read_json_data(file_path, method_name=None):
    result_list = list()
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        json_data = json.load(f)
        if method_name is None:
            for temp in json_data:
                result_list.append(list(temp.values()))
        else:
            for temp in json_data.get(method_name):
                result_list.append(list(temp.values()))
    return result_list