import tkinter as tkt
import statistics

# Function to calculate and display mean, median, and mode
def calculate_stats():
    try:
        data = list(map(float, entry.get().split(",")))
        mean = statistics.mean(data)
        median = statistics.median(data)
        mode = statistics.mode(data)
        result_label.config(text=f"Mean: {mean}\nMedian: {median}\nMode: {mode}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Mean, Median, Mode Calculator")

# Input field
entry_label = tk.Label(root, text="Enter numbers separated by commas:")
entry_label.pack()
entry = tk.Entry(root, width=30)
entry.pack()

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate_stats)
calculate_button.pack()

# Label to display results
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
