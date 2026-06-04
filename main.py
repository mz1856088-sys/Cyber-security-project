from analyzer import analyze_password

print("=" * 40)
print("Password Strength Analyzer")
print("=" * 40)

password = input("Enter Password: ")

result = analyze_password(password)

print("\nResults")
print("-" * 40)
print(f"Strength : {result['strength']}")
print(f"Score    : {result['score']}/100")

if result["suggestions"]:
    print("\nSuggestions:")
    for item in result["suggestions"]:
        print(f"- {item}")