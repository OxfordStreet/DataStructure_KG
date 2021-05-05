from py2neo import Graph

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="@"
)  # DataStructureKG
CA_LIST = {"科目": 0, "章节": 1, "单元": 2, "主题": 3, "概念": 4, "其他": 5}
