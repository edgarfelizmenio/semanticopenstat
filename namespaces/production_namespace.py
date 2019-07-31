# Production namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
productionNS = Namespace(common_uri + "production#")
productionClass = productionNS["Production"]

# define the properties:
producedAt = productionNS['produced_at']

productionVolume = productionNS['production_volume']
productionCrop = productionNS['production_crop']
productionYear = productionNS['production_year']

productionQuarter = productionNS['production_quarter']
productionSemester = productionNS['production_semester']

schema_triples = [
    # class declarations
    (productionClass, rdfType, owlClass),
    # (productionClass, rdfsSubClassOf, objectClass),

    (producedAt, rdfType, owlObjectProperty),
    (producedAt, rdfsDomain, productionClass),
    (producedAt, rdfsRange, placeClass),

    (productionVolume, rdfType, owlDatatypeProperty),
    (productionVolume, rdfsDomain, productionClass),
    (productionVolume, rdfsRange, xsdDecimal),

    (productionYear, rdfType, owlDatatypeProperty),
    (productionYear, rdfsDomain, productionClass),
    (productionYear, rdfsRange, xsdYear),

    (productionCrop, rdfType, owlObjectProperty),
    (productionCrop, rdfsDomain, productionClass),
    (productionCrop, rdfsRange, cropClass),

    (productionQuarter, rdfType, owlDatatypeProperty),
    (productionQuarter, rdfsDomain, productionClass),
    (productionQuarter, rdfsRange, xsdPositiveInteger),

    (productionSemester, rdfType, owlDatatypeProperty),
    (productionSemester, rdfsDomain, productionClass),
    (productionSemester, rdfsRange, xsdPositiveInteger),


]
