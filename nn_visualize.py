#!/usr/bin/python3

import graphviz as gv

class ann_visualize():
    def __init__(self):
        self.network = gv.Graph()

    def __str__(self):
        return "NN Visualizer"

    def add_layer(self, layer_name, nodes):
        pass

    def visualize(self):
        self.network.view()

def add_layer(network, layer_name, nodes):
    with network.subgraph(name=f'layer_{layer_name}') as layer:
        if nodes > 10:
            layer.attr(labeljust='right', labelloc='bottom', label='+'+str(nodes - 10))
            nodes = 10
        layer.attr(body=layer_name)

        for i in range(nodes):
            layer.node(f'{layer_name}_{i}', style='filled', fillcolor='yellow')

    return network

network = gv.Digraph("NN", directory='graphs', format='png',
              graph_attr=dict(ranksep='2', rankdir='LR', color='black', splines='line'),
              node_attr=dict(label='', shape='circle', width='0.5'))

global input_nodes = 12
global hidden_nodes = 4
global output_nodes = 4

add_layer(network, 'input', input_nodes)
add_layer(network, 'hidden', hidden_nodes)
add_layer(network, 'output', output_nodes)

for i in range(input_nodes):
    for h in range(hidden_nodes):
        network.edge(f'input_{i}', f'hidden_{h}')

for h in range(hidden_nodes):
    for o in range(output_nodes):
        network.edge(f'hidden_{h}', f'output_{o}')

network.view()