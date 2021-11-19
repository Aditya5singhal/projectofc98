def swapfile():
    file1=input("which file u want to read")
    file2=input("which file  u want to write")

    f=open(file1,'r')
    f1=f.read()
    f2=open(file2,'w')
    f2.write(f1)


swapfile()



