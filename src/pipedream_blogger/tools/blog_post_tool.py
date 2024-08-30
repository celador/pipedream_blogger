from crewai_tools import BaseTool
import requests

# Define the custom tool for sending HTTP requests
class BlogPostTool(BaseTool):
    name: str = "Blog Post Sender"
    description: str = (
        "This tool sends a blog post to the Pipedream (Ghost) Blog."
    )

    def _run(self, title: str, markdown: str) -> str:
        data = {
        'title': title,
        'markdown': markdown
        }
        response = requests.post("https://eo5www52nchzf9l.m.pipedream.net", json=data)
        if response.status_code == 200:
            return "Data successfully sent."
        else:
            return f"Failed to send data. Status code: {response.status_code}"

