from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from pipedream_blogger.tools.blog_post_tool import BlogPostTool
from pipedream_blogger.tools.format_tool import FormatTool

from crewai_tools import (
    WebsiteSearchTool, # Pipedream Website Search Tool
    CodeDocsSearchTool, # Docs Search Tool
    # SerperDevTool, # General Search Tool
		EXASearchTool,
	  # DallETool,
   	# tool,
)

# google_search = SerperDevTool()
exa_client = EXASearchTool()
blog_post_tool = BlogPostTool()
# yc_search = WebsiteSearchTool(website='https://news.ycombinator.com')
# blog_search = WebsiteSearchTool(website='https://pipedream.com/blog')
# website_search = WebsiteSearchTool(website='https://pipedream.com')
# docs_search = CodeDocsSearchTool(docs_url='https://pipedream.com/docs')

# blog_urls = [
# 	'https://pipedream.com/blog/2fa/',
# 	'https://pipedream.com/blog/add-preview-screenshots-to-gitlab-merge-requests-with-browserless/',
# 	'https://pipedream.com/blog/adding-a-contact-form-to-next-js-on-vercel/',
# 	'https://pipedream.com/blog/adding-background-jobs-to-next-js-with-qstash/',
# 	'https://pipedream.com/blog/ai-driven-smoke-tests/',
# 	'https://pipedream.com/blog/airtable-as-an-approval-queue-with-pipedream/',
# 	'https://pipedream.com/blog/archiving-slack-threads-to-discourse-with-gpt-3/',
# 	'https://pipedream.com/blog/automate-a-weekly-new-twitter-followers-shoutout-with-pipedream/',
# 	'https://pipedream.com/blog/automate-customer-support-with-dialogflow/',
# 	'https://pipedream.com/blog/avoiding-parking-tickets-with-pipedream/',
# 	'https://pipedream.com/blog/bring-your-own-oauth-clients/',
# 	'https://pipedream.com/blog/build-a-slack-slash-command-in-less-than-10-minutes/',
# 	'https://pipedream.com/blog/build-a-youtube-channel-connected-slack-bot/',
# 	'https://pipedream.com/blog/build-workflows-faster-with-ai/',
# 	'https://pipedream.com/blog/build-your-own-chat-bot-with-openai-and-pipedream/',
# 	'https://pipedream.com/blog/building-a-custom-pipedream-action-component-with-gitpod/',
# 	'https://pipedream.com/blog/classifying-bug-reports-with-chatgpt/',
# 	'https://pipedream.com/blog/command-your-telegram-bot-with-pipedream/',
# 	'https://pipedream.com/blog/commit-your-dev-to-articles-to-github/',
# 	'https://pipedream.com/blog/concurrency-controls-design/',
# 	'https://pipedream.com/blog/connect-a-webflow-form-to-an-airtable/',
# 	'https://pipedream.com/blog/connecting-your-user-accounts-to-pipedream/',
# 	'https://pipedream.com/blog/creating-an-out-of-office-reminder-system/',
# 	'https://pipedream.com/blog/creating-workflows-programmatically/',
# 	'https://pipedream.com/blog/devreleng/',
# 	'https://pipedream.com/blog/eliminate-cold-starts-with-warm-workers/',
# 	'https://pipedream.com/blog/export-axios-response-data-from-a-loop/',
# 	'https://pipedream.com/blog/export-insomnia-to-bruno/',
# 	'https://pipedream.com/blog/file-stores-live-demo-recap-and-workflows/',
# 	'https://pipedream.com/blog/filestores/',
# 	'https://pipedream.com/blog/github-sync/',
# 	'https://pipedream.com/blog/graphql-requests-with-node-js/',
# 	'https://pipedream.com/blog/hippa/',
# 	'https://pipedream.com/blog/how-to-build-a-bot-to-download-the-latest-r-gifs-posts-on-reddit/',
# 	'https://pipedream.com/blog/how-to-connect-to-and-insert-data-into-supabase-with-pipedream/',
# 	'https://pipedream.com/blog/how-to-retrieve-data-from-apis-using-pagination/',
# 	'https://pipedream.com/blog/how-to-sending-messages-to-a-channel-with-a-discord-bot/',
# 	'https://pipedream.com/blog/http-api-for-latest-wuhan-coronavirus-data-2019-ncov/',
# 	'https://pipedream.com/blog/introducing-one-second-cron-jobs/',
# 	'https://pipedream.com/blog/introducing-the-pipedream-source-available-license/',
# 	'https://pipedream.com/blog/log-workflow-errors-to-aws-cloudwatch/',
# 	'https://pipedream.com/blog/managing-access-to-your-projects-and-secrets/',
# 	'https://pipedream.com/blog/meet-the-new-event-history/',
# 	'https://pipedream.com/blog/node18/',
# 	'https://pipedream.com/blog/openai-integrations-live-demo-recap-workflows/',
# 	'https://pipedream.com/blog/page/2#/portal',
# 	'https://pipedream.com/blog/parse-multi-part-form-data-using/',
# 	'https://pipedream.com/blog/performing-shopify-bulk-operations-in-one-workflow-with-flow-rerun/',
# 	'https://pipedream.com/blog/pipedream-customer-facing-integration-prototypes/',
# 	'https://pipedream.com/blog/pipedream-plus-snowflake-for-data-observability/',
# 	'https://pipedream.com/blog/pipedream-potent-serverless-capabilities/',
# 	'https://pipedream.com/blog/pipedream-unaffected-by-log4shell/',
# 	'https://pipedream.com/blog/pipedreams-affiliate-program/',
# 	'https://pipedream.com/blog/post-mortem-on-our-2-13-aws-incident/',
# 	'https://pipedream.com/blog/private-connected-accounts/',
# 	'https://pipedream.com/blog/publish-notion-pages-as-blog-posts/',
# 	'https://pipedream.com/blog/puppeteer-and-playwright/',
# 	'https://pipedream.com/blog/real-time-data-check-notifications-with-mongodb/',
# 	'https://pipedream.com/blog/real-time-notifications-on-x-keywords/',
# 	'https://pipedream.com/blog/reducing-churn-with-stripe-and-chatgpt/',
# 	'https://pipedream.com/blog/reindex-algolia-on-github-releases/',
# 	'https://pipedream.com/blog/requestbin-events-api/',
# 	'https://pipedream.com/blog/return-a-plain-text-response-from-a-workflow/',
# 	'https://pipedream.com/blog/run-and-monitor-production-systems-on-pipedream/',
# 	'https://pipedream.com/blog/scale-your-automotive-business-with-parseur-and-pipedream/',
# 	'https://pipedream.com/blog/scraping-discourse-with-a-custom-pipedream-source/',
# 	'https://pipedream.com/blog/scraping-market-data-with-python/',
# 	'https://pipedream.com/blog/scraping-url-metadata-with-an-npm-package-in-a-node-js-code-step/',
# 	'https://pipedream.com/blog/send-a-tweet-whenever-a-new-blog-post-is-published-on-ghost/',
# 	'https://pipedream.com/blog/send-delayed-welcome-emails-to-new-users-with-postmark/',
# 	'https://pipedream.com/blog/send-promotion-emails-with-shopify-orders-at-random/',
# 	'https://pipedream.com/blog/series-a-financing/',
# 	'https://pipedream.com/blog/set-up-shopify-gdpr-webhooks-without-code/',
# 	'https://pipedream.com/blog/sharp-js-compatibility/',
# 	'https://pipedream.com/blog/shopify-app-install-notifications-to-slack-without-code/',
# 	'https://pipedream.com/blog/shopify-partner-transactions-counter/',
# 	'https://pipedream.com/blog/shutting-down-the-sql-service/',
# 	'https://pipedream.com/blog/support-for-openai-vision-assistants-and-more/',
# 	'https://pipedream.com/blog/the-simplest-way-to-run-node-code-on-a-schedule/',
# 	'https://pipedream.com/blog/trigger-a-pipedream-workflow-from-an-airtable-base-button/',
# 	'https://pipedream.com/blog/unlocking-poetic-possibilities-using-gpt-3-to-create-a-bot-that-transforms-tweets-into-poetry-no-coding-experience-necessary/',
# 	'https://pipedream.com/blog/use-any-api-in-seconds-with-auth-managed-by-pipedream/',
# 	'https://pipedream.com/blog/using-airtable-as-a-database-with-next-js/',
# 	'https://pipedream.com/blog/using-the-new-openai-actions-in-pipedream/',
# 	'https://pipedream.com/blog/verify-woocommerce-orders-with-sms-codes-with-fraudlabs-pro/',
# 	'https://pipedream.com/blog/what-is-json/',
# 	'https://pipedream.com/blog/workflows-are-now-shareable/',
# 	'https://pipedream.com/blog/workspaces-inviting-team-members/',
# 	'https://pipedream.com/blog/write-nodejs-using-lodash-on-pipedream/',
# ]

# website_urls = [
# 	"https://pipedream.com/support",
# 	"https://pipedream.com/terms",
# 	"https://pipedream.com/privacy",
# 	"https://pipedream.com/sla",
# 	"https://pipedream.com/dpa",
# ]


# create an array of website search tools for each of the website_urls

# pipedream_searchers = []

# for url in [*blog_urls, *website_urls]:
#     pipedream_searchers.append(WebsiteSearchTool(website=url))
#     time.sleep(0.1)  # Sleep for 1 second between initializing each searcher


@CrewBase
class PipedreamBloggerCrew():
	"""PipedreamBlogger crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[exa_client],
			verbose=True
		)

	@agent
	def pipedream_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['pipedream_expert'],
			tools=[exa_client],
			verbose=True
		)

	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_writer'],
			tools=[exa_client],
			verbose=True
		)

	@agent
	def http_sender(self) -> Agent:
		return Agent(
			config=self.agents_config['http_sender'],
			tools=[blog_post_tool],
			verbose=True,
			memory=False,
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
	def writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['writing_task'],
			tools=[FormatTool(result_as_answer=True)],
			# output_file='output/report.md'
		)

	@task
	def http_task(self) -> Task:
		return Task(
			config=self.tasks_config['http_task'],
			input_mapping=lambda inputs: {
				'title': inputs['title'],
				'content': inputs['content'],
			}
	)

	""" 1 CREW """
	@crew
	def crew(self) -> Crew:
		"""Creates the PipedreamBlogger crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			memory=False,
			verbose=True,
   		planning=True,
			max_rpm="600"
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
