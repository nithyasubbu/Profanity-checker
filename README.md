# Profanity-checker
Profanity checker for given set of documents


Basically the idea is to scale this application to serve as a curseword filter & identify if there is a 'Profanity alert'
for any composed mails prior to sending. Many a times, it so happens that we use curse words accidentally or unknowingly and get caught up in embarrassing situations. To prevent any such issues, it's better to build a small application to detect if it has curse words or not.

For the scope of this small task, we have taken two documents. But it's an ongoing project where the scalability to filter composed mails for profanity is the primary focus. Will upload the source code soon. 

There are two docs: movie_quotes.txt & email_profanity.txt are present (with & without curse words). Using Google's WDYL.com (What Do You Love) application, the curse word detection is done. If the response to any WDYL query is false, it is not a curse word and if otherwise, it is. This is made useful in this application.

profanityEditor.py is the python file that needs to be run for execution.

User Instructions:
Please download the entire folder containing the two text files and profanityEditor.py file and note the location where you save the files & folder in your local computer. Using terminal (OS), cd into the location where the files are present and run >> python profanityEditor.py

For Windows, type in the path of the files, "C:/.../../python" , ls and cd into the folder and then run >> C:/.../../python profanityEditor.py and execute it. You can check for any kind of text docs with and without curse words.
