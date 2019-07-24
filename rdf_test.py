import rdflib
g=rdflib.Graph()
g.load('https://data.gov.ph/dataset/responsible-parenthood-and-family-planning-rpfp-demand-generation-report.xml')

for s,p,o in g:
    print("Subject:", s)
    print("Predicate:", p)
    print("Object:", o)    
    # print()