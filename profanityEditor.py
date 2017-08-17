#Import urllib for web content extraction
import urllib

#readFile() method to read the .txt documents and pass that as an argument to the profanityChecker() method
#After passing the contents, close the url connection
def readFile():
	quotes = open("/Users/nithysub/Desktop/FSWD/email_profanity.txt")
	contentsRead = quotes.read()
	#print(contentsRead)
	quotes.close()
	profanityChecker(contentsRead)
	
#profanityChecker() method takes in a .txt file as input. It uses urllib.urlopen() function to extract the contents from the web
#Since the query to pass is the text document itself, it then uses WDYL.com application to help detect curse words or not.
#When curse words are detected, it alerts with a message 'Profanity Alert' else it prints a message saying 'The document is free of curse words'
def profanityChecker(text_ToCheck):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_ToCheck)
	#print(connection.read())
	if(connection.read()=="true"):
		print("Profanity Alert!!!")
	else:
		print("The document is free of curse words")
	connection.close()


readFile()