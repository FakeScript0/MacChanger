import subprocess
import time
import optparse
option=optparse.OptionParser()
option.add_option("-i",dest="interface",help="Interface")
option.add_option("-m",dest="mac_adress",help="Mac Adress")
(user_input,arguments)=option.parse_args()

mac_adress=(user_input.mac_adress)
interface=(user_input.interface)
print("Mac Degistirici Proqraminiz Ise Basladi!")
time.sleep(1)
print("Mac Adresinizi Degistirmek istiyorsaniz (y) eks halda (n) Yazin!")

while True:
    n=input()
    if n=="y" or n=="Yes" or n=="yes":
        time.sleep(0.8)
        print("Mac Adresiniz Degistiriliyor!")
        time.sleep(2)

        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",mac_adress])
        subprocess.call(["ifconfig",interface,"up"])
        mac=subprocess.check_output(["ifconfig",interface])
        print("""
        Melumat:
        
        
        {}
        
        
            """.format(mac))
        print("\nMac Adresiniz Degistirildi")
        break
    elif n=="n" or n=="no" or n=="No":
        time.sleep(1)
        print("Proqram Kapatildi!MAC Adresiniz Degistirilmedi")
        break
    else:
        print("Gecerli Bir deyer Gir(Yes Or No)!")
