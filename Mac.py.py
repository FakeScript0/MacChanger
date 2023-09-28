import subprocess
import time
print("Mac Degistirici Proqraminiz Ise Basladi!")
time.sleep(1)
print("Mac Adresinizi Degistirmek istiyorsaniz (y) eks halda (n) Yazin!")

while True:
    n=input()
    if n=="y" or n=="Yes" or n=="yes":
        time.sleep(0.8)
        print("Mac Adresiniz Degistiriliyor!")
        time.sleep(2)

        subprocess.call(["ifconfig","eth0","down"])
        subprocess.call(["ifconfig","eth0","hw","ether","00:22:33:44:55:66"])
        subprocess.call(["ifconfig","eth0","up"])
        print("Mac Adresiniz Degistirildi")
        break
    elif n=="n" or n=="no" or n=="No":
        time.sleep(1)
        print("Proqram Kapatildi!MAC Adresiniz Degistirilmedi")
        break
    else:
        print("Gecerli Bir deyer Gir(Yes Or No)!")
