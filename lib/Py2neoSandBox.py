from py2neo import Node, Relationship
 from py2neo import Node, Relationship
 from py2neo import Graph
 graph = Graph(password = '12345')
 from py2neo import cypher


 d ={"element_type":"Person", "id":1}
 d ={"element_type":"Individual", "id":1}
 d
{'element_type': 'Individual', 'id': 1}
 a = Node('Individual', d['element_type'], d['id'])
 a
(f3be18a:`1`:Individual)
 a = Node('Individual', element_type=d['element_type'], id= d['id'])
 a
(aa5c675:Individual {element_type:"Individual",id:1})
graph.create(a)
n=graph.data("MATCH (n) WHERE n.id=1 RETURN n")
n
[{u'n': (aa5c675:Individual {element_type:"Individual",id:1})}]
 f = {"element_type":"Person", "id":1}
 b = Node('Person', f['element_type'], f['id'])
 graph.create(b)
 f = {"element_type":"Person", "name":"Christian"}
 b = Node('Person', f['element_type'], f['name'])
 graph.create(b)
 n=graph.data("MATCH (n) WHERE n.name='Christian' RETURN n")
 n2=graph.data("MATCH (n) WHERE n.id='1' RETURN n")
 relation_person_individual = Relationship(n, "LIKES", n2)
 graph.create(relation_person_individual)
 type(n)
<type 'list'>
 n[0]
 n=graph.data("MATCH (n) WHERE n.id=1 RETURN n")
 n
[{u'n': (aa5c675:Individual {element_type:"Individual",id:1})}]
 b = Node('Person', element_type= f['element_type'], name=f['name'])
 b
(christian:Person {element_type:"Person",name:"Christian"})

 graph.create(b)
 n=graph.data("MATCH (n) WHERE n.name='Christian' RETURN n")
 n
[{u'n': (christian:Person {element_type:"Person",name:"Christian"})}]
 n2=graph.data("MATCH (n) WHERE n.id='1' RETURN n")
 n
[{u'n': (christian:Person {element_type:"Person",name:"Christian"})}]
 n2 = graph.data("MATCH (n) WHERE n.id=1 RETURN n")
 n2
[{u'n': (aa5c675:Individual {element_type:"Individual",id:1})}]
 n[0]
{u'n': (christian:Person {element_type:"Person",name:"Christian"})}
 type(n[0]
... )
<type 'dict'>
 n
[{u'n': (christian:Person {element_type:"Person",name:"Christian"})}]
 nodo1 = Node (n[0]['n'])
 nodo1
(c4dff5f:`(christian:Person {element_type:"Person",name:"Christian"})`)
 n2
[{u'n': (aa5c675:Individual {element_type:"Individual",id:1})}]
 nodo2 = Node(n2[0]['n'])
relation_person_individual = Relationship(nodo1, "LIKES", nodo2)
graph.create(relation_person_individual)
