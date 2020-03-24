import os,PyPDF4
os.chdir("/home/ylli/Downloads")
pdf = open("Python - The Ultimate Beginner's guide - Andrew Johansen.pdf","rb")
reader = PyPDF4.PdfFileReader(pdf)
# for i in range(reader.numPages):
#     print(reader.getPage(i).extractText())
print(reader.numPages)
print(reader.getPage(20).extractText())