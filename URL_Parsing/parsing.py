# ! URL PARSING

url = "https://www.kaggle.com/datasets"

# ? Protocol
protocol = url[: url.find(":")]

# ? Domain
dot1 = url.find(".")
dot2 = url.find(".", dot1 + 1)
domain = url[dot1 + 1 : dot2]

# ? Page
page = url[url.find("/", dot2) :]

print("Protocol :", protocol)
print("Domain   :", domain)
print("Page     :", page)
