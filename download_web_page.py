import urllib.request as urllib2

url = "https://facebookd.com"

raspuns_server = urllib2.urlopen(url)

date = raspuns_server.read()

print(date)

try:
    fisier_html = open("site_download.html", "w")
    fisier_html.write(date)
except Exception:
    print("Procesul nu s-a incheiat cu succes")
else:
    fisier_html.close()

print("Job done...")



















