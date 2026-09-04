userName = input("Enter user name: ")
role = input("Enter role (Student/Faculty/Admin): ")
idCard = input("Is the ID card valid? (yes/no): ").lower()
restrictedArea = input("Is this a restricted area? (yes/no): ").lower()

authorizedRoles = ["Student", "Faculty", "Admin"]

idValid = idCard == "yes"
authorizedRole = role in authorizedRoles
isRestricted = restrictedArea == "yes"

if authorizedRole and idValid:
    status = "GRANTED"

    if role == "Admin":
        accessLevel = "Full Access"
    elif role == "Faculty":
        accessLevel = "Faculty Access"
    else:
        accessLevel = "Student Access"

else:
    status = "DENIED"
    accessLevel = "No Access"

print("\n---------- SMART ACCESS DASHBOARD ----------")
print(f"User Name           : {userName}")
print(f"Role                : {role}")
print("ID Card             :", "VALID" if idValid else "INVALID")
print("Authorized Role     :", "YES" if authorizedRole else "NO")
print("ID Card Valid       :", "YES" if idValid else "NO")
print("Restricted Area     :", "YES" if isRestricted else "NO")
print(f"Access Level        : {accessLevel}")
print(f"ACCESS STATUS       : {status}")