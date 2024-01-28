import numpy as np
import re


def convert_string_to_01_list(hp_st):
    re = map(lambda x: '0' if x=='P' else '1', hp_st)
    return ''.join(list(re))

def search_blocks(seq: str):
    result = {}
    pattern = re.compile(r'1(0(00)*1)*')
    xy_group = 0
    y_li = []
    x_li = []
    matches = list(pattern.finditer(seq))
    half_matches = int(len(matches)/2)
    
    for match in matches[:half_matches]:
        start_index = match.start()
        matched_text = match.group()
        end_index = match.end()-1
        segment = (start_index, end_index)
        if(xy_group==0):
            y_li.append(segment)
        elif(xy_group==1):
            x_li.append(segment)
        xy_group = (xy_group+1)%2
        # print(f"Matched '{matched_text}' starting at index {start_index}")
    result.update({"a": {"x": x_li, "y": y_li}})
    
    y_li = []
    x_li = []
    xy_group = 0
    for match in matches[half_matches:]:
        start_index = match.start()
        matched_text = match.group()
        end_index = match.end()-1
        segment = (start_index, end_index)
        if(xy_group==0):
            y_li.append(segment)
        elif(xy_group==1):
            x_li.append(segment)
        xy_group = (xy_group+1)%2
        # print(f"Matched '{matched_text}' starting at index {start_index}")
    result.update({"b": {"x": x_li, "y": y_li}})    
    
    return result



# example output
# {"a": {"x":[(2,6)], "y":[]}, "b": {"x":[], "y":[7,7]}, "ori": [0,0,1,0,0,0,1,1]}

# search_blocks("s")



def get_blocked_data():
    data = []
    sample = "0101000111100100000001101011000101101001"
    with open("row_data.txt") as file:
        for sequence in file: 
            s_01 = convert_string_to_01_list(sequence)
            re = search_blocks(s_01)
            re.update({"ori": s_01})
            data.append(re)
            # print(re)
        
get_blocked_data()