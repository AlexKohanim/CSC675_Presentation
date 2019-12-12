#!/usr/bin/env python3

import pymysql

host = '0.0.0.0'
user_name = 'root'
password = None
db_name = 'delership'

db = pymysql.connect(host, user_name, password, db_name)
cursor = db.cursor()


with open("employee.csv", 'r') as file:
    file.readline()
    # file.readline()

    for line in file.readlines():
        line = line.strip("\n")
        print(line)
        line = line.replace("'", "")
        line = ",".join("'" + str(x) + "'" for x in line.split(","))
        print(line)
        print(line.index(","))
        query = """
        INSERT IGNORE INTO `Employees` (`Name`, `NumSales`, `Salary` )  
        VALUES ( """ + line + """);

        """
        cursor.execute(query)
        db.commit()



with open("customers.csv", 'r') as file:
    file.readline()
    # file.readline()

    for line in file.readlines():
        line = line.strip("\n")
        print(line)
        # line = line.replace("'", "")
        line = ",".join("'" + str(x) + "'" for x in line.split(","))
        print(line)
        print(line.index(","))
        query = """
        INSERT IGNORE INTO `Customers` (`Phone`, `Email`, `Name` )  
        VALUES ( """ + line + """);

        """
        cursor.execute(query)
        db.commit()


with open("cars.csv", 'r') as file:
    file.readline()
    file.readline()

    for line in file.readlines():
        line = line.strip("\n")
        print(line)
        line = line.replace("'", "")
        line = ",".join("'" + str(x) + "'" for x in line.split(","))
        print(line)
        print(line.index(","))
        query = """
        INSERT IGNORE INTO `Cars` (`Model`, `Inventory`, `MSRP`, `Year` )  
        VALUES ( """ + line + """);

        """
        cursor.execute(query)
        db.commit()


with open("sales.csv", 'r') as file:
    file.readline()
    # file.readline()

    for line in file.readlines():
        line = line.strip("\n")
        print(line)
        # line = line.replace("'", "")
        line = ",".join("'" + str(x) + "'" for x in line.split(","))
        print(line)
        print(line.index(","))
        query = """
        INSERT IGNORE INTO `Sales` (`Cid`, `Pid`, `SalePrice`, `Eid` )  
        VALUES ( """ + line + """);

        """
        cursor.execute(query)
        db.commit()