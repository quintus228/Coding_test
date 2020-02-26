import requests
name = "Chenkun"
url = "https://www.yjezimoc.com/test/helloworld?name=%s" % name
data = requests.post(url=url).json()
with open("coding_test.html", "w") as f:
    f.write("<h1>%s</h1>\n" % data['title'])
    f.write("<p>%s</p>\n" % data['content'])
