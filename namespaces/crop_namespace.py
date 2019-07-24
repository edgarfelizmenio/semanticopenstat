# Crop Namespace
from .common_namespace import *

# define the namespace and classes:
cropNS = Namespace(common_uri + "crop#")
cropClass = cropNS["Crop"]

crop_schema_triples = [
    # class declarations
    (cropClass, rdfsSubClassOf, objectClass),
    (cropClass, owlSameAs, dbpediaNS["Crop"]),
]