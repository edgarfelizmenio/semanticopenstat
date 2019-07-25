import databases
import os
import importlib

from rdflib import ConjunctiveGraph
import rdf_common

# import parsers.agriculture_forestries_fisheries.crops.
# for i in range()
# i = importlib.import_module("matplotlib.text")

rdf_graph = ConjunctiveGraph()

for domain in databases.DOMAINS.values():
    input_path = domain["directories"]["input_path"]
    output_path = domain["directories"]["output_path"]
    for name, path in domain["directories"].items():
        print(path)
    for database in domain["databases"]:
        file_key = database["file_key"]
        print("loading parser ({}) for csv database {}".format(database["parser"], file_key))
        parser_module_path = '.'.join([domain["directories"]["parsers_path"], database["parser"]])
        parser = importlib.import_module(parser_module_path, package=None)
        parser.extract(file_key, input_path, output_path, rdf_graph)

    rdf_common.serialize_rdf_to_file(rdf_graph, "linked_db.rdf", "xml")