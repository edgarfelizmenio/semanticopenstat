import os

DATA_FOLDER = "data"
PARSERS_FOLDER = "parsers"

RAW_DATA_FOLDER = os.path.join(DATA_FOLDER, "raw") 
RDF_DATA_FOLDER = os.path.join(DATA_FOLDER, "rdf")

PARSERS_PATH = "parsers"
AGRI_PATH = "agriculture, forestries, fisheries"

DOMAINS = {
    "crops": {
        "directories": {
            "input_path": os.path.join(RAW_DATA_FOLDER, AGRI_PATH, "crops"),
            "output_path": os.path.join(RDF_DATA_FOLDER, AGRI_PATH, "crops"),
            "parsers_path": '.'.join([PARSERS_FOLDER, AGRI_PATH.replace(", ", "_"), "crops"]),
        },
        "databases": [{
            "file_key": "2E4EAHO0",
            "title": "Other Crops: Area Planted/Harvested, by Region and by Province, 1990-2018",
            "parser": "_2E4EAHO0"
        }, {
            "file_key": "2E4EVCP1",
            "title": "Other Crops: Volume of Production, by Region and by Province, 1990-2018",
            "parser": "_2E4EVCP1"
        }, {
            "file_key": "2E4ENBT0",
            "title": "Other Crops: Number of Bearing Trees/Hills/Vines, by Region and by Province, 1990-2018",
            "parser": "_2E4ENBT0"
        }, {
            "file_key": "2E4ENVCP",
            "title": "Palay and Corn: Volume of Production",
            "parser": "_2E4ENVCP"
        }]
    },
}

# for domain in DOMAINS.values():
#     for name, path in domain["directories"].items():
        # if not os.path.exists(path):
        #     os.makedirs(path)
