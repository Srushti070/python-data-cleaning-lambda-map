"""
Data Cleaning using lambda and map
"""

# Clean names
def clean_names(names):
    return list(map(lambda x: x.strip().capitalize(), names))


# Clean marks
def clean_marks(marks):
    return list(map(lambda x: int(x.strip()), marks))


# Clean emails
def clean_emails(emails):
    return list(map(lambda x: x.strip().lower(), emails))


# Add bonus
def add_bonus(marks):
    return list(map(lambda x: x + 5, marks))


# -------------------- NEW ADDITIONS --------------------

def clean_prices(prices):
    return list(map(lambda x: int(x) if x.isdigit() else 0, prices))


def validate_names(names):
    return list(map(lambda x: x if x.isalpha() else None, names))