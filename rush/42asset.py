import sys
import os
import json
from datetime import datetime

asset_next_id = 1
asset_list = []

DATA_FILE = "assets.json"

def load_assets():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ File corrupted, build new data...")
        return []

def save_assets(assets):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=4, ensure_ascii=False)

def find_next_id(assets):
    max_object = max(assets, key=lambda item: item["id"], default={"id": 0})
    return max_object["id"] + 1

def global_load():
    global asset_list
    global asset_next_id
    asset_list = load_assets()
    asset_next_id = find_next_id(asset_list)

def global_persist():
    save_assets(asset_list)

def get_id() :
    global asset_next_id
    current_id = asset_next_id
    asset_next_id += 1
    return current_id

def print_error(msg):
    print(f"⚠️ Error: {msg}")
    return

def confirm_with_yes(prompt):
    yes_or_no = (
        input(f"{prompt} (yes/no): ")
        .strip()
        .lower()
    )

    if yes_or_no == "yes":
        return True
    else:
        return False 

def is_serial_exist(serial_number):
    check_serial_number = [item for item in asset_list if item["serial_number"] == serial_number]
    if len(check_serial_number) > 0:
        return True
    else:
        return False

def find_asset_by_id(asset_id):
    target_list = [item for item in asset_list if item["id"] == int(asset_id)]
    if len(target_list) == 0:
        return {"ok": False, "asset": {}, "asset_index": -1}
    else:
        asset = target_list[0]
        index = asset_list.index(asset)
        return {"ok":True, "asset": asset, "index": index}

def asset_count():
    return len(asset_list)

def do_add_asset():
    print("\n--- Add new asset ---")
    name = input("Asset name: ").strip()
    category = input("Category (ex. Laptop, Mobile, Chair): ").strip()
    serial_number = input("Serial Number: ").strip()
    assigned_to = input("Responsible person / User (optional): ").strip()

    if not name or not category or not serial_number:
        print_error("Name, Category and Serial No. are required!")
        return

    id = get_id()
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if is_serial_exist(serial_number):
        print_error("This serial number already exist in the system.")
    else:
        asset_record = { "id": id, "name":name, "category": category, "serial_number": serial_number, "assigned_to": assigned_to, "status": "Active", "date_added": date_added}
        asset_list.append(asset_record)
        print(f"🎉 The asset: '{name}' has been added!")
        global_persist()


def do_view_assets():
    print("\n--- All assets ---")

    if len(asset_list) < 1:
        print("No asset data in the system")
        return

    # Display in table format
    template = "{:<5} {:<20} {:<15} {:<15} {:<15} {:<10}"
    print(
        template.format("ID", "Name", "Category", "Serial No.", "User", "Status")
    )
    print("-" * 85)

    for asset in asset_list:
        print(
            template.format(
                asset["id"],
                asset["name"][:18],
                asset["category"][:13],
                asset["serial_number"][:13],
                asset["assigned_to"][:13] if asset["assigned_to"] else "-",
                asset["status"],
            )
        )
    total = asset_count()
    print(f'\nTotal: {total}')

def do_update_asset():
    print("\n--- Udate asset ---")
    asset_id = input("Choose ID of asset to be updated: ").strip()

    if not asset_id.isdigit():
        print_error("ID must be numbers")
        return
    
    result = find_asset_by_id(asset_id)

    if not result["ok"]:
        print("🥺 Not found asset with this ID")
        return

    asset = result["asset"]
    asset_index = result["index"]

    print(
        f"Asset founded: {asset['name']} (Status: {asset['status']}, User: {asset['assigned_to'] or '-'})"
    )

    new_assigned = input(
        f"Change user (Press Enter to keep the original [{asset['assigned_to']}]): "
    ).strip()
    new_status = input(
        f"Change status (Active/Maintenance/Retired) (Press Enter to keep the original): "
    ).strip()

    # Use previous values if leave blank
    final_assigned = (
        new_assigned if new_assigned else asset["assigned_to"]
    )
    final_status = new_status if new_status else asset["status"]

    asset['assigned_to'] = final_assigned
    asset['status'] = final_status

    asset_list[asset_index] = asset

    print("✨ Data updated!")
    global_persist()


def do_delete_asset():
    print("\n--- Delete asset ---")
    global asset_list
    asset_id = input("Enter ID of the asset to be deleted: ").strip()

    if not asset_id.isdigit():
        print_error("ID must be number")
        return

    result = find_asset_by_id(asset_id)

    if not result["ok"]:
        print("🥺 Not found asset with this ID")
        return

    target_asset = result["asset"]
    target_asset_name = target_asset["name"]
    target_asset_index = result["index"]
    if confirm_with_yes(f"Please confirm that you want to delete '{target_asset_name}'?") :
        asset_list.pop(target_asset_index)
        print("🗑️ the asset deleted")
        global_persist()
    else:
        print("Abort deletion process")

def do_exit():
    print("\nThanks for using our system! See you. 👋")
    global_persist()
    sys.exit()

def main_menu():
    global_load()

    while True:
        print("\n_____________________________\n")
        print(" Asset42 : Asset Tracking ")
        print("_____________________________\n")
        print(" 1. List all assets")
        print(" 2. Add new asset")
        print(" 3. Update asset")
        print(" 4. Delete asset")
        print(" 5. Exit")
        print("_____________________________")

        choice = input("Select Menu (1-5): ").strip()

        if choice == "1":
            do_view_assets()
        elif choice == "2":
            do_add_asset()
        elif choice == "3":
            do_update_asset()
        elif choice == "4":
            do_delete_asset()
        elif choice == "5" or choice.upper() == "EXIT":
            do_exit()
        else:
            print("🥺 Incorrect option. Please choose 1-5")


if __name__ == "__main__":
    main_menu()
