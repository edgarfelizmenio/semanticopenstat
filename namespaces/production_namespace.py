# Production namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
productionNS = Namespace(common_uri + "production#")
productionClass = productionNS["Production"]

# define the properties:
hasProduction = productionNS['has_production']

productionVolume = productionNS['production_volume']
productionCrop = productionNS['production_crop']
productionYear = productionNS['production_year']

schema_triples = [
    # class declarations
    (productionClass, rdfType, owlClass),
    (productionClass, rdfsSubClassOf, objectClass),

    (hasProduction, rdfType, owlObjectProperty),
    (hasProduction, rdfsDomain, placeClass),
    (hasProduction, rdfsRange, productionClass),

    (productionVolume, rdfType, owlDatatypeProperty),
    (productionVolume, rdfsDomain, productionClass),
    (productionVolume, rdfsRange, xsdDecimal),

    (productionYear, rdfType, owlDatatypeProperty),
    (productionYear, rdfsDomain, productionClass),
    (productionYear, rdfsRange, xsdYear),

    (productionCrop, rdfType, owlObjectProperty),
    (productionCrop, rdfsDomain, productionClass),
    (productionCrop, rdfsRange, cropClass),

]
