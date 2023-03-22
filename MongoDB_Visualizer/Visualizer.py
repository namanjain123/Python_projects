import json
import subprocess
import os
from graphviz import Digraph
# get the dependency from enviorment
def getdependency(dependecy):
    # Load the environment variables from the .env file
    load_dotenv()
    # Get the URI from an environment variable
    uri = os.environ.get(dependecy)
    return uri
# Add Nodes
def add_nodes(node, json_obj, parent=None):
    for key, value in json_obj.items():
        if isinstance(value, dict):
            child = node.node(key, shape='box', style='filled', fillcolor='#b8dbf2', label=f"{key}")
            if parent:
                node.edge(parent, key, dir='both')
            add_nodes(node, value, parent=key)
        else:
            value_str = str(value)
            node.node(f"{key}: {value_str}", shape='ellipse', style='filled', fillcolor='#c1f5c3')
            if parent:
                node.edge(parent, f"{key}: {value_str}", dir='both')
# clear dependecy
def remove_dependency(package_name):
    # Install the package without dependencies
    subprocess.check_call(['pip', 'install', '--no-deps',package_name])
# Crate Flowchart
def create_flowchart(json_obj):
    # Convert the JSON object to a Python dictionary
    obj_dict = json.loads(json_obj)
    # Create a new Digraph object
    dot = Digraph(comment='JSON Flowchart', node_attr={'style': 'rounded'})

    # Add the nodes and edges recursively
    add_nodes(dot, obj_dict)

    # Render the flowchart to a file
    dot.format = 'png'
    dot.render('json_flowchart', view=True)
# Call MongoDb file from database
def call_mongodb_Json(collectionName):
    # installing the dependency
    remove_dependency('pymongo')
    remove_dependency('dotenv')
    #load the dependency
    import pymongo
    from dotenv import load_dotenv
    mongodburi=getdependency('mogouri')
    client = pymongo.MongoClient(str(mongodburi))
    databasename=getdependency('databaseName')
    db = client[str(databasename)]
    
    collection = db[str(collectionName)]
    # query the collection and get the result as a list of dictionaries
    result = list(collection.find())
    # convert the result into a JSON format
    json_data = json.dumps(result)
    # Call the function to create and save the flowchart
    return json_data
try:
  json_obj=call_mongodb_Json("naman")
  create_flowchart(json_obj)
except Exception as e:
  print(str(e))
