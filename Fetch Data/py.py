import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

# Function to fetch data from the given URL and save it to a file
def fetch_data():
    url = entry.get()  # Get the URL entered in the input field
    
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return

    try:
        # Send a GET request to the website
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Open a text file to save the data
            with open('output_data.txt', 'w', encoding='utf-8') as file:
                # Extract data (for example, all paragraph text)
                paragraphs = soup.find_all('p')
                for p in paragraphs:
                    file.write(p.text + '\n')  # Write each paragraph to the file
            
            messagebox.showinfo("Success", "Data saved to output_data.txt")
        else:
            messagebox.showerror("Error", f"Failed to retrieve data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Website Data Fetcher")

# Create a label for the URL entry
label = tk.Label(root, text="Enter the Website URL:")
label.pack(pady=10)

# Create an entry widget to accept URL input
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create a button to trigger the fetch_data function
button = tk.Button(root, text="Fetch Data", command=fetch_data)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
