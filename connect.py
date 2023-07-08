import pyodbc
import tkinter as tk
from jinja2 import Template

root = tk.Tk()
root.title("Enter Data")

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-EP03SKT;"
                      "Database=Wardrobe;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()



# Type
label = tk.Label(root, text="Type")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Name
label2 = tk.Label(root, text="Name")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Brand
label3 = tk.Label(root, text="Brand")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

# Color
label4 = tk.Label(root, text="Color")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

# Price
label5 = tk.Label(root, text="Price")
label5.pack()
entry5 = tk.Entry(root)
entry5.pack()


def send_data():
    var_type = entry.get()
    var_name = entry2.get()
    var_brand = entry3.get()
    var_color = entry4.get()
    var_price = entry5.get()
    
    # Ensure string values are enclosed in single quotes
    sql_query = "INSERT INTO dbo.War VALUES ('{}','{}','{}','{}','{}')".format(var_type, var_name, var_brand, var_color, var_price)
    
    print(sql_query)
    
    cursor.execute(sql_query)
    cursor.commit()
    
    popup = tk.Toplevel()
    popup_label = tk.Label(popup, text="Added")
    popup_label.pack()
# Send button
send_button = tk.Button(root, text="Send", command=send_data)
send_button.pack()


root.mainloop()




root.mainloop()

cursor.execute("SELECT * FROM dbo.War")

rows = cursor.fetchall()

for row in rows:
    print('Type:', row[0])
    print('Name:', row[1])
    print('Brand:', row[2])
    print('Color:', row[3])
    print('Price:', row[4])
    print('-----------------------')

cursor.close()
cnxn.close()

while True:
    with open('index.html') as file:
        template_content = file.read()
        template = Template(template_content)
        rendered_content = template.render(rows=rows)
    with open('rendered.html','w') as file:
        file.write(rendered_content)




