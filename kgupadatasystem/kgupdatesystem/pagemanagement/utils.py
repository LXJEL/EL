from random import sample
import json


def getType(eOrr, id):
    if eOrr == 'e':
        id_path = './StaticFile/DB300K/entityId_map.txt'
    else:
        id_path = './StaticFile/DB300K/relationId_map.txt'
    with open(id_path, 'r', encoding='UTF-8') as id_list:
        for id_data in id_list:
            if id_data.split('\t')[0] == str(id):
                return id_data.strip('\n').split('\t')[1].replace('-', '_').replace('(', '').replace(')', '').replace(',', '')
    id_list.close()
    return ''


def get_kg_fromyago(limit):
    with open("./StaticFile/DB300K/neo4j/graph.json", "r") as f:
        data = json.load(f)
        node_all_list = data['Vertices']
        link_all_list = data["Edges"]
    node_list = []
    link_list = sample(link_all_list, limit)
    node_id_list = []
    for link in link_list:
        node_id_list.append(link['start_id'])
        node_id_list.append(link['target_id'])
    node_id_list = set(node_id_list)

    for node in node_all_list:
        if node['id'] in node_id_list:
            node['entity_type'] = getType('e', node['entity_type'])
            node_list.append(node)
    for link in link_list:
        link['relationship_type'] = getType('r', link['relationship_type'])
    # print(link_list,node_list)
    return node_list, link_list

# get_kg_fromyago(2)