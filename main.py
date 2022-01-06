from cryptos import *

def keydress1():
    PrivateKey = random_key()
    PublicKey = privtopub(PrivateKey)
    Address = pubtoaddr(PublicKey)
    open("keydresses.txt",'a')
    open("addresses.txt",'a')
    file1 = open("keydresses.txt",'a')
    file2 = open("addresses.txt",'a')
    file1.write("\n" +Address+" ")
    file1.write("\n" +PrivateKey+" ")
    file1.close()
    file2.write("\n" +Address+" ")
    file2.close()
    

        
[keydress1() for _ in range(640000000000000000)]
