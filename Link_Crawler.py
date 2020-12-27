from bs4 import BeautifulSoup
import urllib.request as url
import sys

pagina = input("\n\nDigite a Url do alvo: ")
try:
	site = url.urlopen(pagina)

except:
	print("\n\nA url passada não existe ou está fora do ar\n\n")
	sys.exit(0)

else:
	print("\n\n")
	cont = 0
	site = site.read()
	site = BeautifulSoup(site, "html.parser")
	links = site.find_all("a")

	for l in links:
		cont += 1
		print(f'\n {l.get("href")}')
	print("-----------------------------------------------------------------------")
	print(f"\n\n\t\tA busca retornou {cont} links\n\n")
