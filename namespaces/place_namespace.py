# Place Namespace
from .common_namespace import *

# define the namespace and classes:
placeNS = Namespace(common_uri + "place#")
placeClass = placeNS["Place"]
countryClass = placeNS["Country"]
regionClass = placeNS["Region"]
provinceClass = placeNS["Province"]
cityClass = placeNS["City"]

locatedIn = placeNS["located_in"]

# create new relationship for "inside"

schema_triples = [
    # class declarations
    # (placeClass, rdfsSubClassOf, objectClass),
    (countryClass, rdfsSubClassOf, placeClass),
    (regionClass, rdfsSubClassOf, placeClass),
    (provinceClass, rdfsSubClassOf, placeClass),
    (cityClass, rdfsSubClassOf, placeClass),

    # declare same as relationships
    # (cropClass, owlSameAs, cropDBO["Crop"]),
    (countryClass, owlSameAs, dbpediaNS["Place"]),
    (countryClass, owlSameAs, dbpediaNS["Country"]),
    (regionClass, owlSameAs, dbpediaNS["Region"]),
    (provinceClass, owlSameAs, dbpediaNS["Province"]),
    (cityClass, owlSameAs, dbpediaNS["City"]),

    # declare "located at" relationships
    # ()
    (locatedIn, rdfType, owlObjectProperty),
    (locatedIn, rdfsDomain, placeClass),
    (locatedIn, rdfsRange, placeClass)

]