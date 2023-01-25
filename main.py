import json
import os
import pandas as pd
from activity_per_person import average_activity

address_folder_mono = "D://GDrive/Mono"
address_folder_multi = "D://GDrive/Multi"

""" This loop designed to get some basic information about Mono repositories"""

df_mono = pd.DataFrame(
    columns=['Repo name', 'User name', 'Team size', 'Langauge', 'Star count', 'Fork count', 'Commit count', 'Amount of active days'])

dict_list = []

""" 
Mono repositories
Same code also can be implemented to Multi repositories after few changes 
"""
# for each_file in os.listdir(address_folder_mono):
#     if '.json' in each_file:
#         with open(address_folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             dict_mono = {'Repo name': '', 'User name': '', 'Team size': '', 'Langauge': '', 'Star count': '',
#                          'Fork count': '', 'Commit count': '', 'Amount of active days': ''}
#
#             dict_mono['Repo name'] = file_content['repo_name']
#             dict_mono['User name'] = file_content['user_name']
#             dict_mono['Team size'] = file_content['size']
#             dict_mono['Langauge'] = file_content['languages']
#             dict_mono['Star count'] = file_content['star_count']
#             dict_mono['Fork count'] = file_content['fork_count']
#             dict_mono['Commit count'] = len(file_content['commits'])
#             dict_mono['Amount of active days'] = len(file_content['activity'])
#
#             dict_list.append(dict_mono)
#
# df_mono = pd.DataFrame.from_records(dict_list)
#
# print(df_mono.head(10))


""" Measuring Activity per person """

# This is an example file for the testing of scripts
file_path = 'D://GDrive/Mono/7-wonders-capstone--7-wonders-capstone.json'

with open(file_path, 'r', encoding="utf8") as file:
    file_content = json.load(file)

    for each_contributor in file_content['contributors']:
        # print(each_contributor['contributor_name'])
        average_activity(file_content['commits'], file_content['activity_bursts'], each_contributor['contributor_name'])





