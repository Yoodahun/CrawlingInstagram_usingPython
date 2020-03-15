from lib.Crawler import crawl

url = "https://www.instagram.com/explore/tags/xpro3/"

pageString = crawl(url)
print(pageString)