#!/usr/bin/python -tt
# Project: data_model_design
# Filename: gen_design_doc.py
# claudia
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "2019-08-11"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
import pygraphviz as pgv
import json
import os
import jinja2
import datetime
import markdown
import weasyprint


# Source Attribution
# https://mikegriffin.ie/blog/20110308-a-graphviz-tutorial


def write_rendered_to_file(full_file_path, content, filename):

    output_filename = os.path.join(full_file_path, filename)
    print(f"Creating rendered Design Document {filename}: \n\tFull Path: {full_file_path}\n")

    with open(output_filename, "w") as outfile:
        content_with_lines = content.splitlines()
        for line in content_with_lines:
            outfile.write(line+'\n')


def render_doc(payload, info, doc_template, debug=False):

    ##############################################
    ### Render the Jinja2 Template with the values
    ##############################################

    cwd = os.path.dirname(os.path.realpath(__file__))
    j2envpath = os.path.join(cwd)
    if debug: print(j2envpath)

    J2ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(j2envpath))
    template_full_path = os.path.join(j2envpath, doc_template)
    if debug:print(template_full_path)

    template = J2ENV.get_template(doc_template)

    rendered = template.render(payload=payload, info=info, template=template)
    if debug: print(rendered)

    return rendered


def gen_diagram(file_name, dot_path='graph.dot'):

    # dot_path = 'graph.dot'

    G = pgv.AGraph(dot_path, directed=True)
    G.graph_attr.update(color='red')

    print(G.string())

    dot_filename = f"{file_name}.dot"
    image_filename = f"{file_name}.png"

    G.write(dot_filename)
    G.layout(prog='dot')
    G.draw(image_filename)

    return dot_filename, image_filename


def load_json(json_payload_file):

    with open(json_payload_file) as payload:
        data = json.load(payload)

    return data


def gen_dot(payload_file):

    G = pgv.AGraph()
    G.graph_attr['label'] = 'ACI Fabric Edge Network Diagram'
    G.graph_attr['fontname'] = 'arial'
    G.graph_attr['splines'] = 'compound'

    node_attributes = {
        'color': "#d3edea",
        'fontname': "arial bold",
        'fontsize': "12",
        'shape': "box",
        'style': "filled"
    }

    #   edge1 [ label="Loop0 1.1.1.1" shape=none image="images/router.png" labelloc=b color="#ffffff"];
    image_node_attributes = {
        'color': "#ffffff",
        'fontname': "arial",
        'fontsize': "12",
        'shape': "none",
        'labelloc': "b"
    }

    data = load_json(payload_file)

    node_list_of_dicts = []
    list_of_nodes = []

    # print(len(data))
    for line in data:
        # print(line.keys())
        # print(line)
        for key in line.keys():
            node_list_of_dicts.append(line[key])

    # print(len(node_list_of_dicts))

    for line in node_list_of_dicts:

        tmp_list = []
        loop = ''

        order = line['order']
        hn = line['hostname']
        desc_text = line['service']['config']

        if line.get('interface'):
            loop = line['interface']['Loopback']

        # print(line['order'])
        # print(line['hostname'])
        # print(desc_text)
        # print(loop)
        # print(line['platform'])
        for key in line['platform'].keys():
            # print(line['platform'][key]['image'])
            image = line['platform'][key]['image']
        # print()

        tmp_list.append(order)
        tmp_list.append(hn)
        tmp_list.append(image)
        tmp_list.append(desc_text)
        tmp_list.append(loop)

        list_of_nodes.append(tmp_list)

    # print(list_of_nodes)

    list_of_nodes.sort(key=lambda x: x[0])

    print(list_of_nodes)

    for node in list_of_nodes:
        # print(node)
        # print(node[1])

        G.add_node(node[1])

        n = G.get_node(node[1])
        n.attr['label'] = node[1]
        n.attr['image'] = node[2]
        n.attr['labelloc'] = "c"
        # n.attr['bgcolor'] = "grey"
        # n.attr['font color'] = "white"
        n.attr['color'] = "#ffffff"

    tmp_list_of_nodes = list_of_nodes

    edges = [
        ("The Internet", "oceana-rtr01"),
        ("The Internet", "oceana-rtr02"),
        ("oceana-rtr01", "ACI Fabric"),
        ("oceana-rtr02", "ACI Fabric"),
        ("ACI Fabric", "Servers and Storage"),
    ]

    for edge in edges:
        G.add_edge(edge)

    dot_source_string = G.string()
    # print(f" DOT Source Strings)

    return dot_source_string


def gen_pdf(md_file):

    # Convert Markdown to HTML
    # https://github.com/ljpengelen/markdown-to-pdf/blob/master/md2pdf.py

    # md_withext = f"{md_file}.md"

    with open(md_file, mode="r", encoding="utf-8") as markdown_file:
        markdown_input = markdown_file.read()

    md2html = markdown.markdown(markdown_input, extensions=["extra", "meta", "tables"])
    html = weasyprint.HTML(string=md2html)
    html.write_pdf(md_file + ".pdf")

def main():


    #######
    ### Generate Design Diagram
    design_drawing_filename = 'ACI_Diagram'
    dot_source = gen_dot(arguments.payload)
    dot_fn, diagram_fn = gen_diagram(design_drawing_filename, dot_source)

    #######
    ### Generate Design Document

    config_template = 'design_summary_report_md_template.j2'
    dattim = str(format(datetime.datetime.now()))

    cfg_dict = load_json(arguments.payload)
    cfginfo_dict = {}

    cfginfo_dict = load_json("doc_info.json")

    cfginfo_dict.update({'hlddiagram': diagram_fn})
    cfginfo_dict.update({'dattim': dattim})

    rendered_cfg = render_doc(cfg_dict, cfginfo_dict, config_template, debug=False)

    # Define Configuration File Name
    _ = diagram_fn.split('.')
    doc_filename = f"{_[0]}_DesignDocument.md"
    doc_fp = os.path.join(".")

    write_rendered_to_file(doc_fp,rendered_cfg,doc_filename)


# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Description",
                                     epilog="Usage: 'python gen_design_doc.py <design payload>' ")

    parser.add_argument('payload', help='Configuration Payload file')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',
    #                     default=False)
    arguments = parser.parse_args()
    main()
