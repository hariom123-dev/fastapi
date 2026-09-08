import sys

sys.path.insert(0, r"E:\post hog\fastapi")
from starlette.datastructures import Headers, QueryParams

q = QueryParams([("a", "1"), ("", "2"), ("a", "3")])
q_filtered = type(q)([(k, v) for k, v in q.multi_items() if k != ""])
print(type(q_filtered))
print(q_filtered.getlist("a"))
print(q_filtered.multi_items())

h = Headers([("b", "1"), ("", "2"), ("b", "3")])
h_filtered = type(h)([(k, v) for k, v in h.multi_items() if k != ""])
print(type(h_filtered))
print(h_filtered.getlist("b"))
print(h_filtered.multi_items())
