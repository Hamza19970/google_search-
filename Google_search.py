from googlesearch import search
from colorama import Fore, Back, Style

def core():
	aamzA=str(input("enter your key to all search :"))
	num=int(input("enter any numbers to search :" ))
	hamza=str(input("choose language fr ,en :"))
	h=search(aamzA, num_results=num,    lang=hamza)
	for i in h:
	   print(Fore.RED+i)
	   
core()	   
	   
	   
   
	
	

