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
person_uri = base_uri + 'person/'
schema_person_uri = 'https://schema.org/Person'
role_uri = 'https://data.ehu.eus/bcitr/role/' # https://data.ehu.eus/bcitr/role/[normalised-person-name][officer|president|director|...][dates]
company_uri = base_uri + "company/"

has_role_prop = 'http://ehu.eus/tro#has_role'
person_name_prop = "http://www.w3.org/ns/person#name"
person_profile_prop = "http://ehu.eus/tro#profile_url"

for row in input_file:
    # for k, v in row.items():
    #     print(k,v)
    name = row['name']
    profile = row['profile']
    entity = row['entity']

    # Codigo repetido de Registro Licitadores: mala idea
    for row in input_file_licitadores:
        entity_id = row['Número inscripción']
        entity_name = row['Denominación social']
        if entity_name == entity:
            print(entity_id)
            entity_uri = company_uri + entity_id


    # TODO: https://github.com/mikel-egana-aranguren/BasqueCountryInstitutionsTransparentRelationsGraph/issues/9
    normalised_name = name.replace(" ", "-").lower()
    person_uri_name = person_uri + normalised_name
    output_graph.add((URIRef(person_uri_name), RDFS.label, Literal(name)))
    output_graph.add((URIRef(person_uri_name), RDF.type, URIRef(schema_person_uri)))
    output_graph.add((URIRef(person_uri_name), URIRef(person_name_prop), Literal(name)))
    output_graph.add((URIRef(person_uri_name), URIRef(person_profile_prop), Literal(profile)))
    output_graph.add((URIRef(person_uri_name), URIRef(), URIRef()))

output_graph.serialize(destination='People.nq', format='nquads', encoding="utf-8")



