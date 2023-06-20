import tkinter as tk

class CounterGUI:
    def __init__(self, categories):
        self.counts = {category: 0 for category in categories}

        # Create the GUI window
        self.window = tk.Tk()
        self.window.title("Category Counters")

        # Create the widgets for each category
        self.widgets = {}
        for category in categories:
            # Create the label
            label = tk.Label(self.window, text=f"{category} Count: {self.counts[category]}")
            label.grid(row=categories.index(category), column=0)

            # Create the plus button
            plus_button = tk.Button(self.window, text="+", fg="white", bg="green",
                                    command=lambda cat=category: self.increment_count(cat))
            plus_button.grid(row=categories.index(category), column=1)

            # Create the minus button
            minus_button = tk.Button(self.window, text="-", fg="white", bg="red",
                                     command=lambda cat=category: self.decrement_count(cat))
            minus_button.grid(row=categories.index(category), column=2)

            # Save the widgets for later access
            self.widgets[category] = (label, plus_button, minus_button)

    def run(self):
        self.window.mainloop()

    def increment_count(self, category):
        self.counts[category] += 1
        self.widgets[category][0].config(text=f"{category} Count: {self.counts[category]}")

    def decrement_count(self, category):
        self.counts[category] -= 1
        self.widgets[category][0].config(text=f"{category} Count: {self.counts[category]}")


# Define the categories
categories = ["Mental Health", "Course Availability/Registration", "Dining",
              "Transportation", "Housing", "Study Spaces", "Course Structure/Difficulty",
              "Advising/Tutoring", "Student Activities", "Infrastructure"]

# Create a CounterGUI instance for all categories
gui = CounterGUI(categories)

# Run the GUI
gui.run()
