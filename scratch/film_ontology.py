from rdflib import ConjunctiveGraph, Namespace, Literal, BNode

import pprint

# define the OWL, RDF, RDFS, and XSD URIs
owlNS = Namespace("http://www.w3.org/2002/07/owl#")
owlClass = owlNS["Class"]
owlObjectProperty = owlNS["ObjectProperty"]
owlDatatypeProperty = owlNS["DatatypeProperty"]
rdfNS = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfProperty = rdfNS["Property"]
rdfType = rdfNS["Type"]
rdfsNS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
rdfsSubClassOf = rdfsNS["subClassOf"]
rdfsDomain = rdfsNS["domain"]
rdfsRange = rdfsNS["range"]
xsdNS = Namespace("http://www.w3.org/2001/XMLSchema#")
xsdString = xsdNS["string"]

# define the namespace and classes:
filmNS = Namespace("http://www.semprog.com/film#")
objectClass = filmNS["Object"]
personClass = filmNS["Person"]
filmClass = filmNS["Film"]
performanceClass = filmNS["Performance"]
actorClass = filmNS["Actor"]
roleClass = filmNS["Role"]
directorClass = filmNS["Director"]

# define the properties:
name = filmNS["name"]
starring = filmNS["starring"]
hasActor = filmNS["has_actor"]
hasRole = filmNS["has_role"]
directedBy = filmNS["directed_by"]

schemaTriples = [
    # class declarations
    (filmNS['Object'], rdfType, owlClass),
    (filmNS['Person'], rdfType, owlClass),
    (filmNS['Film'], rdfType, owlClass),
    (filmNS['Actor'], rdfType, owlClass),
    (filmNS['Role'], rdfType, owlClass),
    (filmNS['Director'], rdfType, owlClass),
    # (filmNS['Performance'], rdfType, owlClass),
    
    # class heirarchy
    (filmNS['Film'], rdfsSubClassOf, filmNS['Object']),
    (filmNS['Person'], rdfsSubClassOf, filmNS['Object']),
    (filmNS['Actor'], rdfsSubClassOf, filmNS['Person']),
    (filmNS['Role'], rdfsSubClassOf, filmNS['Object']),
    (filmNS['Director'], rdfsSubClassOf, filmNS['Person']),

    # name property
    (filmNS['name'], rdfType, owlDatatypeProperty),
    (filmNS['name'], rdfsDomain, filmNS['Object']),
    (filmNS['name'], rdfsRange, xsdString),

    # starring property
    (filmNS['starring'], rdfType, owlObjectProperty),
    (filmNS['starring'], rdfsDomain, filmNS['Film']),
    (filmNS['starring'], rdfsRange, filmNS['Performance']),

    # hasActor property
    (filmNS['hasActor'], rdfType, owlObjectProperty),
    (filmNS['hasActor'], rdfsDomain, filmNS['Performance']),
    (filmNS['hasActor'], rdfsRange, filmNS['Actor']),

    # hasRole property
    (filmNS['hasRole'], rdfType, owlObjectProperty),
    (filmNS['hasRole'], rdfsDomain, filmNS['Performance']),
    (filmNS['hasRole'], rdfsRange, filmNS['Role']),

    # directedBy property
    (filmNS['directedBy'], rdfType, owlObjectProperty),
    (filmNS['directedBy'], rdfsDomain, filmNS['Film']),
    (filmNS['directedBy'], rdfsRange, filmNS['Director']),

]

graph = ConjunctiveGraph()
for triple in schemaTriples:
    graph.add(triple)

def isSubClassOf(subClass, superClass, graph):
    if subClass == superClass: return True
    for parentClass in graph.objects(subClass, rdfsSubClassOf):
        if isSubClassOf(parentClass, superClass, graph): return True
    return False

pprint.pprint(list(graph.subjects(rdfType, owlClass)))
pprint.pprint(list(graph.subjects(rdfType, owlObjectProperty)))
pprint.pprint(list(graph.subjects(rdfType, owlDatatypeProperty)))

print(isSubClassOf(filmNS['Actor'], filmNS['Person'], graph))
print(isSubClassOf(filmNS['Film'], filmNS['Person'], graph))

owl_filename = "film_ontology.owl"
with open(owl_filename, "w") as owl_file:
    xml_string = str(graph.serialize(format="xml"), "utf-8")
    owl_file.write(xml_string)

# Define a blank node for the performance
performance = BNode('_:perf1')

filmTriples = [
    # Movie
    (filmNS['blade_runner'], rdfType, filmNS['Film']),
    (filmNS['blade_runner'], filmNS['name'], Literal("Blade Runner", datatype=xsdString)),
    (filmNS['blade_runner'], filmNS['starring'], performance),
    (filmNS['blade_runner'], filmNS['directedBy'], filmNS['ridley_scott']),

    # Performance
    (performance, rdfType, filmNS['Performance']),
    (performance, filmNS['hasActor'], filmNS['harrison_ford']),
    (performance, filmNS['hasRole'], filmNS['rick_deckard']),
    # Actor
    (filmNS['harrison_ford'], rdfType, filmNS['Actor']),
    (filmNS['harrison_ford'], filmNS['name'], Literal("Harrison Ford", datatype=xsdString)),
    # Role
    (filmNS['rick_deckard'], rdfType, filmNS['Role']),
    (filmNS['rick_deckard'], filmNS['name'], Literal("Rick Deckard", datatype=xsdString)),
    # Director
    (filmNS['ridley_scott'], rdfType, filmNS['Director']),
    (filmNS['ridley_scott'], filmNS['name'], Literal("Ridley Scott", datatype=xsdString)),
]

for triple in filmTriples:
    graph.add(triple)

def findInstances(queryClass, graph, instances=None):
    if instances is None: instances = set()
    for instance in graph.subjects(rdfType, queryClass): 
        instances.add(instance)
    for subClass in graph.subjects(rdfsSubClassOf, queryClass):
        instances.update(findInstances(subClass, graph, instances))
    return instances

pprint.pprint(findInstances(personClass, graph))

rdf_filename = "film.rdf"
with open(rdf_filename, "w") as rdf_file:
    xml_string = str(graph.serialize(format="xml"), "utf-8")
    rdf_file.write(xml_string)