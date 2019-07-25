import csv
import os
import pprint

from rdflib import Namespace, Graph, URIRef, Literal, BNode
from rdflib.namespace import RDF, FOAF, NamespaceManager

from ontology import *
import rdf_common

TREE_INDENT = '..'
BLANK = '..'

RESOURCE = common_namespace.common_uri
DBPEDIA = Namespace('http://dbpedia.org/ontology/')
OBOLIB = Namespace('http://purl.obolibrary.org/obo/')
LOCATED_IN = OBOLIB['RO_0001025']

LOCATION_CLASSES = {
    0: {
        "source": RESOURCE + "countries/{}",
        "type": place_namespace.countryClass,
    },
    1: {
        "source": RESOURCE + "regions/{}",
        "type": place_namespace.regionClass,
    },
    2: {
        "source": RESOURCE + "provinces/{}",
        "type": place_namespace.provinceClass,
    },
    3: {
        "source": RESOURCE + "cities/{}",
        "type": place_namespace.cityClass,
    },
}

CROP_CLASS = {
    "source": RESOURCE + "crops/{}",
    "type": crop_namespace.cropClass,
}

HARVEST_CLASS = {
    "source": RESOURCE + "harvests/{}",
    "type": harvest_namespace.harvestClass
}

def build_crop_rdf(crop_names, name_to_uri_table, uri_to_node_table, rdf_graph):
    for crop_name in crop_names:
        instance_name = CROP_CLASS["source"].format(crop_name.replace(" ", "_").replace("/","%2F"))
        node = URIRef(instance_name)
        name_to_uri_table[crop_name] = instance_name
        uri_to_node_table[instance_name] = node
        rdf_graph.add((node, common_namespace.objectName, Literal(crop_name)))
        rdf_graph.add((node, common_namespace.rdfType, CROP_CLASS["type"]))

def get_depth(current_place):
    depth = 0
    while current_place.startswith(TREE_INDENT):
        depth += 1
        current_place = current_place[2:]
    return depth

def trim_once(place_raw):
    if (place_raw.startswith(TREE_INDENT)):
        place_raw = place_raw[2:]
    return place_raw

def trim(place_raw):
    while place_raw.startswith(TREE_INDENT):
        place_raw = place_raw[2:]
    return place_raw

def get_places(places_raw):
    places = {}
    for place_raw in places_raw:
        places[place_raw] = trim(place_raw)
    return places

def get_place_hierarchy(places_raw, i = 0, depth = 0, places = {}):
    while i < len(places_raw):
        place_raw = places_raw[i]
        current_depth = get_depth(place_raw)
        if current_depth == depth:
            if place_raw in places:
                return i
            places[trim(place_raw)] = {}
            parent = place_raw
            i += 1
        elif current_depth > depth:
            i = get_place_hierarchy(places_raw, i, depth + 1, places[trim(parent)])
        else:
            return i

def insert_place_node(name, name_to_uri_table, uri_to_node_table, rdf_graph, depth, parent = None):
    instance_name = LOCATION_CLASSES[depth]["source"].format(name.replace(" ", "_").replace("/","\%2F"))
    node = URIRef(instance_name)

    name_to_uri_table[name] = instance_name
    uri_to_node_table[instance_name] = node

    rdf_graph.add((node, common_namespace.objectName, Literal(name)))
    rdf_graph.add((node, common_namespace.rdfType, LOCATION_CLASSES[depth]["type"]))
    if parent is not None:
        rdf_graph.add((node, place_namespace.locatedIn, uri_to_node_table[parent]))

    return instance_name

def build_hierarchy_rdf(place_hierarchy, name_to_uri_table, uri_to_node_table, rdf_graph, depth = 0, parent=None):
    for key, value in place_hierarchy.items():
        parent_instance = insert_place_node(key, name_to_uri_table, uri_to_node_table, rdf_graph, depth, parent)
        if len(value) > 0:
            for child in value.keys():
                build_hierarchy_rdf({child: place_hierarchy[key][child]}, name_to_uri_table, uri_to_node_table, rdf_graph, depth + 1, parent_instance)

def build_harvest_rdf(headers, lines, places_to_uri_table, places_uri_to_nodes_table, crops_to_uri_table, crops_uri_to_nodes_table, rdf_graph):
    for i in range(2,len(headers)):
        headers[i] = int(headers[i])
    print(headers)
    for line in lines:
        crop = line[0]
        place = trim(line[1])
        crop_node = crops_uri_to_nodes_table[crops_to_uri_table[line[0]]]
        place_node = places_uri_to_nodes_table[places_to_uri_table[trim(line[1])]]
        
        for i in range(2, len(headers)):
            year = headers[i]
            harvest_area = trim(line[i])
            if len(harvest_area) > 0:
                harvest_area = float(harvest_area)
                harvest_instance_name = "{}-{}-harvest-{}".format(place.replace(" ","_"), crop.replace(" ","_").replace("/", "%2F"), year)
                harvest_node = URIRef(HARVEST_CLASS["source"].format(harvest_instance_name))
                
                rdf_graph.add((harvest_node, common_namespace.rdfType, HARVEST_CLASS["type"]))
                rdf_graph.add((harvest_node, harvest_namespace.harvestCrop, crop_node))
                rdf_graph.add((harvest_node, harvest_namespace.harvestYear, Literal(year)))
                rdf_graph.add((harvest_node, harvest_namespace.harvestArea, Literal(harvest_area)))
                # rdf_graph.add((harvest_node, URIRef("unit"), Literal("sq.m.")))
                rdf_graph.add((place_node, harvest_namespace.hasHarvest, harvest_node))

def extract(file_key, input_path, output_path, rdf_graph):
    data_file_names = []
    for data_file_name in os.listdir(input_path):
        if data_file_name.startswith(file_key) and data_file_name.endswith('.csv'):
            data_file_names.append(data_file_name)

    lines = []
    for data_file_name in data_file_names:
        input_filename = os.path.join(input_path, data_file_name)
        print("input_file_name:", input_filename)
        with open(input_filename) as input_file:
            stream = csv.reader(input_file)
            title = next(stream)[0]
            next(stream)
            headers = next(stream)
            lines_partial = list(stream)
            lines += lines_partial

    CROPS = list(set([line[0] for line in lines]))
    CROPS.sort()

    crops_to_uri_table = {}
    crops_uri_to_nodes_table = {}
    build_crop_rdf(CROPS, crops_to_uri_table, crops_uri_to_nodes_table, rdf_graph)
    places_raw = [line[1] for line in lines]

    place_hierarchy = {}
    get_place_hierarchy(places_raw, 0, 0, place_hierarchy)

    places_to_uri_table = {}
    places_uri_to_nodes_table = {}
    build_hierarchy_rdf(place_hierarchy, places_to_uri_table, places_uri_to_nodes_table, rdf_graph)
    build_harvest_rdf(headers, lines, places_to_uri_table, places_uri_to_nodes_table, crops_to_uri_table, crops_uri_to_nodes_table, rdf_graph)
    rdf_common.serialize_rdf_to_file(rdf_graph, os.path.join(output_path, file_key + ".rdf"), "xml")

def main():
    csv_data_files = os.path.join('data', 'raw', 'agriculture, forestries, fisheries', 'crops')
    rdf_data_files = os.path.join('data', 'rdf', 'agriculture, forestries, fisheries', 'crops')

    file_key = os.path.splitext(os.path.basename(__file__))[0]    
    output_filename = file_key + '.rdf'

    rdf_graph = Graph()
    rdf_graph.namespace_manager.bind("obo", OBOLIB, replace=True)
    use_ontology(rdf_graph)



    rdf_common.serialize_rdf_to_file(rdf_graph, output_filename, "xml")