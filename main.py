import os
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

# --- Neon Glow Palette ---
G = Fore.GREEN + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
R = Fore.RED + Style.BRIGHT
M = Fore.MAGENTA + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT

OWNER_NAME = "ROMAN HACKER"

def banner():
    os.system('clear')
    print(f"{C}┌" + "─"*45 + "┐")
    print(f"{C}│{M}    ⚡ {W}{OWNER_NAME} KING 👑 BANNER {C}       │")
    print(f"{C}├" + "─"*45 + "┤")
    print(f"{C}│ {G}Dev: {W}{OWNER_NAME:<12} {G}Ver: {W}2.5.0  {C}│")
    print(f"{C}│ {G}Status: {W}Online      {G}Mode: {W}Proxy  {C}│")
    print(f"{C}└" + "─"*45 + "┘")

    print(f"\n{M}[{W}1{M}] {W}Start 24h Review Strike")
    print(f"{M}[{W}2{M}] {W}Update Proxy Nodes")
    print(f"{M}[{W}3{M}] {W}Exit System")
    print(f"\n{C}" + "━"*47)

def simulate_strike(target):
    print(f"\n{C}📡 Initializing Secure Tunnel...")
    time.sleep(1.5)
    print(f"{G}🔗 Connected to 127.0.0.1:8080 (Encrypted)")
    time.sleep(1)
    
    reasons = ["Spam", "Harassment", "TOS Violation", "Bot Activity"]
    
    for i in range(1, 51):
        reason = random.choice(reasons)
        ticket = f"RH-{random.randint(100, 999)}-STK"
        
        # Fake Progress Effect
        print(f"{G}⚡ STRIKE {i}/50 {W}>>> {M}Target: {W}{target} {G}[{reason}] {Y}{ticket}")
        
        # Random delay to make it look real
        time.sleep(random.uniform(0.1, 0.5)) 

    print(f"\n\n{G}✅ MISSION ACCOMPLISHED! TARGET {target} IS UNDER REVIEW.")
    print(f"{Y}Expect results within 24-48 hours.")

def main():
    while True:
        banner()
        cmd = input(f"{M}ROMAN{W}@{C}HACKER{W}:~# ")
        
        if cmd == "1":
            target = input(f"\n{Y}Target Number/+92: {W}")
            if target:
                simulate_strike(target)
                input(f"\n{C}Press Enter to return...")
        elif cmd == "2":
            print(f"\n{C}🔄 Fetching new nodes...")
            time.sleep(2)
            print(f"{G}Done! 154 Nodes Active.")
            time.sleep(1)
        elif cmd == "3":
            print(f"{R}System Shutting Down...")
            break

if __name__ == "__main__":
    main()
  
