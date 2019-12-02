
def getVarName(var):
     varName = [ k for k,v in locals().iteritems() if v == var][0] # https://www.tutorialspoint.com/How-to-get-a-variable-name-as-a-string-in-Python
     return varName