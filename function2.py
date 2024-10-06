
def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

display_invoice("John Doe", 100.50, "2022-04-15")
display_invoice("vinaya", 100.50, "2022-05-15")