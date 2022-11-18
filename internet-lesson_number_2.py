yourName = input("Your name?\n")
old = int(input("How old are you?\n"))
age_stg = "child" if old < 13 else "teenager" if old < 18 else "man" if old < 50 else "older"
print(f"Hello {yourName}, you {age_stg}!")
