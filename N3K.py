import os
import sys
import datetime
import shutil
from cfonts import render  
from rich.console import Console
from rich.table import Table
import requests
columns, _ = shutil.get_terminal_size()
border = "═" * (columns - 2) 
kral = render('#NIKZ', colors=['green', 'yellow'], align='center')
print(f"\033[1;38m╔{border}╗")  
print(kral)  
print(f"\033[1;32m       🕵️‍♂️ JACKING TOOLS   |   🛠️ Developer: @NikzPy  ")  
print(f"\033[1;39m╚{border}╝\n")  
console = Console()
table = Table(title="🔥 VIP  CONTROL PANEL", style="bold green", expand=True)
table.add_column("🔢 No.", justify="center", style="bold cyan", no_wrap=True)
table.add_column("⚡ Feature Name", style="bold yellow")
table.add_column("🟢 Status", justify="center", style="bold green")
options = [
    ("1️⃣", "📜  HUNTER (G+A) (META)","   ✅ Active"),
    ("2️⃣", "📜  GMAIL + AOL (META)","   ✅ Active"),
    ("3️⃣", "🗑️  OLD All AGE IG ","✅ Active"),
    ("4️⃣", "📧  Reset Tool", "  ✅ Active"),
      ("5️⃣", "🛠️  Former Username Remover", "  ❌ Inactive"),
    ("6️⃣", "🎯  Reporting Tool", "    ❌ Inactive"),
]
for num, feature, status in options:
    table.add_row(num, feature, status)
console.print(table)
import os
import requests

# Dictionary mapping numbers (1-10) to different script URLs
script_links = {
    1: "https://raw.githubusercontent.com/nikzffx/NIKZ/refs/heads/main/Hunter.py",
    2: "https://raw.githubusercontent.com/nikzffx/NIKZ/refs/heads/main/Vip%20G%2BA.py",
    3:"https://raw.githubusercontent.com/nikzffx/NIKZ/refs/heads/main/Old%20Is%20Gold.py",
    4:"https://raw.githubusercontent.com/nikzffx/NIKZ/refs/heads/main/passrest.py"
}

def fetch_and_execute(choice):
    """Fetch and execute the selected script"""
    if choice in script_links:
        url = script_links[choice]
        try:
            script_content = requests.get(url)
            if script_content.status_code == 200:  # Check if the request was successful
                exec(script_content.text, globals())
            else:
                print("❌ Failed to fetch the script. Status code:", script_content.status_code)
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching the script: {e}")
    else:
        print("❌ Invalid choice! Please select a valid option.")

# Get user input
try:
    user_choice = int(input("Enter a number (1-4) to select a script: "))
    os.system('cls' if os.name == 'nt' else 'clear')  # Use 'cls' for Windows and 'clear' for UNIX systems
    fetch_and_execute(user_choice)
except ValueError:
    print("❌ Invalid input! Please enter a number between 1 and 4.")
