"""Lightweight in-memory knowledge graph."""

from collections import defaultdict
from typing import Dict, List


class KnowledgeGraph:
    def __init__(self) -> None:
        self.edges: Dict[str, List[str]] = defaultdict(list)

    def connect(self, src: str, dst: str) -> None:
        if dst not in self.edges[src]:
            self.edges[src].append(dst)

    def neighbors(self, node: str) -> List[str]:
        return list(self.edges.get(node, []))
