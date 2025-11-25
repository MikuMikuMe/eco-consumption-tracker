Creating an eco-consumption tracker that monitors household energy, water, and waste consumption requires developing an application that collects data, analyzes it, and provides recommendations. Below is a simplified version of such an application in Python. This example uses a command-line interface for simplicity. More complex applications might use databases, APIs, and graphical user interfaces, but this illustrates the core functionality:

```python
import json
import datetime

class EcoConsumptionTracker:
    def __init__(self):
        self.data = {
            'energy': [],
            'water': [],
            'waste': []
        }
        self.load_data()

    def load_data(self):
        """
        Load consumption data from a JSON file.
        """
        try:
            with open('consumption_data.json', 'r') as file:
                self.data = json.load(file)
                print("Data loaded successfully.")
        except FileNotFoundError:
            # If the file does not exist, continue with an empty dataset
            print("No existing data found, starting with an empty dataset.")
        except json.JSONDecodeError:
            print("Error decoding JSON file, starting with an empty dataset.")

    def save_data(self):
        """
        Save consumption data to a JSON file.
        """
        try:
            with open('consumption_data.json', 'w') as file:
                json.dump(self.data, file, indent=4)
                print("Data saved successfully.")
        except IOError as e:
            print(f"An error occurred while saving data: {e}")

    def log_consumption(self, resource_type, amount):
        """
        Log consumption data for a specific resource type.
        """
        resource_data = self.data.get(resource_type)
        if resource_data is not None:
            resource_entry = {
                'date': datetime.datetime.now().strftime('%Y-%m-%d'),
                'amount': amount
            }
            resource_data.append(resource_entry)
            print(f"{resource_type.capitalize()} consumption logged: {amount}")
        else:
            print(f"Resource type '{resource_type}' is not recognized.")

    def generate_report(self):
        """
        Generate a consumption report with recommendations.
        """
        print("\n--- Consumption Report ---")
        for resource_type, records in self.data.items():
            total = sum(record['amount'] for record in records)
            print(f"{resource_type.capitalize()}: Total consumption = {total}")
            self.provide_recommendations(resource_type, total)

    def provide_recommendations(self, resource_type, total):
        """
        Provide recommendations based on the total consumption.
        """
        recommendations = {
            'energy': "Consider using energy-efficient appliances or LED lighting.",
            'water': "Consider shorter showers or fixing leaks.",
            'waste': "Improve recycling efforts or compost organic waste."
        }
        if total > 100: # arbitrary threshold for demo purposes
            print(f"Recommendation for {resource_type}: {recommendations.get(resource_type, 'No recommendation available.')}")
        else:
            print(f"{resource_type.capitalize()} consumption is within acceptable limits.")

    def main(self):
        """
        Main method to drive the tracker.
        """
        while True:
            print("\n1. Log Energy Consumption")
            print("2. Log Water Consumption")
            print("3. Log Waste Production")
            print("4. Generate Report")
            print("5. Exit")

            choice = input("Select an option: ")

            try:
                if choice == '1':
                    amount = float(input("Enter energy consumption (kWh): "))
                    self.log_consumption('energy', amount)
                elif choice == '2':
                    amount = float(input("Enter water usage (liters): "))
                    self.log_consumption('water', amount)
                elif choice == '3':
                    amount = float(input("Enter waste production (kg): "))
                    self.log_consumption('waste', amount)
                elif choice == '4':
                    self.generate_report()
                elif choice == '5':
                    self.save_data()
                    print("Exiting Eco Consumption Tracker.")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

# Create the tracker and start the main program loop
tracker = EcoConsumptionTracker()
tracker.main()
```

### Key Features and Considerations:

1. **Data Storage**: The program saves consumption data in a JSON file, allowing persistence across sessions. This is simple and suitable for small datasets.

2. **Error Handling**: The program includes error handling for file operations and user inputs to prevent and handle common issues.

3. **Recommendations**: It offers simple recommendations based on consumption levels. These recommendations can be expanded with more detailed criteria.

4. **User Interaction**: It uses a command-line interface where users can log their consumption patterns and generate reports.

5. **Extensibility**: The program structure allows for easy extension. For example, by expanding the data model, adding a graphical interface, connecting to sensors or APIs, or integrating advanced analytics.

This is a foundational program. Inproduction systems, you'd likely want to integrate with external data sources (like IoT devices or utility provider data), use a database for storage, and implement a more sophisticated user interface.