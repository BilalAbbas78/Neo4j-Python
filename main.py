# python -m pip install neo4j
from neo4j import GraphDatabase
uri = "bolt://URL"
driver = GraphDatabase.driver(uri, auth=("neo4j", "PASSWORD"), encrypted=True)

s1 = "MATCH (n) RETURN count(*)"
# s1 = "CREATE (d: Dept) RETURN d"

result = driver.session().run(s1)
print(result.single()[0])

# Close the driver
driver.close()