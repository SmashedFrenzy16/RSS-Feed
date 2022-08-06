import feedparser

feed = feedparser.parse("https://netfruittechnologies.blogspot.com/")

print('Number of RSS feed posts: ', len(feed.entries))

entryask = int(input("Enter in an index number to see a feed: "))

entry = feed.entries[entryask]

print('Post Title: ', entry.title)

print("")

print(entry.published)

print("-----------------")

print(entry.summary)

print("-------News Link---------")

print(entry.link)
