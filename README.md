# Basque Country Institutions Transparent Relations Graph

## Introduction

The aim of this project is to build an [RDF](https://www.w3.org/TR/?filter-tr-name=RDF&status%5B%5D=standard&tags%5B%5D=data) Knowledge Graph (KG) to capture transparent relations involving public institutions from the [Basque Country](https://en.wikipedia.org/wiki/Basque_Country_(autonomous_community). The KG integrates information about entities and individuals that might have a conflict of interest, in order to analyse such information.

**DISCLAIMER:** This graph integrates only publicly available information from legitimate sources (Open Data portals, news, etc.). Therefore the inclusion of a person or entity in this graph is not intended to suggest or imply that they have engaged in illegal or improper conduct.

## Directory structure

* `data/`: data sources (see bellow).
* `deployment/`: deployment of the system storing the data (see bellow).
* `doc`: documentation. 

## Data sources (`data/`)

Each folder represents a data source that will result in a Named Graph in the Triple Store. Thus, regardless of the data source, the data will be converted to RDF following certain conventions (That should be documented soon). Therefore, the `README.md` file in the folder should include, at least:

* Origin of the data.
* URI conventions and ontologies used to produce the RDF.
* Documented program to convert the data to RDF.
* Resulting file in RDF (`nq` for Named Graphs).
* Metadata file in RDF, including pointers to the Named Graph.

See `/People` and `/RegistroLicitadoresYEmpresasClasificadas` for examples.

## Data storage (`deployment/`)

Since RDF is a W3C standard, you should be able to load the resulting RDF files in any Triple Store of your choice. Oxigraph is provided for convenience:

* Run: `docker-compose up`, then check `http://localhost:7878`.
* Upload data: for example `./oxigraph_post_data.sh ex.ttl`.
