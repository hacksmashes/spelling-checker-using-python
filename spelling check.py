from textblob import TextBlob

a="hleeo"
print("Original Text : "+str(a))
b=TextBlob(a)
print("Corrected text : "+str(b.correct()))
