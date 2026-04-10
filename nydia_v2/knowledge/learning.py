"""Learning engine internalizes new patterns into graph memory."""

from .knowledge_graph import KnowledgeGraph


class LearningEngine:
    def __init__(self, graph: KnowledgeGraph) -> None:
        self.graph = graph

    def internalize(self, topic: str, goal: str) -> None:
        if topic and goal:
            self.graph.connect(topic, goal)
