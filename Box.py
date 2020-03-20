# import traceback
# try:
#     raise Exception("This is an error message")
# except:
#     errorfile = open("error_log.txt","a")
#     errorfile.write(traceback.format_exc())
#     errorfile.close()
#     print("all error are in the errorlog text file")
def Box(symbol,height,width):
    if len(symbol) !=1:
        raise Exception("'symbol' has to be a string of length 1")
    if height <2 or width<1:
        raise Exception("'Width' must be at least 1 and 'Height' must be at least 2")
    print(symbol*width)
    for i in range(height-2):
        print(symbol + " "*(width-2) + symbol)
    print(symbol*width)
Box("+",1,0)