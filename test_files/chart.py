from typing import List
import os
from svg.charts import bar


class Bar:

    def __init__(self, fields: List, values: List[List[float]], titles: List[str], graph_title: str):
        self.graph = bar.VerticalBar(fields)
        self.graph.stack = 'side'
        self.graph.scale_integers = True
        self.graph.width = 1024
        self.graph.height = 768
        self.graph.graph_title = graph_title
        self.graph.show_graph_title = True
        self.graph.bar_gap = True

        for i in range(len(titles)):
            self.graph.add_data({'data': values[i], 'title': titles[i]})

    def save(self, filename):
        _dir = os.path.join(os.path.dirname(__file__), "svg")
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        res = self.graph.burn()
        with open(f'{os.path.join(_dir, os.getenv("PYTEST_CURRENT_TEST", ""), filename)}.py.svg', 'w') as f:
            f.write(res)
