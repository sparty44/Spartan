# -*- coding: utf-8 -*-
"""
User: Brendan Teodorescu
Project: Finances Tool
"""

import sqlite3
from sqlite3 import Error

def add_banking_info(name, date, bank, bal):
    """
    Adds a bank account to the userbanking table given user,date,bank, and balance.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        c.execute("INSERT INTO userbanking (name,date,bank,balance) VALUES (?, ?, ?, ?)", (name, date, bank, bal))
        conn.commit()
        print("---------------------------------------------------------")
        print("Banking data added!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    except Error as e:
        print(e)

def add_security(name, date, symbol, qty, price):
    """
    This Function adds a row to the usersecurities table using input data.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        c.execute("INSERT INTO usersecurities (name,date,symbol,qty,price) VALUES (?, ?, ?, ?, ?)", (name, date, symbol, qty, price))
        conn.commit()
        print("---------------------------------------------------------")
        print("Security data added!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    except Error as e:
        print(e)
        
def add_asset(name, date, item_name, value):
    
        """
        This function adds a row to the usernoncash table using input data
        """
        try:
            conn = sqlite3.connect('finances.db', timeout=10)
            c = conn.cursor()
            c.execute("INSERT INTO usernoncash (name, date, item_name, value) VALUES (?, ?, ?, ?)", (name, date, item_name, value))
            conn.commit()
            print("---------------------------------------------------------")
            print("Asset data added!")
            print("---------------------------------------------------------")
            c.close()
            conn.close()
        except Error as e:
            print(e)
            
def add_monthly_cost(name, date, cost_name, cost_val):
    """
        This function adds a row to the usermonthlycosts table using input data.
    """
    try:
        conn = sqlite3.connect('finances.db', timeout=10)
        c = conn.cursor()
        c.execute("INSERT INTO usermonthlycosts (name, date, item_name, value) VALUES (?, ?, ?, ?)", (name, date, cost_name, cost_val))
        conn.commit()
        print("---------------------------------------------------------")
        print("Monthly cost entry added!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    except Error as e:
        print(e)
        
def add_monthly_income(name, date, source, val):
    """
        This function adds a row to the usermonthlyincome table using input data.
    """
    try:
        conn = sqlite3.connect('finances.db', timeout=10)
        c = conn.cursor()
        c.execute("INSERT INTO usermonthlyincome (name, date, income_source, value) VALUES (?, ?, ?, ?)", (name, date, source, val))
        conn.commit()
        print("---------------------------------------------------------")
        print("Monthly income entry added!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    except Error as e:
        print(e)

def add_saving_goal(name, date, goal_name, target_val):
    """
        This function adds a row to the usersavinggoals table using input data.
    """
    try:
        conn = sqlite3.connect('finances.db', timeout=10)
        c = conn.cursor()
        c.execute("INSERT INTO usersavinggoals (name, date, goal_name, value) VALUES (?, ?, ?, ?)", (name, date, goal_name, target_val))
        conn.commit()
        print("---------------------------------------------------------")
        print("Saving goal entry added!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    except Error as e:
        print(e)
        
def add_saving_progress(name, date, goal_name, saving_entry, saving_entry_val):
    """
        This function adds a row to the usersavingprogress table using input data.
    """
    try:
        conn = sqlite3.connect('finances.db', timeout=10)
        c = conn.cursor()
        c.execute("INSERT INTO usersavingprogress (name, date, goal_name, saving_item, value) VALUES (?, ?, ?, ?, ?)", (name, date, goal_name, saving_entry, saving_entry_val))
        conn.commit()
        print("---------------------------------------------------------")
        print("Saving goal entry added!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    except Error as e:
        print(e)
            
def remove_asset(name, item_name):
    """
    This function removes a user's asset based on user name and asset name
    """
    try:
        conn = sqlite3.connect('finances.db', timeout = 10)
        c = conn.cursor()
        
        #deleting a single row
        c.execute("DELETE FROM usernoncash WHERE name = ? AND item_name = ?", (name, item_name))
        conn.commit()
        print("---------------------------------------------------------")
        print("User asset deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1
    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete record from userassets table: ", error)
        print("---------------------------------------------------------")
        return 0
      
def remove_security(name, security_symbol):
    """
    This function removes a row from the user securities function where the
        user and security symbol are specified.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()

        #Deleting single row
        c.execute("DELETE FROM usersecurities WHERE name = ? AND symbol = ?", (name, security_symbol))
        conn.commit()
        print("---------------------------------------------------------")
        print("User security deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1
    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete record from usersecurities table: ", error)
        print("---------------------------------------------------------")
        return 0

def remove_banking(name, bank):
    """
    This function removes a row from the userbanking table where the user and bank name are specified.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        
        #Deleting single row
        c.execute("DELETE FROM userbanking WHERE name = ? AND bank = ?", (name, bank))
        conn.commit()
        print("---------------------------------------------------------")
        print("User bank deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1

    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete record from sqlite table", error)
        print("---------------------------------------------------------")
        return 0
    
def remove_monthly_cost(name, cost_name):
    """
    This function removes a row from the usermonthlycosts table where the user and cost name are specified.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        
        #Deleting single row
        c.execute("DELETE FROM usermonthlycosts WHERE name = ? AND item_name = ?", (name, cost_name))
        conn.commit()
        print("---------------------------------------------------------")
        print("User cost entry deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1

    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete record from sqlite table", error)
        print("---------------------------------------------------------")
        return 0

def remove_monthly_income(name, source):
    """
    This function removes a row from the usermonthlyincome table where the user and income source are specified.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        
        #Deleting single row
        c.execute("DELETE FROM usermonthlyincome WHERE name = ? AND income_source = ?", (name, source))
        conn.commit()
        print("---------------------------------------------------------")
        print("User income entry deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1

    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete income entry from database.", error)
        print("---------------------------------------------------------")
        return 0

def remove_saving_progress(name, goal_name, saving_entry):
    """
    This function removes a row from the usersavingprogress table.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        
        #Deleting single row
        c.execute("DELETE FROM usersavinggoals WHERE name = ? AND goal_name = ? AND saving_item = ?", (name, goal_name, saving_entry))
        conn.commit()
        print("---------------------------------------------------------")
        print("User saving progress entry deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1

    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete saving progress entry from database.", error)
        print("---------------------------------------------------------")
        return 0

def remove_saving_goal(name, goal_name):
    """
    This function removes a row from the usersavinggoals table.
    """
    try:
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        
        #Deleting single row
        c.execute("DELETE FROM usersavinggoals WHERE name = ? AND goal_name = ?", (name, goal_name))
        conn.commit()
        print("---------------------------------------------------------")
        print("User saving goal deleted successfully!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        return 1

    except sqlite3.Error as error:
        print("---------------------------------------------------------")
        print("Failed to delete saving goal from database.", error)
        print("---------------------------------------------------------")
        return 0

def update_table(table, name, date, symbol = "", qty = 0, price = 0, bank = "", acct_val = 0, asset_n = "", asset_val = 0):
    """
    Updates an entry in a table based on stipulated table name and other values.
    """
    
    if (table == "usersecurities"):
        if (qty > 0 and price == 0):
            #Update just quantity
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("UPDATE usersecurities SET qty = ?, date = ? WHERE name = ? AND symbol = ?", (qty, date, name, symbol))
            conn.commit()
            print("---------------------------------------------------------")
            print("Update successful!")
            print("---------------------------------------------------------")
            c.close()
            conn.close()
        elif (price > 0 and qty == 0):
            #update just price
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("UPDATE usersecurities SET price = ?, date = ? WHERE name = ? AND symbol = ?", (price, date, name, symbol))
            conn.commit()
            print("---------------------------------------------------------")
            print("Update successful!")
            print("---------------------------------------------------------")
            c.close()
            conn.close()
        elif (price > 0 and qty > 0):
            #update both price and quantity
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("UPDATE usersecurities SET qty = ?, price = ?, date = ? WHERE name = ? AND symbol = ?", (qty, price, date, name, symbol))
            conn.commit()
            print("---------------------------------------------------------")
            print("Update successful!")
            print("---------------------------------------------------------")
            c.close()
            conn.close()
    elif (table == "userbanking"):
        #update an account balance
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        c.execute("UPDATE userbanking SET balance = ?, date = ? WHERE name = ? AND bank = ?", (acct_val, date, name, bank))
        conn.commit()
        print("---------------------------------------------------------")
        print("Update successful!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
    elif (table == "usernoncash"):
        #update value of noncash asset
        conn = sqlite3.connect('finances.db',timeout=10)
        c = conn.cursor()
        c.execute("UPDATE usernoncash SET value = ?, date = ? WHERE name = ? AND item_name = ?", (asset_val, date, name, asset_n))
        conn.commit()
        print("---------------------------------------------------------")
        print("Update successful!")
        print("---------------------------------------------------------")
        c.close()
        conn.close()
        
def update_monthly_costs(name, date, item_name, cost_val):
    """
    Updates a cost entry in usermonthlycosts based on stipulated table name and other values.
    """
    
    conn = sqlite3.connect('finances.db',timeout=10)
    c = conn.cursor()
    c.execute("UPDATE usermonthlycosts SET value = ?, date = ? WHERE name = ? AND item_name = ?", (cost_val, date, name, item_name))
    conn.commit()
    print("---------------------------------------------------------")
    print("Update successful!")
    print("---------------------------------------------------------")
    c.close()
    conn.close()
    
def update_monthly_income(name, date, source, val):
    """
    Updates an income entry in usermonthlyincome based on stipulated table name and other values.
    """
    
    conn = sqlite3.connect('finances.db',timeout=10)
    c = conn.cursor()
    c.execute("UPDATE usermonthlyincome SET value = ?, date = ? WHERE name = ? AND income_source = ?", (val, date, name, source))
    conn.commit()
    print("---------------------------------------------------------")
    print("Income update successful!")
    print("---------------------------------------------------------")
    c.close()
    conn.close()
    
def update_saving_goal(name, date, goal, val):
    """
    Updates an income entry in usermonthlyincome based on stipulated table name and other values.
    """
    
    conn = sqlite3.connect('finances.db',timeout=10)
    c = conn.cursor()
    c.execute("UPDATE usersavinggoals SET value = ?, date = ? WHERE name = ? AND goal_name = ?", (val, date, name, goal))
    conn.commit()
    print("---------------------------------------------------------")
    print("Saving goal update successful!")
    print("---------------------------------------------------------")
    c.close()
    conn.close()
    
def output_SQLite_Table_Row(table, name, key = 0):
    
    """
    Outputs financial data owned by the specified user.
    """
    
    #Pre-initialized variables
    security_values = []
    account_values = []
    asset_values = []
    cost_values = []
    income_values = []
    value = 0
    total_value = 0
    
    #for securities
    if (table == "usersecurities"):
        try:
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM usersecurities WHERE name = (?)", (name,))
            records = c.fetchall()
            if (len(records) > 0):
                if (key == 0):
                    print("\n")
                    print("---------------------------------------------------------")
                print("Number of unique securities owned by this user: ", len(records))
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("Displaying user securities:")
                    print("\n")
                for row in records:
                    value = (row[3] * row[4])
                    security_values.append(value)
                    if (key == 0):
                        print("User Initials: ", row[0])
                        print("Last Update: ", row[1]) 
                        print("Security Prefix: ", row[2])
                        print("Share Quantity: ", row[3])
                        print("Share Price: $", row[4])
                        print("Total security value: ${:,.2f}".format(value))
                        print("------------------------------------------")
                for item in security_values:
                    total_value = total_value + item
                if (key == 0):
                    print("Combined value of all of the user's securities: ${:,.2f}".format(total_value))
                    print("---------------------------------------------------------")
                
            else:
                print("---------------------------------------------------------")
                print("This user has no stored securities.")
                print("---------------------------------------------------------")
            c.close()
            conn.close()
            return total_value
        except sqlite3.Error as error:
            print("---------------------------------------------------------")
            print("Failed to read data from securities table", error)
            print("---------------------------------------------------------")
            
    #For banking
    elif (table == "userbanking"):
        try:
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM userbanking WHERE name = (?)", (name,))
            records = c.fetchall()
            if (len(records) > 0):
                if (key == 0):
                    print("\n")
                    print("---------------------------------------------------------")
                print("Number of bank accounts owned by this user: ", len(records))
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("Displaying user accounts:")
                    print("\n")
                for row in records:
                    value = row[3]
                    account_values.append(value)
                    if (key == 0):
                        print("User Initials: ", row[0])
                        print("Date: ",row[1])
                        print("Banking Institution: ", row[2])
                        print("Account Balance: ${:,.2f}".format(row[3]))
                        print("------------------------------------------")
                for item in account_values:
                    total_value = total_value + item
                if (key == 0):
                    print("Combined value of all of the user's accounts: ${:,.2f}".format(total_value))
                    print("---------------------------------------------------------")
            else:
                print("---------------------------------------------------------")
                print("This user has no stored bank accounts.")
                print("---------------------------------------------------------")
            return total_value
        except sqlite3.Error as error:
            print("---------------------------------------------------------")
            print("Failed to read data from the banking table: ", error)
            print("---------------------------------------------------------")
            
    #For noncash assets
    elif (table == "usernoncash"):
        try:
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM usernoncash WHERE name = (?)", (name,))
            records = c.fetchall()
            if (len(records) > 0):
                if (key == 0):
                    print("\n")
                    print("---------------------------------------------------------")
                print("Number of non-cash assets owned by this user: ", len(records))
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("Displaying user non-cash assets")
                    print("\n")
                for row in records:
                    value = row[3]
                    asset_values.append(value)
                    if (key == 0):
                        print("User initials: ", row[0])
                        print("Date: ", row[1])
                        print("Asset name: ", row[2])
                        print("Asset Value: ${:,.2f}".format(row[3]))
                        print("------------------------------------------")
                for item in asset_values:
                    total_value = total_value + item
                if (key == 0):
                    print("Combined value of user's non-cash assets: ${:,.2f}".format(total_value))
                    print("---------------------------------------------------------")
            else:
                print("---------------------------------------------------------")
                print("This user has no stored non-cash assets.")
                print("---------------------------------------------------------")
            return total_value
        except sqlite3.Error as error:
            print("---------------------------------------------------------")
            print("Failed to read data from the non-cash assets table: ", error)
            print("---------------------------------------------------------")
            
    #For monthly costs
    elif (table == "usermonthlycosts"):
        try:
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM usermonthlycosts WHERE name = (?)", (name,))
            records = c.fetchall()
            if (len(records) > 0):
                if (key == 0):
                    print("\n")
                    print("---------------------------------------------------------")
                print("Number of monthly costs owed by this user: ", len(records))
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("Displaying user monthly costs")
                    print("\n")
                for row in records:
                    value = row[3]
                    cost_values.append(value)
                    if (key == 0):
                        print("Item: ", row[2])
                        print("Monthly Cost: ${:,.2f}".format(row[3]))
                        print("------------------------------------------")
                for item in cost_values:
                    total_value = total_value + item
                if (key == 0):
                    print("Total monthly costs owed by user: ${:,.2f}".format(total_value))
                    print("---------------------------------------------------------")
            else:
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("This user has no stored monthly costs.")
                    print("---------------------------------------------------------")
            return total_value
        except sqlite3.Error as error:
            print("---------------------------------------------------------")
            print("Failed to read data from the monthly costs table: ", error)
            print("---------------------------------------------------------")
            
    #For monthly income.
    elif (table == "usermonthlyincome"):
        try:
            conn = sqlite3.connect('finances.db',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM usermonthlyincome WHERE name = (?)", (name,))
            records = c.fetchall()
            if (len(records) > 0):
                if (key == 0):
                    print("\n")
                    print("---------------------------------------------------------")
                print("Number of monthly income sources owned by this user: ", len(records))
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("Displaying user monthly income sources")
                    print("\n")
                for row in records:
                    value = row[3]
                    income_values.append(value)
                    if (key == 0):
                        print("Source: ", row[2])
                        print("Monthly Income: ${:,.2f}".format(row[3]))
                        print("------------------------------------------")
                for item in income_values:
                    total_value = total_value + item
                if (key == 0):
                    print("Total monthly income: ${:,.2f}".format(total_value))
                    print("---------------------------------------------------------")
            else:
                if (key == 0):
                    print("---------------------------------------------------------")
                    print("This user has no stored monthly income.")
                    print("---------------------------------------------------------")
            return total_value
        except sqlite3.Error as error:
            print("---------------------------------------------------------")
            print("Failed to read data from the monthly income table: ", error)
            print("---------------------------------------------------------")
                      
def main():
    #Create connection to SQLite.
    conn = sqlite3.connect('finances.db',timeout=10)
    c = conn.cursor()
    #Create table
    c.execute('''CREATE TABLE IF NOT EXISTS usersecurities
             (name text, date text, symbol text, qty real, price real)''')
    c.execute('''CREATE TABLE IF NOT EXISTS userbanking
             (name text, date text, bank text, balance real)''')
    c.execute('''CREATE TABLE IF NOT EXISTS usernoncash
             (name text, date text, item_name text, value real)''')
    c.execute('''CREATE TABLE IF NOT EXISTS usermonthlycosts
             (name text, date text, item_name text, value real)''')
    c.execute('''CREATE TABLE IF NOT EXISTS usermonthlyincome
             (name text, date text, income_source text, value real)''')
    c.execute('''CREATE TABLE IF NOT EXISTS usersavinggoals
             (name text, date text, goal_name text, value real)''')
    c.execute('''CREATE TABLE IF NOT EXISTS usersavingprogress
             (name text, date text, goal_name text, saving_item text, value real)''')
    c.close()
    conn.close()
   
    #Opening loops to get username(initials) and the day's date.
    iterator = 0
    divider_iter = 0
    while (iterator == 0):
        if (divider_iter == 0):
            print("---------------------------------------------------------")
            print("Hello!")
        name = input("Enter your first and last Initials (ex: AB): ")
        name = name.upper().strip()
        if (len(name) == 2):
            iterator = 1
        else:
            print("---------------------------------------------------------")
            print("ERROR: enter only your first and last name initials.")
            print("---------------------------------------------------------")
            divider_iter = 1
    iterator = 0
    while (iterator == 0):
        date = input("Enter todays date in month/day/year format (ex: 1/2/3456): ")
        date.strip()
        if (len(date) > 7 and len(date) < 11):
            iterator = 1
        else:
            print("---------------------------------------------------------")
            print("ERROR: incorrect date format")
            print("---------------------------------------------------------")
        
    #Master loop for main user interface and transaction options.
    master_iterator = 0
    while (master_iterator == 0):
        task = input("What can I do for you today? (Options: Securities, Banking, Non-cash Assets, Net Worth, Costs, Income, Saving Tool, or Exit): ")
        task = task.lower().strip()
                
        #Ends program.
        if (task == "exit"):
            print("---------------------------------------------------------")
            print("Have a nice day!")
            print("---------------------------------------------------------")
            break
        #Loop for securities transactions.
        elif (task == "securities"):
            sec_iter = 0
            while (sec_iter == 0):
                action = input("Would you like to add, remove, update, or view securities? (Commands: add, remove, update, view, or exit): ")
                action = action.lower().strip()
                
                #Loop for adding a security to the usersecurities table in finances.db
                if (action == "add"):
                    iterator = 0
                    while (iterator == 0):
                        symbol = input("Enter the security's trading symbol (ex: ABCD): ")
                        symbol.upper().strip()
                        if (len(symbol) > 0 and len(symbol) <= 7):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: try again")
                            print("---------------------------------------------------------")
                    iterator = 0
                    while (iterator == 0):
                        string_qty = input("Enter the amount of shares: ")
                        string_qty = string_qty.strip()
                        try:
                            qty = float(string_qty)
                            if (qty > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")
                            print("---------------------------------------------------------")
                    iterator = 0
                    while (iterator == 0):
                        price_string = input("Enter the price of the security (ex: 47.55 or 35): ")
                        price_string= price_string.strip()
                        try:
                            price = float(price_string)
                            if (price > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Please enter a non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")
                            print("---------------------------------------------------------")
                    add_security(name, date, symbol, qty, price)
                    
                #Loop for removing a security from the usersecurities table.
                elif (action == "remove"):
                    iterator = 0
                    while (iterator == 0):
                        one_to_delete = input("Please enter the security's symbol: ")
                        one_to_delete = one_to_delete.upper().strip()
                        ri = remove_security(name, one_to_delete)
                        if (ri == 1):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Cannot remove security.")
                            print("---------------------------------------------------------")
                        
                #Loop for outputting/viewing user securities from usersecurities table
                elif (action == "view"):
                    output_SQLite_Table_Row("usersecurities", name)
                    
                #Loop to exit to main menu from securities.
                elif (action == "exit"):
                    sec_iter = 1
                    
                #Loop for updating a single security from the user.
                elif (action == "update"):
                    iterator = 0
                    while (iterator == 0):
                        ticker = input("Enter the ticker symbol of the security you wish to update: ")
                        ticker = ticker.upper().strip()
                        if (len(ticker) > 0 and len(ticker) < 8):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("Invalid entry. Try Again.")
                            print("---------------------------------------------------------")
                    update_action = input("Please choose an update option (quantity, price, or both): ")
                    update_action = update_action.lower().strip()
                    sec_update_iter = 0
                    while (sec_update_iter == 0):
                        if (update_action == "quantity"):
                            string_qty = input("Enter new share quantity: ")
                            try:
                                qty = float(string_qty)
                                update_table("usersecurities", name, date, ticker, qty)
                                sec_update_iter = 1
                            except ValueError:
                                print("---------------------------------------------------------")
                                print("Invalid Entry. Try again.")
                                print("---------------------------------------------------------")
                        elif (update_action == "price"):
                            string_price = input("Enter new share price: ")
                            try:
                                price = float(string_price)
                                update_table("usersecurities", name, date, ticker, 0, price)
                                sec_update_iter = 1
                            except ValueError:
                                print("---------------------------------------------------------")
                                print("Invalid Entry. Try again.")
                                print("---------------------------------------------------------")
                        elif (update_action == "both"):
                            iter2 = 0
                            while (iter2 == 0):
                                string_qty = input("Enter new share quantity: ")
                                try:
                                    qty = float(string_qty)
                                except ValueError:
                                    print("---------------------------------------------------------")
                                    print("Invalid Entry. Try again.")
                                    print("---------------------------------------------------------")
                                string_price = input("Enter new share price: ")
                                try:
                                    price = float(string_price)
                                    iter2 = 1
                                except ValueError:
                                    print("---------------------------------------------------------")
                                    print("Invalid Entry. Try again.")
                                    print("---------------------------------------------------------")
                            update_table("usersecurities", name, date, ticker, qty, price)
                            sec_update_iter = 1
                            
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Invalid Entry. Try Again...")
                            print("---------------------------------------------------------")
                            sec_update_iter = 1
                else:
                    print("---------------------------------------------------------")
                    print("ERROR: Incorrect command. Try Again.")
                    print("---------------------------------------------------------")
                    
        #Loop for banking transactions.
        elif (task == "banking"):
            bank_iter = 0
            while (bank_iter == 0):
                action = input("Would you like to add, remove, update, or view bank accounts? (Commands: add, remove, update, view, or exit): ")
                action = action.lower().strip()
                
                #Loop for adding a bank account to the userbanking table in finances.db.
                if (action == "add"):
                    iterator = 0
                    while (iterator == 0):
                        bank = input("Enter the bank's name (ex: Citizens): ")
                        bank = bank.upper().strip()
                        if (len(bank) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: try again")
                            print("---------------------------------------------------------")
                    iterator = 0
                    while (iterator == 0):
                        string_bal = input("Enter the account's balance (no comma's): ")
                        string_bal.strip()
                        try:
                            bal = float(string_bal)
                            if (bal > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")   
                            print("---------------------------------------------------------")
                    add_banking_info(name, date, bank, bal)
                    
                #Loop for removing a bank account from the userbanking table.
                elif (action == "remove"):
                    iterator = 0
                    while (iterator == 0):
                        bank = input("Please enter the bank's name: ")
                        bank = bank.upper().strip()
                        ri = remove_banking(name, bank)
                        if (ri == 1):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Cannot remove bank account.")
                            print("---------------------------------------------------------")
                
                #Loop for updating bank accounts from userbanking table.
                elif (action == "update"):
                    bank_name = input("Please enter the name of the bank institution account you wish to update: ")
                    bank_name = bank_name.upper().strip()
                    acct_val_str = input("Please enter the new account value: ")
                    acct_val_str = acct_val_str.strip()
                    iterator = 0
                    while (iterator == 0):
                        try:
                            acct_val = float(acct_val_str)
                            iterator = 1
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR... Please enter a number.")
                            print("---------------------------------------------------------")
                    update_table("userbanking", name, date, "", 0, 0, bank_name, acct_val)
                    
                #Loop for outputting/viewing user bank accounts from userbanking table.
                elif (action == "view"):
                    output_SQLite_Table_Row("userbanking", name)
                    
                #loop to exit to main menu from banking
                elif(action == 'exit'):
                    bank_iter = 1
                
                #Loop for incorrect banking commands
                else:
                    print("---------------------------------------------------------")
                    print("Incorrect banking command...")
                    print("---------------------------------------------------------")
                
        #Loop for asset transactions         
        elif(task == "assets" or task == "noncash" or task == "noncash assets" or task == "non-cash" or task == "non-cash assets"):
            asset_iter = 0
            while (asset_iter == 0):
                action = input("Would you like to add, remove, update, or view non-cash assets? (Commands: add, remove, update, view, or exit): ")
                action = action.lower().strip()
                
                #Loop for adding an asset to the asset table in finances.db.
                if (action == "add"):
                    iterator = 0
                    while (iterator == 0):
                        item_name = input("Enter the name of the asset you wish to add (ex: Pontiac Vibe): ")
                        item_name = item_name.upper().strip()
                        if (len(item_name) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: try again")
                            print("---------------------------------------------------------")
                    iterator = 0
                    while (iterator == 0):
                        string_val = input("Enter the assets's value (no comma's): ")
                        string_val = string_val.strip()
                        try:
                            val = float(string_val)
                            if (val > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")
                            print("---------------------------------------------------------")
                    add_asset(name, date, item_name, val)
                    
                #Loop for removing a non-cash asset from the userassets table.
                elif (action == "remove"):
                    iterator = 0
                    while (iterator == 0):
                        item_name = input("Please enter the name of the asset to be removed: ")
                        item_name = item_name.upper().strip()
                        ri = remove_asset(name, item_name)
                        if (ri == 1):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Unable to remove noncash asset.")
                            print("---------------------------------------------------------")
                            
                #Loops for viewing user asset listings.
                elif (action == "view"):
                    output_SQLite_Table_Row("usernoncash", name)
                    
                #Loop for updating user asset listings.
                elif (action == "update"):
                    asset_name = input("Please enter the name of the non-cash asset you wish to update: ")
                    asset_name = asset_name.upper().strip()
                    asset_val_str = input("Please enter the new asset value: ")
                    asset_val_str = asset_val_str.strip()
                    iterator = 0
                    while (iterator == 0):
                        try:
                            asset_val = float(asset_val_str)
                            iterator = 1
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR... Please enter a number.")
                            print("---------------------------------------------------------")
                    update_table("usernoncash", name, date, "", 0, 0, "", 0, asset_name, asset_val)
                
                #Loop for exiting to main menu from non-cash assets
                elif (action == "exit"):
                    asset_iter = 1
                
                #loop for incorrect asset commands
                else:
                    print("---------------------------------------------------------")
                    print("Incorrect command...")
                    print("---------------------------------------------------------")
                
        #Loop for calculating and displaying total stored value/worth.    
        elif (task == "worth" or task == "networth" or task == "net worth" or task == "net"):
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("---------------------------------------------------------")
            total_sec = output_SQLite_Table_Row("usersecurities", name,1)
            total_bank = output_SQLite_Table_Row("userbanking", name,1)
            total_noncash = output_SQLite_Table_Row("usernoncash", name,1)
            total_monthly_costs = output_SQLite_Table_Row("usermonthlycosts",name,1)
            total_monthly_income = output_SQLite_Table_Row("usermonthlyincome", name, 1)
            monthly_profit = total_monthly_income - total_monthly_costs
            net_worth = total_sec + total_bank + total_noncash
            print("")
            print("Securities total value: ${:,.2f}".format(total_sec))
            print("Banking total value: ${:,.2f}".format(total_bank))
            print("Non-cash assets total value: ${:,.2f}".format(total_noncash))
            print("")
            print("Total Monthly costs: ${:,.2f}".format(total_monthly_costs))
            print("Total Monthly income: ${:,.2f}".format(total_monthly_income))
            print("Total Monthly inflow/outflow: ${:,.2f}".format(monthly_profit))
            print("")
            print("As of: ", date)
            print("---------------------------------------------------------")
            print("The total value of this user's assets is: ${:,.2f}".format(net_worth))
            print("---------------------------------------------------------")
        
        #Loop for costs menu.
        elif (task == "costs"):
            cost_iter = 0
            while (cost_iter == 0):
                action = input("Would you like to add, remove, update, or view costs? (Commands: add, remove, update, view, or exit): ")
                action = action.lower().strip()
                
                #Loop for adding a cost to the usermonthlycosts table in finances.db.
                if (action == "add"):
                    iterator = 0
                    while (iterator == 0):
                        cost_name = input("Enter the monthly cost name (ex: rent): ")
                        cost_name = cost_name.upper().strip()
                        if (len(cost_name) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: try again")
                            print("---------------------------------------------------------")
                    iterator = 0
                    while (iterator == 0):
                        string_cost_value = input("Enter the monthly dollar value of the cost (no comma's): ")
                        string_cost_value.strip()
                        try:
                            cost_value = float(string_cost_value)
                            if (cost_value > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")   
                            print("---------------------------------------------------------")
                    add_monthly_cost(name, date, cost_name, cost_value)
                    
                #Loop for removing a cost entry from the usermonthlycosts table.
                elif (action == "remove"):
                    iterator = 0
                    while (iterator == 0):
                        cost_name = input("Please enter the cost's name: ")
                        cost_name = cost_name.upper().strip()
                        ri = remove_monthly_cost(name, cost_name)
                        if (ri == 1):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Unable to remove cost entry.")
                            print("---------------------------------------------------------")
                
                #Loop for updating user cost listings.
                elif (action == "update"):
                    cost_name = input("Please enter the name of the monthly cost you wish to update: ")
                    cost_name = cost_name.strip().upper()
                    cost_val_str = input("Please enter the new monthly cost value: ")
                    cost_val_str = cost_val_str.strip()
                    iterator = 0
                    while (iterator == 0):
                        try:
                            cost_val = float(cost_val_str)
                            iterator = 1
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR... Please enter a number.")
                            print("---------------------------------------------------------")
                    update_monthly_costs(name, date, cost_name, cost_val)
                    
                #Loop for outputting/viewing user monthly costs from usermonthlycosts table.
                elif (action == "view"):
                    output_SQLite_Table_Row("usermonthlycosts", name)
                    
                #loop to exit to main menu from costs menu
                elif(action == 'exit'):
                    cost_iter = 1
                
                #Loop for incorrect cost commands
                else:
                    print("---------------------------------------------------------")
                    print("Incorrect costs command...")
                    print("---------------------------------------------------------")
        
        #Loop for income menu.
        elif (task == "income"):
            income_iter = 0
            while (income_iter == 0):
                action = input("Would you like to add, remove, update, or view income? (Commands: add, remove, update, view, or exit): ")
                action = action.lower().strip()
                
                #Loop for adding an income entry to the usermonthlyincome table in finances.db.
                if (action == "add"):
                    iterator = 0
                    while (iterator == 0):
                        income_source = input("Enter the monthly income source (ex: FakeWorkplace Income): ")
                        income_source = income_source.upper().strip()
                        if (len(income_source) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: try again")
                            print("---------------------------------------------------------")
                    iterator = 0
                    while (iterator == 0):
                        string_income_val = input("Enter the monthly dollar value income (no comma's): ")
                        string_income_val.strip()
                        try:
                            income_val = float(string_income_val)
                            if (income_val > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")   
                            print("---------------------------------------------------------")
                    add_monthly_income(name, date, income_source, income_val)
                    
                #Loop for removing an income entry from the usermonthlyincome table.
                elif (action == "remove"):
                    iterator = 0
                    while (iterator == 0):
                        income_source = input("Please enter the income's source: ")
                        income_source = income_source.upper().strip()
                        ri = remove_monthly_income(name, income_source)
                        if (ri == 1):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Unable to remove income entry.")
                            print("---------------------------------------------------------")
                
                #Loop for updating user income listings.
                elif (action == "update"):
                    income_source = input("Please enter the source of the monthly income you wish to update: ")
                    income_source = income_source.strip().upper()
                    income_val_str = input("Please enter the new monthly income value: ")
                    income_val_str = income_val_str.strip()
                    iterator = 0
                    while (iterator == 0):
                        try:
                            income_val = float(income_val_str)
                            iterator = 1
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR... Please enter a number.")
                            print("---------------------------------------------------------")
                    update_monthly_income(name, date, income_source, income_val)
                    
                #Loop for outputting/viewing user monthly income from usermonthlyincome table.
                elif (action == "view"):
                    output_SQLite_Table_Row("usermonthlyincome", name)
                    
                #loop to exit to main menu from income menu.
                elif(action == 'exit'):
                    income_iter = 1
                
                #Loop for incorrect income commands.
                else:
                    print("---------------------------------------------------------")
                    print("Incorrect income command...")
                    print("---------------------------------------------------------")
            
        #Loop for saving calculator menu.
        elif (task == "saving tool" or task == "saving" or task == "savings tool" or task == "tool"):
            saving_iter = 0
            while (saving_iter == 0):
                action = input("Would you like to add goal, remove goal, update goal, add saving, remove saving, update saving, or view goal progress? (Commands: add goal, remove goal, update goal, add saving, remove saving, update saving, view, or exit): ")
                action = action.lower().strip()
                
                #Loop for adding saving goal entries to the usersavinggoals table in finances.db.
                if (action == "add goal"):
                    iterator = 0
                    while (iterator == 0):
                        goal_item = input("Please enter the name of the item you wish to track saving progress for: ")
                        goal_item = goal_item.upper().strip()
                        if (len(goal_item) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter an item name.")
                            print("---------------------------------------------------------")
                        
                    cost_iter = 0
                    while (cost_iter == 0):
                        target_savings_str = input("What is the cost of this item: ")
                        target_savings_str = target_savings_str.strip()
                        try:
                            target_savings = float(target_savings_str)
                            if (target_savings > 0.0):
                                cost_iter = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")   
                            print("---------------------------------------------------------")
                                
                    add_saving_goal(name, date, goal_item, target_savings)
                    
                #Loop for removing a goal entry from the usersavinggoals table.
                elif (action == "remove goal"):
                    iterator = 0
                    while (iterator == 0):
                        goal_item = input("Please enter the goal item: ")
                        goal_item = goal_item.upper().strip()
                        ri = remove_saving_goal(name, goal_item)
                        if (ri == 1):
                            iterator = 1    
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Unable to remove saving goal entry.")
                            print("---------------------------------------------------------")
                
                #Loop for updating user goal listings.
                elif (action == "update goal"):
                    goal = input("Please enter the goal you wish to update: ")
                    goal = goal.strip().upper()
                    target_str = input("Please enter the new saving target value: ")
                    target_str = target_str.strip()
                    goal_iter = 0
                    while (goal_iter == 0):
                        try:
                            target_val = float(target_str)
                            goal_iter = 1
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR... Please enter a number.")
                            print("---------------------------------------------------------")
                    update_saving_goal(name, date, goal, target_val)
                    
########################## saving entries                    
                #Loop for adding a saving progress entry to the usersavingprogress table in finances.db.
                elif (action == "add saving"):
                    iterator = 0
                    while (iterator == 0):
                        goal_item = input("Please enter the name of the item you wish to add saving progress for: ")
                        goal_item = goal_item.upper().strip()
                        if (len(goal_item) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter an item name.")
                            print("---------------------------------------------------------")
                    
                    iterator = 0
                    while (iterator == 0):
                        saving_entry = input("Enter the name of the savings entry: ")
                        saving_entry = saving_entry.upper().strip()
                        if (len(saving_entry) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a savings entry.")
                            print("---------------------------------------------------------")
                    
                    iterator = 0
                    while (iterator == 0):
                        saving_val_str = input("What is the value of this saving entry: ")
                        saving_val_str = saving_val_str.strip()
                        try:
                            saving_entry_val = float(saving_val_str)
                            if (saving_entry_val > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")   
                            print("---------------------------------------------------------")
                                
                    add_saving_progress(name, date, goal_item, saving_entry, saving_entry_val)
                   
                #Loop for removing a saving progress entry from the usersavingprogress table in finances.db.
                elif (action == "remove saving"):
                    iterator = 0
                    while (iterator == 0):
                        goal_item = input("Please enter the name of the item you wish to remove saving progress for: ")
                        goal_item = goal_item.upper().strip()
                        if (len(goal_item) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter an item name.")
                            print("---------------------------------------------------------")
                    
                    iterator = 0
                    while (iterator == 0):
                        saving_entry = input("Enter the name of the saving entry")
                        saving_entry = saving_entry.upper().strip()
                        if (len(saving_entry) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a saving entry.")
                            print("---------------------------------------------------------")
                                
                    remove_saving_progress(name, goal_item, saving_entry)
#########             
                #Loop for updating user saving entry listings.
                elif (action == "update saving"):
                    iterator = 0
                    while (iterator == 0):
                        goal_item = input("Please enter the name of the item you wish to update saving progress for: ")
                        goal_item = goal_item.upper().strip()
                        if (len(goal_item) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter an item name.")
                            print("---------------------------------------------------------")
                    
                    iterator = 0
                    while (iterator == 0):
                        saving_entry = input("Enter the name of the saving entry")
                        saving_entry = saving_entry.upper().strip()
                        if (len(saving_entry) > 0):
                            iterator = 1
                        else:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a saving entry.")
                            print("---------------------------------------------------------")
                    
                    iterator = 0
                    while (iterator == 0):
                        saving_val_str = input("What is the new value of this saving entry?: ")
                        saving_val_str = saving_val_str.strip()
                        try:
                            saving_entry_val = float(saving_val_str)
                            if (saving_entry_val > 0.0):
                                iterator = 1
                            else:
                                print("---------------------------------------------------------")
                                print("ERROR: Enter non-zero number.")
                                print("---------------------------------------------------------")
                        except ValueError:
                            print("---------------------------------------------------------")
                            print("ERROR: Please enter a number...")   
                            print("---------------------------------------------------------")   
                            
                    update_saving_progress(name, date, goal_item, saving_item, saving_entry_val)
                    
                    
                    
                    
                    
                    
                    
                    
                #Loop for outputting/viewing user saving goals from usersavinggoals table.
                elif (action == "view"):
                    output_SQLite_Table_Row("usersavinggoals", name)
                    
                #loop to exit to main menu from saving calculator menu.
                elif(action == 'exit'):
                    saving_iter = 1
                
                #Loop for incorrect saving calculator commands.
                else:
                    print("---------------------------------------------------------")
                    print("Incorrect saving calculator command...")
                    print("---------------------------------------------------------")
            
            
            
            
            
                    
        #Loop for all other erroneous answers.
        else:
            print("---------------------------------------------------------")
            print("ERROR: Incorrect command...")
            print("---------------------------------------------------------")
        
        
                                 
if __name__ == '__main__':
    main()


