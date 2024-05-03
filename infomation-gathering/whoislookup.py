# pip install python-whois

import whois
domain= input("Enter Domain you want to know about : ")

opt = input("Do you want to save output in any file (y/n) : ")
if(opt == 'y'):
    fileName = f"{domain}.txt"
    with open(fileName, 'w') as file:
        whois_info = str(whois.whois(domain))
        file.write(whois_info)
    print(f"WHOIS information saved to '{fileName}'")
else:
    print(whois.whois(domain))

    
