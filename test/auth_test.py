import allure


@allure.id("28415")
@allure.title("Sign in with Google(clone)")
@allure.tag("web", "smoke")
@allure.story("External auth")
@allure.feature("Auth")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
def test_google_auth():
    with allure.step("Open main page"):
        pass
    with allure.step("Select Sign in with Google"):
        pass
    with allure.step("Sign in as userX"):
        with allure.step("Type login userx@email.com"):
            pass
    with allure.step("Type password 12345"):
        pass
    with allure.step("Click Sign in button"):
        pass
    with allure.step("Verify successful auth"):
        pass
    with allure.step("Verify user data updated from Google profile"):
        with allure.step("Name xuser"):
            pass
    with allure.step("Email: userx@email.com"):
        pass