# Stock namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
stockNS = Namespace(common_uri + "stock#")
stockClass = stockNS["Stock"]

# define the properties:
hasStock = stockNS['has_stock']

stockAmount = stockNS['stock_amount']
stockCrop = stockNS['stock_crop']
stockSector = stockNS['stock_sector']
stockYear = stockNS['stock_year']
stockMonth = stockNS['stock_month']

schema_triples = [
    # class declarations
    (stockClass, rdfType, owlClass),
    (stockClass, rdfsSubClassOf, objectClass),

    (hasStock, rdfType, owlObjectProperty),
    (hasStock, rdfsDomain, placeClass),
    (hasStock, rdfsRange, stockClass),

    (stockAmount, rdfType, owlDatatypeProperty),
    (stockAmount, rdfsDomain, stockClass),
    (stockAmount, rdfsRange, xsdDecimal),

    (stockYear, rdfType, owlDatatypeProperty),
    (stockYear, rdfsDomain, stockClass),
    (stockYear, rdfsRange, xsdYear),

    (stockMonth, rdfType, owlDatatypeProperty),
    (stockMonth, rdfsDomain, stockClass),
    (stockMonth, rdfsRange, xsdMonth),

    (stockCrop, rdfType, owlObjectProperty),
    (stockCrop, rdfsDomain, stockClass),
    (stockCrop, rdfsRange, cropClass),

    (stockSector, rdfType, owlDatatypeProperty),
    (stockSector, rdfsDomain, stockClass),
    (stockSector, rdfsRange, xsdString),

]

