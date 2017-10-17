__author__ = 'chris'

from time, datetime

from py2neo import Graph
from py2neo import Node, Relationship

graph = Graph(password="12345")


class MasterNode(object):
    def __init__(self):
        self.created =str(datetime.datetime.now())

    def create_node(self, **kwargs):
        d={"created":self.created}
        for item in kwargs.items():
            d.update({item[0]:item[1]})

        print "######## Dictionary for node creations ########"
        print d

        if d["element_type"] == "person":
            person = graph.create(Node("Person",
                                       [element_type = d["element_type"],
                                        name = d["name"],
                                        email = d["email"],
                                        created = d["created"]]))
            msg = "Node Created!"
            print msg

        elif d["element_type"] == "individual":
            individual = graph.create(Node("Individual", [element_type= d["element_type"],
                                                          _id = d["id"],
                                                          chromosome = str(d["chromosome"]),
                                                          views = d["views"],
                                                          fitness = d["currentFitness"],
                                                          created = d["created"]]))
            msg = "Node Created!"

        elif d["element_type"] == "collection":
            collection = graph.create(Node("Collection", [element_type = d["element_type"],
                                                          name = d["name"],
                                                          description = d["description"],
                                                          visibility = d["visibility"]])
            msg = "Node Created!"
            print msg

    def get_node(self, name = None):
        self.node = name
        query = "MATCH (n) WHERE n.name = '" + self.node + "' RETURN n"


        return query






