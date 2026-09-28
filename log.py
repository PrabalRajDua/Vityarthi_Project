def write_log(message):
    f = open("app.log", "a")
    f.write(message + "\n")
    f.close()
