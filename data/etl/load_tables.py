import json

def jsonl_to_list(file_path: str):
    with open(file_path, 'r') as fp:
        json_list = list(fp)
    dict_list = [json.loads(json_str) for json_str in json_list]
    return dict_list