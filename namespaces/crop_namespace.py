# Crop Namespace
from .common_namespace import *

# define the namespace and classes:
cropNS = Namespace(common_uri + "crop#")
cropClass = cropNS["Crop"]

schema_triples = [
    # class declarations
    # (cropClass, rdfsSubClassOf, objectClass),
    (cropClass, rdfType, owlClass),
    (cropClass, owlSameAs, dbpediaNS["Crop"]),
]

prefixes = [
    (cropNS, "crop"),
]