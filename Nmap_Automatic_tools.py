#!/usr/bin/env python3
"""
Nmap Automation Tool - darkboss1bd
Professional Network Scanning Tool with Advanced Features
"""

import os
import sys
import subprocess
import threading
import time
from datetime import datetime
import webbrowser

class DarkBossNmapScanner:
    def __init__(self):
        self.results = {}
        self.banner = """
\033[92m
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗║
║    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔═══██╗██╔════╝║
║    ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║   ██║███████╗║
║    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║╚════██║║
║    ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████║║
║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝║
║                                                              ║
║                  N M A P   A U T O M A T O R                 ║
║                     by darkboss1bd                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
\033[0m
        """
        
        self.contacts = {
            'telegram_id': 'https://t.me/darkvaiadmin',
            'telegram_channel': 'https://t.me/windowspremiumkey',
            'website': 'https://crackyworld.com/'
        }

    def display_banner(self):
        print(self.banner)
        print("\033[93m" + "="*70 + "\033[0m")
        print("\033[96m📱 Telegram ID:\033[0m", self.contacts['telegram_id'])
        print("\033[96m📢 Telegram Channel:\033[0m", self.contacts['telegram_channel'])
        print("\033[96m🌐 Website:\033[0m", self.contacts['website'])
        print("\033[93m" + "="*70 + "\033[0m")
        print()

    def open_links(self):
        print("\033[94m[*] Opening contact links...\033[0m")
        for name, url in self.contacts.items():
            try:
                webbrowser.open_new_tab(url)
                print(f"\033[92m[+] Opened: {name}\033[0m")
                time.sleep(1)
            except Exception as e:
                print(f"\033[91m[!] Failed to open {name}: {e}\033[0m")

    def check_nmap_installation(self):
        try:
            result = subprocess.run(['nmap', '--version'], capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def run_nmap_scan(self, target, scan_args):
        try:
            print(f"\033[94m[*] Running: nmap {scan_args} {target}\033[0m")
            
            cmd = ['nmap'] + scan_args.split() + [target]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                return result.stdout
            else:
                print(f"\033[91m[!] Nmap error: {result.stderr}\033[0m")
                return None
                
        except Exception as e:
            print(f"\033[91m[!] Scan failed: {e}\033[0m")
            return None

    def scan_target(self, target, scan_type="quick"):
        scan_commands = {
            "quick": "-T4 -F",
            "intense": "-T4 -A -v",
            "comprehensive": "-p- -sV -sC -A -O",
            "stealth": "-sS -T2 -f",
            "udp": "-sU -T4",
            "vulnerability": "-sV --script vuln",
            "os_detection": "-O -sV"
        }
        
        if scan_type not in scan_commands:
            print("\033[91m[!] Invalid scan type!\033[0m")
            return None

        command = scan_commands[scan_type]
        return self.run_nmap_scan(target, command)

    def display_scan_results(self, results):
        if not results:
            print("\033[91m[!] No results to display!\033[0m")
            return

        print("\n" + "="*70)
        print("\033[95m🎯 SCAN RESULTS\033[0m")
        print("="*70)
        print(results)
        print("="*70)

    def save_results(self, target, scan_type, results):
        if not results:
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"scan_results_{target}_{scan_type}_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write(f"DarkBoss Nmap Scanner - darkboss1bd\n")
                f.write(f"Scan Date: {datetime.now()}\n")
                f.write(f"Target: {target}\n")
                f.write(f"Scan Type: {scan_type}\n")
                f.write("="*50 + "\n")
                f.write(results)
            
            print(f"\033[92m[+] Results saved to: {filename}\033[0m")
        except Exception as e:
            print(f"\033[91m[!] Failed to save results: {e}\033[0m")

    def show_scan_menu(self):
        print("\n\033[95m🔍 SCAN MENU:\033[0m")
        print("\033[93m1.\033[0m Quick Scan (Fast port scan)")
        print("\033[93m2.\033[0m Intense Scan (Comprehensive scan)")
        print("\033[93m3.\033[0m Comprehensive Scan (All ports + services)")
        print("\033[93m4.\033[0m Stealth Scan (Slow & stealthy)")
        print("\033[93m5.\033[0m UDP Scan")
        print("\033[93m6.\033[0m Vulnerability Scan")
        print("\033[93m7.\033[0m OS Detection")
        print("\033[93m8.\033[0m Custom Scan")
        print("\033[93m0.\033[0m Exit")

    def run_custom_scan(self, target):
        print("\n\033[95m🎛️  CUSTOM SCAN\033[0m")
        print("Enter nmap arguments (e.g., '-sS -p 80,443 -A'):")
        custom_args = input("\033[96mArguments: \033[0m").strip()
        
        if custom_args:
            return self.run_nmap_scan(target, custom_args)
        return None

def main():
    scanner = DarkBossNmapScanner()
    
    scanner.display_banner()
    
    link_thread = threading.Thread(target=scanner.open_links)
    link_thread.daemon = True
    link_thread.start()
    
    if not scanner.check_nmap_installation():
        print("\033[91m[!] Nmap is not installed or not in PATH!\033[0m")
        print("\033[94m[*] Please install nmap to use this tool:\033[0m")
        print("    Windows: Download from https://nmap.org/download.html")
        print("    Linux: sudo apt-get install nmap")
        print("    Mac: brew install nmap")
        sys.exit(1)
    
    print("\033[92m[✓] Nmap is installed and ready!\033[0m")
    
    while True:
        try:
            print("\n\033[95m🎯 TARGET SELECTION:\033[0m")
            target = input("\033[96mEnter target (IP/hostname/range) or 'quit' to exit: \033[0m").strip()
            
            if target.lower() in ['quit', 'exit', 'q']:
                print("\033[92m[+] Thank you for using DarkBoss Nmap Scanner! 👋\033[0m")
                break
            
            if not target:
                print("\033[91m[!] Please enter a valid target!\033[0m")
                continue
            
            scanner.show_scan_menu()
            choice = input("\n\033[96mSelect scan type (1-8): \033[0m").strip()
            
            scan_types = {
                '1': 'quick',
                '2': 'intense',
                '3': 'comprehensive',
                '4': 'stealth',
                '5': 'udp',
                '6': 'vulnerability',
                '7': 'os_detection',
                '8': 'custom'
            }
            
            if choice == '0':
                continue
            elif choice == '8':
                results = scanner.run_custom_scan(target)
                scan_type = 'custom'
            elif choice in scan_types:
                scan_type = scan_types[choice]
                results = scanner.scan_target(target, scan_type)
            else:
                print("\033[91m[!] Invalid choice!\033[0m")
                continue
            
            if results:
                scanner.display_scan_results(results)
                save_choice = input("\n\033[96mSave results to file? (y/n): \033[0m").strip().lower()
                if save_choice == 'y':
                    scanner.save_results(target, scan_type, results)
            
        except KeyboardInterrupt:
            print("\n\n\033[92m[+] Scan interrupted by user. Goodbye! 👋\033[0m")
            break
        except Exception as e:
            print(f"\033[91m[!] An error occurred: {e}\033[0m")

if __name__ == "__main__":
    main()
