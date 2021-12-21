import json
import pandas as pd

def jsonl_to(file_path:str, destination_type:str = "list"):
    '''
    Params:
        file_path: jsonl file path as string
        destination_type : type of object intended to return
    Returns:
        dict_list or pandas dataframe
    '''
    with open(file_path, 'r') as fp:
        json_list = list(fp)
    dict_list = [json.loads(json_str) for json_str in json_list]
    
    if destination_type == "list":
        return dict_list
    
    elif destination_type == "pandas":
        keys = list(dict_list[0].keys())
        df = pd.DataFrame(data=dict_list,columns=keys)
        return df
    
    else:
        raise Exception("destination_type should be \"list\" or \"pandas\".")