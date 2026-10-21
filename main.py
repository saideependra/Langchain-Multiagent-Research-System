from src.tools.tools import web_search, scrape_url

result = scrape_url.invoke({
    "url": "https://www.reddit.com/r/AISEOInsider/comments/1rs1o1v/latest_ai_news_the_biggest_ai_announcements_right"
})

print(result)


