#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
# https://github.com/SemanticLab/simple-csv-to-rdf
# pip install rdflib
##################################################

import csv
from rdflib import ConjunctiveGraph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD, DC, DCTERMS, VOID

def normalise_name(name):
   return name.replace(" ", "-").lower().replace(".", "-")
   
input_file = csv.DictReader(open("People.csv"))

input_file_licitadores = csv.DictReader(open("../RegistroLicitadoresYEmpresasClasificadas/Empresas-2023-03-05.csv"))

output_graph = ConjunctiveGraph(identifier="https://data.ehu.eus/bcitr/people/graph")

# TODO: https://github.com/mikel-egana-aranguren/BasqueCountryInstitutionsTransparentRelationsGraph/issues/1
base_uri = 'https://data.ehu.eus/bcitr/'
person_uri = base_uri + 'person/'
role_uri = 'https://data.ehu.eus/bcitr/role/'
company_uri = base_uri + "company/"

for row in input_file:
    # for k, v in row.items():
    #     print(k,v)
    name = row['name']
    profile = row['profile']
    entity = row['entity']
    role = row['role']
    startdate = row['start-date']
    enddate = row['end-date']
    entity = row['entity']
    evidence = row['evidence']

    # Codigo repetido de Registro Licitadores: mala idea
    for row in input_file_licitadores:
        entity_id = row['Número inscripción']
        entity_name = row['Denominación social']
        if entity_name == entity:
            entity_uri = company_uri + entity_id

    # TODO: https://github.com/mikel-egana-aranguren/BasqueCountryInstitutionsTransparentRelationsGraph/issues/9

    normalised_name = normalise_name(name)
    person_uri_name = person_uri + normalised_name
    output_graph.add((URIRef(person_uri_name), RDFS.label, Literal(name)))
    output_graph.add((URIRef(person_uri_name), RDF.type, URIRef('https://schema.org/Person')))
    output_graph.add((URIRef(person_uri_name), URIRef("http://www.w3.org/ns/person#name"), Literal(name)))
    output_graph.add((URIRef(person_uri_name), URIRef("http://ehu.eus/tro#profile_url"), Literal(profile)))

    # https://data.ehu.eus/bcitr/role/[normalised-person-name][officer|president|director|...][dates]
    role_def_uri = role_uri + normalised_name + "-" + normalise_name(role) + "-" + startdate + "-" + enddate + "-" + normalise_name(entity)[:-1] + ""

    output_graph.add((URIRef(person_uri_name), URIRef("http://ehu.eus/tro#has_role"), URIRef(role_def_uri)))
    if role == "Manager":
        output_graph.add((URIRef(role_def_uri), RDF.type, URIRef("http://ehu.eus/tro#Manager")))
    output_graph.add((URIRef(role_def_uri), URIRef("http://ehu.eus/tro#start_date"), Literal(startdate)))
    output_graph.add((URIRef(role_def_uri), URIRef("http://ehu.eus/tro#end_date"), Literal(enddate)))
    output_graph.add((URIRef(role_def_uri), URIRef("http://ehu.eus/tro#in_entity"), URIRef(entity_uri)))
    output_graph.add((URIRef(role_def_uri), URIRef("http://ehu.eus/tro#with_evidence"), URIRef(evidence)))

    # TODO: generalizar
    output_graph.add((URIRef(evidence), RDF.type, URIRef("http://ehu.eus/tro#PublicProfile")))
    output_graph.add((URIRef(evidence), URIRef("http://ehu.eus/tro#url"), Literal(evidence)))



output_graph.serialize(destination='People.nq', format='nquads', encoding="utf-8")



