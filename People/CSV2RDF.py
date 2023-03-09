#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
# https://github.com/SemanticLab/simple-csv-to-rdf
# pip install rdflib
##################################################

import csv
from rdflib import ConjunctiveGraph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD, DC, DCTERMS, VOID

input_file = csv.DictReader(open("People.csv"))

input_file_licitadores = csv.DictReader(open("../RegistroLicitadoresYEmpresasClasificadas/Empresas-2023-03-05.csv"))

output_graph = ConjunctiveGraph(identifier="https://data.ehu.eus/bcitr/people/graph")

# TODO: https://github.com/mikel-egana-aranguren/BasqueCountryInstitutionsTransparentRelationsGraph/issues/1
base_uri = 'https://data.ehu.eus/bcitr/'
person_uri = base_uri + "person/"
schema_person_uri = "https://schema.org/Person"

person_name_prop = "http://www.w3.org/ns/person#name"
person_profile_prop = "http://ehu.eus/tro#profile_url"



for row in input_file:
    # for k, v in row.items():
    #     print(k,v)

    name = row['name']
    profile = row['profile']
    # TODO: https://github.com/mikel-egana-aranguren/BasqueCountryInstitutionsTransparentRelationsGraph/issues/9
    normalised_name = name.replace(" ", "-").lower()
    person_uri_name = person_uri + normalised_name
    output_graph.add((URIRef(person_uri_name), RDFS.label, Literal(name)))
    output_graph.add((URIRef(person_uri_name), RDF.type, URIRef(schema_person_uri)))
    output_graph.add((URIRef(person_uri_name), URIRef(person_name_prop), Literal(name)))
    output_graph.add((URIRef(person_uri_name), URIRef(person_profile_prop), Literal(profile)))

output_graph.serialize(destination='People.nq', format='nquads', encoding="utf-8")



