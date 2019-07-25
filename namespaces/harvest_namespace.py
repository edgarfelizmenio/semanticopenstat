# Harvest namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
harvestNS = Namespace(common_uri + "harvest#")
harvestClass = harvestNS["Harvest"]

# define the properties:
hasHarvest = harvestNS['has_harvest']

harvestArea = harvestNS['harvest_area']
harvestCrop = harvestNS['harvest_crop']
harvestYear = harvestNS['harvest_year']

harvest_schema_triples = [
    # class declarations
    (harvestClass, rdfType, owlClass),
    (harvestClass, rdfsSubClassOf, objectClass),

    (hasHarvest, rdfType, owlObjectProperty),
    (hasHarvest, rdfsDomain, placeClass),
    (hasHarvest, rdfsRange, harvestClass),

    (harvestArea, rdfType, owlDatatypeProperty),
    (harvestArea, rdfsDomain, harvestClass),
    (harvestArea, rdfsRange, xsdDecimal),

    (harvestYear, rdfType, owlDatatypeProperty),
    (harvestYear, rdfsDomain, harvestClass),
    (harvestYear, rdfsRange, xsdYear),

    (harvestCrop, rdfType, owlObjectProperty),
    (harvestCrop, rdfsDomain, harvestClass),
    (harvestCrop, rdfsRange, cropClass),

]