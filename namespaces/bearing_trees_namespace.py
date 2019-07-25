# BearingTrees namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
bearingTreesNS = Namespace(common_uri + "bearing_trees#")
bearingTreesClass = bearingTreesNS["BearingTrees"]

# define the properties:
hasBearingTrees = bearingTreesNS['has_bearing_trees']

bearingTreesNumber = bearingTreesNS['bearing_trees_number']
bearingTreesCrop = bearingTreesNS['bearing_trees_crop']
bearingTreesYear = bearingTreesNS['bearing_trees_year']

schema_triples = [
    # class declarations
    (bearingTreesClass, rdfType, owlClass),
    (bearingTreesClass, rdfsSubClassOf, objectClass),

    (hasBearingTrees, rdfType, owlObjectProperty),
    (hasBearingTrees, rdfsDomain, placeClass),
    (hasBearingTrees, rdfsRange, bearingTreesClass),

    (bearingTreesNumber, rdfType, owlDatatypeProperty),
    (bearingTreesNumber, rdfsDomain, bearingTreesClass),
    (bearingTreesNumber, rdfsRange, xsdDecimal),

    (bearingTreesYear, rdfType, owlDatatypeProperty),
    (bearingTreesYear, rdfsDomain, bearingTreesClass),
    (bearingTreesYear, rdfsRange, xsdYear),

    (bearingTreesCrop, rdfType, owlObjectProperty),
    (bearingTreesCrop, rdfsDomain, bearingTreesClass),
    (bearingTreesCrop, rdfsRange, cropClass),

]
