#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
# https://github.com/SemanticLab/simple-csv-to-rdf
# pip install rdflib
##################################################

import csv
# from rdflib import Graph, Literal, Namespace, URIRef
from rdflib import ConjunctiveGraph, Literal, Namespace, URIRef

from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD, DC, DCTERMS, VOID

input_file = csv.DictReader(open("Empresas-2023-03-05.csv"))

output_graph = ConjunctiveGraph(identifier="https://data.ehu.eus/bcitr/graph")

base_uri = 'https://data.ehu.eus/bcitr/'

schema_corporation = 'https://schema.org/Corporation'

for row in input_file:
    id = row['Número inscripción']
    name = row['Denominación social']
    company_uri = base_uri + "company/"
    if id != '':
        output_graph.add((URIRef(company_uri + id), RDFS.label, Literal(name, lang='es')))
        output_graph.add((URIRef(company_uri + id), RDF.type, URIRef(schema_corporation)))

output_graph.serialize(destination='Empresas-2023-03-05.nq', format='nquads', encoding="utf-8")
output_graph.serialize(destination='Empresas-2023-03-05.nt', format='nt', encoding="utf-8")