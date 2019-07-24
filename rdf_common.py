

def serialize_rdf_to_file(rdf_graph, filename, output_format):
    with open(filename, "w") as rdf_file:
        rdf_string = str(rdf_graph.serialize(format=output_format), "utf-8")
        rdf_file.write(rdf_string)