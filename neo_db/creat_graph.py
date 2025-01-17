from py2neo import Graph, Node, Relationship
from config import graph

graph.delete_all()
with open("./raw_data/computer_composition.csv", encoding='utf-8') as f:
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)
        graph.run("merge (p:Concept {cate:'%s', name: '%s'})" % (rela_array[3], rela_array[0]))
        graph.run("merge (p:Concept {cate:'%s',name: '%s'})" % (rela_array[4], rela_array[1]))
        graph.run(
            "MATCH(e: Concept), (cc: Concept) WHERE e.name='%s' AND cc.name='%s' CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (rela_array[0], rela_array[1], rela_array[2], rela_array[2])
        )
