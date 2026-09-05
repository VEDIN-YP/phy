def check_password(password):

    score = 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+[]{};:',.<>?/"

    # Check length
    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    # Check every character
    for character in password:

        if character.isupper():
            has_upper = True

        elif character.islower():
            has_lower = True

        elif character.isdigit():
            has_digit = True

        elif character in special_characters:
            has_special = True

    # Add score for character types
    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    # Display results
    print("\n--- PASSWORD ANALYSIS ---")

    print("Length:", len(password))
    print("Uppercase:", has_upper)
    print("Lowercase:", has_lower)
    print("Number:", has_digit)
    print("Special character:", has_special)

    print("\nScore:", score, "/ 6")

    if score <= 2:
        print("Strength: WEAK ❌")

    elif score <= 4:
        print("Strength: MEDIUM ⚠️")

    else:
        print("Strength: STRONG 🔥")


password = input("Enter your password: ")

check_password(password)
