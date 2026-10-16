hw = int(input("Enter the homework time in minutes:"))

if hw > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no):")
if free_time == "Yes" or "yes":
    print("Reminder:Pick a hobby for your free time!")



print("==================== DAILY PLAN ==================")
print("Hmework minutes:",hw)
print("Plan:",plan)
print("Freetime:",free_time)