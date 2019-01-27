#! python3

# Poor implementation of security exposing all the study material available for download without registering / logging in to askiitians.com .

import requests, bs4


print("""
/***
 *                     _     _____  _____  _______  _                     
 *         /\         | |   |_   _||_   _||__   __|(_)                    
 *        /  \    ___ | | __  | |    | |     | |    _   __ _  _ __   ___  
 *       / /\ \  / __|| |/ /  | |    | |     | |   | | / _` || '_ \ / __| 
 *      / ____ \ \__ \|   <  _| |_  _| |_    | |   | || (_| || | | |\__ \ 
 *     /_/    \_\|___/|_|\_\|_____||_____|   |_|   |_| \__,_||_| |_||___/ 
 *                                                                        
 *                              ╦ ╦┌─┐┌─┐┬┌─┌─┐┌┬┐
 *                              ╠═╣├─┤│  ├┴┐├┤  ││
 *                              ╩ ╩┴ ┴└─┘┴ ┴└─┘─┴┘
 * 001100000111100000110100001110000111000001101001011100100110000101101010                                                                         
 */
""")


RAW_URLS = []

res = requests.get('http://www.askiitians.com/past-year-papers/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
table = soup.find('table')
links = table.findAll('a')

for link in links:
  RAW_URLS.append(link.get("href"))

for i in RAW_URLS:
	if not "https://www.askiitians.com" in i:
		i = "https://www.askiitians.com" + i
	s = bs4.BeautifulSoup(requests.get(i).text, "html.parser")
	for u in s.find_all("a"):
		if not isinstance(u.get("data-href"), type(None)):
			print(u.get("data-href"))
