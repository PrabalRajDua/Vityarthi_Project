from log import write_log
ADMISSION = 0
NAME = 1
BLOOD = 2
AGE = 3
donors = []
def add_donor(admission_no, name, blood_type, age):
    for d in donors:
        if d[ADMISSION] == admission_no:
            return False
    donors.append([admission_no, name, blood_type, age])
    write_log("Added donor " + admission_no)
    return True
def search_donors(position, value):
    found = []
    for d in donors:
        if str(d[position]).lower() == value.strip().lower():
            found.append(d)
    return found
def update_donors(position, old_value, new_value):
    count = 0
    for d in donors:
        if str(d[position]).lower() == old_value.strip().lower():
            d[position] = new_value
            count = count + 1
    write_log("Updated " + str(count) + " donor(s)")
    return count
def delete_donors(position, value):
    removed = []
    for d in donors[:]:
        if str(d[position]).lower() == value.strip().lower():
            donors.remove(d)
            removed.append(d)
    write_log("Deleted " + str(len(removed)) + " donor(s)")
    return removed
