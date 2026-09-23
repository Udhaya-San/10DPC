import time
import webbrowser

import requests
from bs4 import BeautifulSoup           # from beautifulsoup4
from rich.console import Console        # from rich
from rich.table import Table

console = Console()
url = "https://www.google.com"

# Fetch the page, with a spinner while waiting
with console.status(f"[bold cyan]Fetching {url}..."):
    time.sleep(1)
    response = requests.get(url, timeout=10)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string if soup.title else "No title"
links = soup.find_all("a")

# Show the results as a table
table = Table(title="Page Summary")
table.add_column("Item", style="bold magenta")
table.add_column("Value", style="green")
table.add_row("URL", url)
table.add_row("Status code", str(response.status_code))
table.add_row("Page title", title)
table.add_row("Number of links", str(len(links)))
console.print(table)

# Print the first 5 links
console.print("\n[bold yellow]First 5 links:[/]")
for a in links[:5]:
    console.print(f"  • {a.get_text(strip=True) or '(no text)'} → {a.get('href')}")

# Open the site in the browser
console.print("\n[bold green]Opening in browser...[/]")
webbrowser.open(url)