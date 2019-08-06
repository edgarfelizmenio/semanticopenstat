# Harvest namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
harvestNS = Namespace(common_uri + "harvest#")
harvestClass = harvestNS["Harvest"]

# define the properties:
harvestedAt = harvestNS['harvested_at']

harvestArea = harvestNS['harvest_area']
harvestCrop = harvestNS['harvest_crop']
harvestYear = harvestNS['harvest_year']

harvestQuarter = harvestNS['harvest_quarter']
harvestSemester = harvestNS['harvest_semester']

schema_triples = [
    # class declarations
    (harvestClass, rdfType, owlClass),
    # (harvestClass, rdfsSubClassOf, objectClass),

    (harvestedAt, rdfType, owlObjectProperty),
    (harvestedAt, rdfsDomain, harvestClass),
    (harvestedAt, rdfsRange, placeClass),

    (harvestArea, rdfType, owlDatatypeProperty),
    (harvestArea, rdfsDomain, harvestClass),
    (harvestArea, rdfsRange, xsdDecimal),

    (harvestYear, rdfType, owlDatatypeProperty),
    (harvestYear, rdfsDomain, harvestClass),
    (harvestYear, rdfsRange, xsdYear),

    (harvestCrop, rdfType, owlObjectProperty),
    (harvestCrop, rdfsDomain, harvestClass),
    (harvestCrop, rdfsRange, cropClass),

    (harvestQuarter, rdfType, owlDatatypeProperty),
    (harvestQuarter, rdfsDomain, harvestClass),
    (harvestQuarter, rdfsRange, xsdPositiveInteger),

    (harvestSemester, rdfType, owlDatatypeProperty),
    (harvestSemester, rdfsDomain, harvestClass),
    (harvestSemester, rdfsRange, xsdPositiveInteger),

]

prefixes = [
    (harvestNS, "harvest"),
]