
import pprint
from rdflib import ConjunctiveGraph

from namespaces import common_namespace, crop_namespace, place_namespace, harvest_namespace

import rdf_common

schema_triples = []
schema_triples.extend(common_namespace.common_schema_triples)
schema_triples.extend(crop_namespace.crop_schema_triples)
schema_triples.extend(place_namespace.place_schema_triples)
schema_triples.extend(harvest_namespace.harvest_schema_triples)

def use_ontology(graph):
    # pprint.pprint(schema_triples)
    for triple in schema_triples:
        graph.add(triple)

def main():
    owl_graph = ConjunctiveGraph()
    use_ontology(owl_graph)
    rdf_common.serialize_rdf_to_file(owl_graph, "ontology.xml", "xml")


if __name__ == '__main__':
    main()
