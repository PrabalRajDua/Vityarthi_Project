BLOOD_TYPES = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
def is_valid_admission(text):
    return text.strip().isalnum()
def is_valid_name(text):
    text = text.strip().replace(" ", "")
    return text.isalpha()
def is_valid_blood_type(text):
    return text.strip().upper() in BLOOD_TYPES
def is_valid_age(text):
    text = text.strip()
    if not text.isdigit():
        return False
    age = int(text)
    if age >= 18 and age <= 65:
        return True
    return False
