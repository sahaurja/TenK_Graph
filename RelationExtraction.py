#extract relations from pre-processed SEC-10k text
from openie import StanfordOpenIE
import json
from collections import defaultdict

properties = {
    'openie.affinity_probability_cap': 2 / 3,
}

#sanity check for library
# with StanfordOpenIE(properties=properties) as client:
#     text = 'Barack Obama was born in Hawaii. Richard Manning wrote this sentence.'
#     print('Text: %s.' % text)
#     for triple in client.annotate(text):
#         print('|-', triple)
#try with actual sec 10k

#store relations 
#Item : [all relations]
relations = defaultdict(list)

def get_relations(all_items):
    with StanfordOpenIE(properties = properties) as client:
        for item_name in all_items:
            item_content = all_items[item_name]
            for triple in client.annotate(item_content):
                # print("|-", triple)
                relations[item_name].append(triple)
    #save relations to file
    with open ("relations.json", "w") as file:
        json.dump(relations, file)



with open("resolved_items.json", "r") as file:
    loaded_dict = json.load(file)

# print(loaded_dict["Item 1"])

get_relations(loaded_dict)