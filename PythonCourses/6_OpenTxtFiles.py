
dltLogs = open("VSSlogs.txt", "w")
L = "statusChanged().activated"
s = "==="

dltLogs.write(s)
dltLogs.writelines(L)


dltLogs = open("VSSlogs.txt","r")
print(dltLogs.read())
dltLogs.close()