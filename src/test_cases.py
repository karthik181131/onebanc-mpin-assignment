from src.checker import evaluate_mpin

def run_tests():
    test_data = [
        # Format: (mpin, dob, spouse_dob, anniversary, expected_strength, expected_reasons)

        # Commonly used MPINs
        ("1234", "1998-01-02", "2000-12-30", "2020-10-10", "WEAK", ["COMMONLY_USED"]),
        ("1111", "1998-01-02", "2000-12-30", "2020-10-10", "WEAK", ["COMMONLY_USED"]),

        # Demographic: matches DOB (DDMM)
        ("0201", "1998-01-02", "2000-12-30", "2020-10-10", "WEAK", ["COMMONLY_USED","DEMOGRAPHIC_DOB_SELF"]),

        # Demographic: matches Spouse DOB (YYMMDD)
        ("001230", "1998-01-02", "2000-12-30", "2020-10-10", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),

        # Demographic: matches Anniversary (DDMMYYYY)
        ("10102020", "1998-01-02", "2000-12-30", "2020-10-10", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),

        # Combination of common + demographic
        ("0201", "1998-01-02", "0201-12-25", "2020-02-01", "WEAK", [
            "COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_ANNIVERSARY"
        ]),

        # 6-digit match from DOB (DDMMYY)
        ("020198", "1998-01-02", "1999-12-25", "2021-11-11", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),

        # STRONG MPINs
        ("849392", "1998-01-02", "1999-12-25", "2021-11-11", "STRONG", []),
        ("593482", "2000-05-05", "2001-11-15", "2020-07-20", "STRONG", []),
        ("432789", "1990-06-30", "1991-04-20", "2000-01-01", "STRONG", []),

        # More edge cases (DOB + Spouse DOB)
        ("2512", "1990-06-30", "1999-12-25", "2010-05-05", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("3099", "1999-03-09", "2002-11-11", "2011-06-06", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),

        # Matching full year only
        ("1998", "1998-01-02", "2000-12-30", "2020-10-10", "WEAK", ["COMMONLY_USED","DEMOGRAPHIC_DOB_SELF"]),

        # Match via MMDDYY (spouse DOB = 1999-12-30)
        ("123099", "1999-01-02", "1999-12-30", "2020-10-10", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),

        # All matching
        ("021298", "1998-12-02", "1998-12-02", "1998-12-02", "WEAK",
        ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]),


        # Test 17 – STRONG random 6-digit
        ("729384", "1990-01-01", "1991-02-02", "1992-03-03", "STRONG", []),

        # Test 18 – WEAK (spouse DOB: DDMM)
        ("1506", "2000-12-12", "2001-06-15", "2010-10-10", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),

        # Test 19 – WEAK (anniversary: MMYY)
        ("1020", "1998-05-04", "1996-06-06", "2020-10-15", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),

        # Test 20 – STRONG 4-digit not matching any pattern
        ("6482", "1989-03-09", "1990-07-07", "2001-09-09", "STRONG", []),

        # Test 21 – 6-digit from spouse YYMMDD
        ("991225", "1990-01-01", "1999-12-25", "2010-10-10", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),

        # Test 22 – STRONG 6-digit unrelated
        ("736291", "1995-05-05", "1996-06-06", "2000-07-07", "STRONG", []),

        # Test 23 – Match on anniversary DDMMYY
        ("200711", "1990-01-01", "1995-05-05", "2011-07-20", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),

        # Test 24 – Match DOB MMDD
        ("0102", "1998-01-02", "1990-09-09", "2010-10-10", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),

        # Test 25 – Match spouse YYMM
        ("9912", "1995-05-05", "1999-12-20", "2000-01-01", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"])
    ]

    passed = 0
    for i, (mpin, dob, spouse_dob, anniv, expected_strength, expected_reasons) in enumerate(test_data, 1):
        result = evaluate_mpin(mpin, dob, spouse_dob, anniv)
        if result["strength"] == expected_strength and set(result["reasons"]) == set(expected_reasons):
            print(f"✅ Test {i} passed")
            passed += 1
        else:
            print(f"❌ Test {i} failed")
            print(f"   Input: {mpin}, {dob}, {spouse_dob}, {anniv}")
            print(f"   Expected: {expected_strength}, {expected_reasons}")
            print(f"   Got     : {result['strength']}, {result['reasons']}")

    print(f"\n✅ Passed {passed}/{len(test_data)} tests.")

if __name__ == "__main__":
    run_tests()
