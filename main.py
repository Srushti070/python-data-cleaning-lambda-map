from sample_data import names, marks, emails
from data_cleaning import *

print("Original Data:")
print(names)
print(marks)
print(emails)

print("\nCleaned Data:")

cleaned_names = clean_names(names)
cleaned_marks = clean_marks(marks)
cleaned_emails = clean_emails(emails)

print("Names:", cleaned_names)
print("Marks:", cleaned_marks)
print("Emails:", cleaned_emails)

print("\nAfter Bonus Marks:")
print(add_bonus(cleaned_marks))


# -------------------- NEW TEST DATA --------------------
''' in this the number and string alphabet both are there
    we can clear that'''

prices = ['100','200','455','invalid','5774','sry']
print('Prices:',prices)
print("\nClean Prices:", clean_prices(prices))

test_names = ['123','abc','pqr','10000','xyz','23']
print('Names:',test_names)
print("\nValid Names:", validate_names(test_names))