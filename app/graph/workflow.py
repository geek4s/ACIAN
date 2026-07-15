from langgraph.graph import StateGraph
from langgraph.graph import END

from app.state.state import CompetitorState

from app.agents.retrieval_agent import retrieval_agent
from app.agents.comparison_agent import comparison_agent


workflow = StateGraph(CompetitorState)

workflow.add_node(
    "retrieve",
    retrieval_agent
)

workflow.add_node(
    "compare",
    comparison_agent
)

workflow.set_entry_point("retrieve")

workflow.add_edge(
    "retrieve",
    "compare"
)

workflow.add_edge(
    "compare",
    END
)

graph = workflow.compile()