from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print (" "),
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Site ismi gir \n(Örnek : siteadı.com Veya www.siteadı.com ): ")
	print ("\n\n Site : \n")
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print ("Tamam => "),req_link

def Credit():
	Space(9); print ("#####################################")
	Space(9); print ("#   +++ Emre Admin Panel Bulucu +++   #")
	Space(9); print ("#     Script by Emre Coder    #")
	Space(9); print ("#     LiceXTeam   #")
	Space(9); print ("#####################################")

Credit()
findAdmin()