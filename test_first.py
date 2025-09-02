import allure


@allure.title("Test Sum")
def test_sum():
    with allure.step("Check sum of digits"):
        assert 1 == 1, "Incorrect sum of digits"


# MIN HOUR DOM MON DOW
#MIN: 0–59
#HOUR: 0–23
#DOM: 1–31
#MON: 1–12 or Jan–Dec
#DOW: 0–7 or Sun–Sat (0 and 7 = Sun)
#H: random value

# 0 9,17 * * * (09:00 and 17:00 every day)
# H 0 * * * (00:17, 00:01)
