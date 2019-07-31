# Fertilizer namespace
from .common_namespace import *
from .crop_namespace import *
from .place_namespace import *

# define the namespace and classes:
fertilizerNS = Namespace(common_uri + "fertilizer#")
fertilizerClass = fertilizerNS["Fertilizer"]

# define the properties:
appliedAt = fertilizerNS['applied_at']
areaApplied = fertilizerNS['fertilizer_area'] # literal
averageQtyApplied = fertilizerNS['average_qty_applied'] # literal
ureaQty = fertilizerNS['urea_qty'] # literal
ammosulQty = fertilizerNS['ammosul_qty'] # literal
ammophosQty = fertilizerNS['ammophos_qty'] # literal
completeQty = fertilizerNS['complete_qty'] # literal
othersQty = fertilizerNS['others_qty'] # literal
areaHarvested = fertilizerNS['area_harvested'] # literal
yearApplied = fertilizerNS['year_applied'] # literal
cropApplied = fertilizerNS['crop_applied']

schema_triples = [
    # class declarations
    (fertilizerClass, rdfType, owlClass),
    # (fertilizerClass, rdfsSubClassOf, objectClass),

    (appliedAt, rdfType, owlObjectProperty),
    (appliedAt, rdfsDomain, fertilizerClass),
    (appliedAt, rdfsRange, placeClass),

    (areaApplied, rdfType, owlDatatypeProperty),
    (areaApplied, rdfsDomain, fertilizerClass),
    (areaApplied, rdfsRange, xsdDecimal),

    (averageQtyApplied, rdfType, owlDatatypeProperty),
    (averageQtyApplied, rdfsDomain, fertilizerClass),
    (averageQtyApplied, rdfsRange, xsdDecimal),

    (ureaQty, rdfType, owlDatatypeProperty),
    (ureaQty, rdfsDomain, fertilizerClass),
    (ureaQty, rdfsRange, xsdDecimal),

    (ammosulQty, rdfType, owlDatatypeProperty),
    (ammosulQty, rdfsDomain, fertilizerClass),
    (ammosulQty, rdfsRange, xsdDecimal),

    (ammophosQty, rdfType, owlDatatypeProperty),
    (ammophosQty, rdfsDomain, fertilizerClass),
    (ammophosQty, rdfsRange, xsdDecimal),

    (completeQty, rdfType, owlDatatypeProperty),
    (completeQty, rdfsDomain, fertilizerClass),
    (completeQty, rdfsRange, xsdDecimal),

    (othersQty, rdfType, owlDatatypeProperty),
    (othersQty, rdfsDomain, fertilizerClass),
    (othersQty, rdfsRange, xsdDecimal),

    (areaHarvested, rdfType, owlDatatypeProperty),
    (areaHarvested, rdfsDomain, fertilizerClass),
    (areaHarvested, rdfsRange, xsdDecimal),

    (yearApplied, rdfType, owlDatatypeProperty),
    (yearApplied, rdfsDomain, fertilizerClass),
    (yearApplied, rdfsRange, xsdYear),

    (cropApplied, rdfType, owlObjectProperty),
    (cropApplied, rdfsDomain, fertilizerClass),
    (cropApplied, rdfsRange, cropClass),

]
