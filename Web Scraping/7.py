from bs4 import BeautifulSoup
import glob	# to read all files from a directory

def get_all_names(string):
	lst_ = []
	soup = BeautifulSoup(string, "lxml")
	table = soup.find("table", summary="Popularity for top 1000")
	#print len(table) 			
	table_rows = table.find_all('tr')
	for tr in table_rows[:-1]:
		td = tr.find_all('td')
		for i in td:
			lst_.append(i.text)
		
	return lst_[:3000]
		
def main():
	lst = glob.glob("/home/malika/sysP/Homework/babynames/*.html")
	lst.sort()
	#print lst
	for f in lst:
		c = 0
		fhand = open(f,"r")
		lst1 = get_all_names(fhand.read())
		while c < len(lst1):
			lst1.pop(c)
			c = c + 2
		print "\nfor",f,"names of len > 3 are\n"
		l = []
		for name in lst1[:2000]:
			if len(name) > 3:
				l.append(name)
		print l				
		
if __name__ == "__main__":
	main()


