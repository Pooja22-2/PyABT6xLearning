
expected_title=(input("Enter expected title:\n")).strip()
actual_title=(input("Enter actual title:\n")).strip()

if expected_title.lower()==actual_title.strip().lower():
    print("Test Case Passed: expected_title Matches")
else:
    print("Test Case Failed: actual_title not matched")