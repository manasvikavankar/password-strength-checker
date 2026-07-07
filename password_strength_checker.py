while True:

    password = input("\nEnter your password (or type 'exit' to quit): ")

    if password.lower() == "exit":
        print("\nThank you for using Password Strength Checker! 👋")
        print("Stay safe and use strong passwords.")
        break

    print("\nChecking password...\n")
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    score = 0

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for ch in password:

        if ch.islower():
            has_lower = True

        if ch.isupper():
            has_upper = True

        if ch.isdigit():
            has_digit = True

        if ch in special_characters:
            has_special = True
            
        
    if has_lower:
        score += 1

    if has_upper:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if len(password) >= 8:
        score += 1
            
    print("\n" + "=" * 40)
    print("      PASSWORD ANALYSIS")
    print("=" * 40)
    max_score = 5
    print(f"Score : {score}/{max_score}")
    
    if score <= 2:
        print("Strength : 🔴 Weak")

    elif score == 3 or score == 4:
        print("Strength : 🟡 Medium")

    else:
        print("Strength : 🟢 Strong 💪")
        print("✅ Your password meets all the recommended security requirements.")


    if not has_lower:
        print("❌ Add at least one lowercase letter.")

    if not has_upper:
        print("❌ Add at least one uppercase letter.")

    if not has_digit:
        print("❌ Add at least one number.")

    if not has_special:
        print("❌ Add at least one special character.")

    if len(password) < 8:
        print("❌ Password should be at least 8 characters long.")

            
