import gzip
import networkx as nx
import plotly.graph_objects as go
import random
import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import community as community_louvain

# Load graph
def load_graph(edge_file):
    G = nx.Graph()
    with gzip.open(edge_file, "rt", encoding="utf-8") as f:
        for line in f:
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)
    return G

G = load_graph("facebook_combined.txt.gz")
partition = community_louvain.best_partition(G)
pos = nx.spring_layout(G, seed=42)

# Unique communities and color map
unique_communities = sorted(set(partition.values()))
print("Detected community labels:", unique_communities)
print("Total number of communities:", len(unique_communities))
print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")

color_map = {com: f"hsl({i * 360 / len(unique_communities)}, 70%, 50%)" for i, com in enumerate(unique_communities)}

# Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def create_figure(selected_community=None):
    # Filter nodes by community if one is selected
    if selected_community is not None:
        nodes_to_draw = [n for n in G.nodes if partition[n] == selected_community]
        subgraph = G.subgraph(nodes_to_draw)
    else:
        nodes_to_draw = list(G.nodes)
        subgraph = G

    # Edge trace
    edge_x, edge_y = [], []
    for edge in subgraph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#aaa'),
        hoverinfo='none',
        mode='lines'
    )

    # Node trace
    node_x, node_y, node_text, node_colors = [], [], [], []
    for node in nodes_to_draw:
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"Node {node} | Community {partition[node]}")
        node_colors.append(color_map[partition[node]])

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=node_colors,
            size=6,
            line=dict(width=0.5)
        ),
        text=node_text
    )

    fig = go.Figure(data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(text='Facebook Community Graph', font=dict(size=20)),
            title_x=0.5,
            showlegend=False,
            margin=dict(l=20, r=20, t=40, b=20),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False)
        )
    )
    return fig

app.layout = dbc.Container([
    html.H2("Facebook Community Visualization", className="text-center my-4"),

    dbc.Row([
        dbc.Col([
            html.H5("Communities", className="mb-3"),
            dcc.Dropdown(
                id='community-filter',
                options=[{'label': f'Community {c}', 'value': c} for c in unique_communities],
                placeholder="Select a community",
                clearable=True
            )
        ], width=3),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Community Graph"),
                dbc.CardBody([
                    dcc.Graph(id='graph', figure=create_figure())
                ])
            ])
        ], width=9)
    ])
], fluid=True)

# Callback for dropdown filter
@app.callback(
    Output('graph', 'figure'),
    Input('community-filter', 'value')
)
def update_graph(selected_community):
    return create_figure(selected_community)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
