from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from pipedream_blogger.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# Importing crewAI tools
from crewai_tools import (
    WebsiteSearchTool, # Pipedream Website Search Tool
    CodeDocsSearchTool, # Docs Search Tool
    SerperDevTool, # General Search Tool
    GithubSearchTool, # Github Search Tool
)

# pipedream_repo_search = GithubSearchTool(
#     github_repo='https://github.com/pipedreamhq/pipedream',
#     content_types=['code', 'issue'], # Options: code, repo, pr, issue
#     gh_token="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",
# )

website_urls = [
    "https://pipedream.com/support",
    "https://pipedream.com/terms",
    "https://pipedream.com/privacy",
    "https://pipedream.com/sla",
    "https://pipedream.com/dpa",
    "https://pipedream.com/affiliates",
		"https://pipedream.com/blog/page/1",
		"https://pipedream.com/blog/page/2",
		"https://pipedream.com/blog/page/3",
		"https://pipedream.com/blog/page/4",
]

google_search = SerperDevTool()

yc_search = WebsiteSearchTool(website='https://news.ycombinator.com')
pipedream_search = WebsiteSearchTool(website='https://pipedream.com')
# create an array of website search tools for each of the website_urls
pipedream_searchers = [WebsiteSearchTool(website=url) for url in website_urls]

docs_search = CodeDocsSearchTool(docs_url='https://pipedream.com/docs')
blog_search = CodeDocsSearchTool(docs_url='https://pipedream.com/blog')

@CrewBase
class PipedreamBloggerCrew():
	"""PipedreamBlogger crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			tools=[google_search, yc_search],
			verbose=True
		)

	@agent
	def pipedream_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['pipedream_expert'],
			tools=[pipedream_search, docs_search, blog_search, *pipedream_searchers],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			tools=[google_search, pipedream_search, docs_search, blog_search, *pipedream_searchers],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def pipedream_idea_task(self) -> Task:
		return Task(
			config=self.tasks_config['pipedream_idea_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PipedreamBlogger crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
