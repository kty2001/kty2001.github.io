MATCH (node)
UNWIND labels(node) AS label
RETURN
    label,
    count(node) AS count
ORDER BY label;

MATCH ()-[relationship]->()
RETURN
    type(relationship) AS relationship_type,
    count(relationship) AS count
ORDER BY relationship_type;

MATCH path = ()-[]->()
RETURN path;