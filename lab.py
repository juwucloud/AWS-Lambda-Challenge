

#open a file
#read it

#use something to count the words.

#trigger when uploading to s3
#txt file upload to s3 and get an email with "file xyz has xy words"


def wordcount(textfile):
    # set wordcount to 0 from start
    c = 0
    # Opening file in read only mode
    with open(textfile, 'r') as file:
        data = file.read()
        w = data.split()
        c += len(w)
    print(c)

# Testfile is in same folder
text = 'testtext.txt'

wordcount(text)
