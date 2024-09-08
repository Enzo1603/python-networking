message = "test message"

filepath = "tcpmessage.txt"

with open(filepath, "w") as file:
    file.write(message)

print("Die Message wurde gespeichert.")
