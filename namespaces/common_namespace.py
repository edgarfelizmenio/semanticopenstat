from rdflib import Namespace, Literal

# define the OWL URIs
owlNS = Namespace("http://www.w3.org/2002/07/owl#")
owlClass = owlNS["Class"]
owlObjectProperty = owlNS["ObjectProperty"]
owlDatatypeProperty = owlNS["DatatypeProperty"]
owlSameAs = owlNS["sameAs"]

# define RDF URIs
rdfNS = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfProperty = rdfNS["Property"]
rdfType = rdfNS["Type"]

# define RDFS URIs
rdfsNS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
rdfsSubClassOf = rdfsNS["subClassOf"]
rdfsDomain = rdfsNS["domain"]
rdfsRange = rdfsNS["range"]

# define XSD URIs
xsdNS = Namespace("http://www.w3.org/2001/XMLSchema#")
xsdString = xsdNS["string"]
xsdDecimal = xsdNS["decimal"]
xsdYear = xsdNS["gYear"]
xsdMonth = xsdNS["gMonth"]
xsdPositiveInteger = xsdNS["positiveInteger"]

# import third party ontologies for the sameas rule
dbpediaNS = Namespace("http://dbpedia.org/ontology/")

def isSubClassOf(subClass, superClass, graph):
    if subClass == superClass: return True
    for parentClass in graph.objects(subClass, rdfsSubClassOf):
        if isSubClassOf(parentClass, superClass, graph): return True
    return False

def findInstances(queryClass, graph, instances=None):
    if instances is None: instances = set()
    for instance in graph.subjects(rdfType, queryClass): 
        instances.add(instance)
    for subClass in graph.subjects(rdfsSubClassOf, queryClass):
        instances.update(findInstances(subClass, graph, instances))
    return instances

common_uri = "http://kaistwebeng.org/semanticopenstat/"
commonNS = Namespace(common_uri + "common#")
objectClass = commonNS['Object']
objectName = commonNS['name']

schema_triples = [
    (objectClass, rdfType, owlClass),

    (commonNS['name'], rdfType, owlDatatypeProperty),
    (commonNS['name'], rdfsDomain, objectClass),
    (commonNS['name'], rdfsRange, xsdString),
]
