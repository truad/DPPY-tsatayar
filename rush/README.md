# 💻 Project: Asset42

## 🎯 Purpose

This project is a simple, command-line interface (CLI) application designed to help users track inventory and manage corporate or personal physical assets. It provides a structured way to record, view, update, and delete details for items like laptops, chairs, or mobile devices, ensuring that assets are easily accounted for within the organization.

## ✨ Main Features

- **Asset Tracking**: Records essential details for each item, including Name, Category, Serial Number, and Assigned User.
- **Data Persistence:** Uses a local JSON file (`assets.json`) to save all asset records, ensuring that data persists between sessions.
- **Add New Assets**: Allows users to input all required details for a brand new asset. It validates that the serial number does not already exist.
- **View Inventory**: Displays a comprehensive, table-formatted list of all tracked assets, including ID, Name, Category, Serial Number, User, and Status.
- **Update Records**: Enables modifying the assignment user or the operational status (Active, Maintenance, Retired) of an existing asset using its unique ID.
- **Delete Assets**: Safely removes assets from the inventory list after requiring user confirmation.
- **Status Management**: Assets can be assigned a status (e.g., Active, Maintenance, Retired) to help manage their lifecycle.

## 🚀 Instructions to Run

### Prerequisites

You need to have Python installed on your system (Python 3.x is recommended).

### Setup

1. Save the Code: Save the provided Python code into a file named `42asset.py`.
2. Run the Script: Open your terminal or command prompt and navigate to the directory where you saved the file.
3. Execute the script using the following command:
    ```
    $python3 42asset.py
    ```

### Usage Guide

The program will launch the main menu, allowing you to interact with the system:

| Option | Action | Description |
| --- | --- | --- |
| 1 | List all assets | Displays all current assets in a formatted table. |
| 2 | Add new asset | Prompts for asset details (Name, Category, Serial Number, User). |
| 3 | Update asset | Choose an Asset ID to change the assigned user or the status. |
| 4 | Delete asset | Choose an Asset ID and prompts for confirmation before deletion. |
| 5 | Exit | Saves all current data to assets.json and quits the application. |

---

*Note: All data entered and managed by the application will be saved to a file named `assets.json` in the same directory.*