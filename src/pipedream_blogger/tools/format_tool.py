from crewai_tools import BaseTool

class FormatTool(BaseTool):
    name: str = "Format Tool"
    description: str = "Format the content as JSON with a title and content property"

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return {title: "Title", content: argument}
