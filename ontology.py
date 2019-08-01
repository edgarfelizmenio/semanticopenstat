
import pprint
import importlib
from rdflib import ConjunctiveGraph

import namespaces
# from namespaces import common_namespace, \
#                 crop_namespace, \
#                 place_namespace, \
#                 harvest_namespace, \
#                 production_namespace \
#                 bearing_trees_namespace
import rdf_common



namespace_module = "namespaces"

schema_triples = []
prefixes = []
print(namespaces.__name__)
modules = [importlib.import_module("{}.{}".format(namespaces.__name__, module_name)) for module_name in namespaces.__all__]
for module in modules:
    print("importing {}.schema_triples...".format(module.__name__))
    schema_triples.extend(module.schema_triples)
    prefixes.extend(module.prefixes)

def use_ontology(graph):
    # pprint.pprint(schema_triples)
    for triple in schema_triples:
        graph.add(triple)

    for namespace, prefix in prefixes:
            graph.namespace_manager.bind(prefix, namespace, True)

def main():
    owl_graph = ConjunctiveGraph()
    use_ontology(owl_graph)
    rdf_common.serialize_rdf_to_file(owl_graph, "ontology.xml", "xml")


if __name__ == '__main__':
    main()
