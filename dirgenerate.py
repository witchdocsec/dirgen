import requests
from duckduckgo_search import DDGS
import tldextract

with open("banner.txt","r") as banner:
	print(banner.read())

site = input("Enter site name: ")
keywords = "site:{} +filetype:TXT +inurl:\"robots.txt\"".format(site)
results = DDGS().text(keywords)
dirs=[]
for result in results:
	url=result["href"]
	try:
		r=requests.get(url)
		splitl=r.text.split("\n")
		for line in splitl:
			if "Disallow: " in line:
				lnsplt=line.replace("Disallow: ","").split("/")
				for entry in lnsplt:
					q=entry.split("?")
					entry=q[0].replace("*","")
					if entry.lower() not in dirs and not entry == (" ") and not tldextract.extract(url).domain.split(".")[0] in entry.lower() and len(entry) < 25:
						dirs.append(entry.lower())
						with open("dirlist.txt","a") as mylist:
							mylist.write(entry+"\n")
						print("added entry: "+entry)
						
	except:
		pass
print("done")
