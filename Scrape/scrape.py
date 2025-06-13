from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse

scrapfly = ScrapflyClient(key="{{ YOUR_API_KEY }}")

api_response: ScrapeApiResponse = scrapfly.scrape(
    scrape_config=ScrapeConfig(url="https://tds.s-anand.net/#/2025-01/")
)

# Automatic retry errors marked "retryable" and wait delay recommended before retrying
api_response: ScrapeApiResponse = scrapfly.resilient_scrape(
    scrape_config=ScrapeConfig(url="https://tds.s-anand.net/#/2025-01/")
)

# Automatic retry error based on status code
api_response: ScrapeApiResponse = scrapfly.resilient_scrape(
    scrape_config=ScrapeConfig(url="https://httpbin.dev/status/500"),
    retry_on_status_code=[500],
)

# scrape result, content, iframes, response headers, response cookies states, screenshots, ssl, dns etc
print(api_response.scrape_result)

# html content
print(api_response.scrape_result["content"])

# Context of scrape, session, webhook, asp, cache, debug
print(api_response.context)

# raw api result
print(api_response.content)

# True if the scrape respond with >= 200 < 300 http status
print(api_response.success)

# Api status code /!\ Not the api status code of the scrape!
print(api_response.status_code)

# Upstream website status code
print(api_response.upstream_status_code)

# Convert API Scrape Result into well known requests.Response object
print(api_response.upstream_result_into_response())
