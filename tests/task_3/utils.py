import json
import os


def get_breeds_list():
    file_dir = os.path.dirname(__file__)
    file_name = 'final_breeds_list.json'
    with open(os.path.join(file_dir, file_name), 'r') as f:
        breed_list = json.load(f)
    return breed_list['message']


def get_sub_breeds_list():
    breed_list = get_breeds_list()
    sub_breed_list = [(k, v) for k, v in breed_list.items() if len(v) > 0]
    return sub_breed_list


breeds_list = list(get_breeds_list())


sub_breeds_list = get_sub_breeds_list()
