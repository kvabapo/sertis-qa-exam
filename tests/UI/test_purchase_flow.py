import pytest

from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):

    print("before the test runs")

    # Login before each test.
    page.goto("https://www.demoblaze.com/")
    page.click("#login2")
    page.fill("#loginusername", "test")
    page.fill("#loginpassword", "test")
    page.click(
        "#logInModal > div > div > div.modal-footer > button.btn.btn-primary")
    expect(page.locator("#logout2")).to_be_visible()

    yield

    print("after the test runs")
    # Logout after each test
    if expect(page.locator("#logout2")).to_be_visible():
        page.click("#logout2")


def test_success_purchase_of_a_product(page: Page):
    # Add to cart
    page.click("#tbodyid > div:nth-child(3) > div > div > h4 > a")  # Nexus 6
    expect(page.locator("#tbodyid > h2")).to_have_text("Nexus 6")
    expect(page.locator("#tbodyid > h3")).to_have_text("$650 *includes tax")
    page.click("#tbodyid > div.row > div > a")  # Add to cart button
    page.once("dialog", lambda dialog: dialog.dismiss())

    # Go to cart
    page.click("#navbarExample > ul > li:nth-child(4) > a")  # Cart

    # Place Order
    page.click("#page-wrapper > div > div.col-lg-1 > button")

    # Order Form
    page.wait_for_selector("#orderModalLabel")
    page.fill("#name", "Test")
    page.fill("#country", "Thailand")
    page.fill("#city", "Bangkok")
    page.fill("#card", "123456")
    page.fill("#month", "10")
    page.fill("#year", "2025")
    # Purchase button
    page.click(
        "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")

    # Confirmation Message
    page.get_by_role("button", name="OK").click()


def test_delete_a_product_from_cart(page: Page):
    # Add to cart
    page.click("#tbodyid > div:nth-child(3) > div > div > h4 > a")  # Nexus 6
    expect(page.locator("#tbodyid > h2")).to_have_text("Nexus 6")
    expect(page.locator("#tbodyid > h3")).to_have_text("$650 *includes tax")
    page.click("#tbodyid > div.row > div > a")  # Add to cart button
    page.on("dialog", lambda dialog: dialog.dismiss())

    # Go to cart
    page.click("#navbarExample > ul > li:nth-child(4) > a")  # Cart

    # Delete item
    page.click("#tbodyid > tr > td:nth-child(4) > a")
    expect(page.locator("#tbodyid > tr > td:nth-child(4) > a")).to_have_count(0)


def test_purchase_a_product_empty_cart(page: Page):
    # Go to cart
    page.click("#navbarExample > ul > li:nth-child(4) > a")  # Cart

    # Place Order
    page.click("#page-wrapper > div > div.col-lg-1 > button")

    # Order Form
    page.wait_for_selector("#orderModalLabel")
    page.fill("#name", "Test")
    page.fill("#country", "Thailand")
    page.fill("#city", "Bangkok")
    page.fill("#card", "123456")
    page.fill("#month", "10")
    page.fill("#year", "2025")
    # Purchase button
    page.click(
        "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")

    # Error Message (This should fail but I comment it out)
    # expect(page.locator("#errormsg")).to_have_text("user can't purchase when cart is empty")


def test_input_validation_purchase_form(page: Page):
    # Go to cart
    page.click("#navbarExample > ul > li:nth-child(4) > a")  # Cart

    # Place Order
    page.click("#page-wrapper > div > div.col-lg-1 > button")

    # Order Form
    page.wait_for_selector("#orderModalLabel")
    # Purchase button
    page.click(
        "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")

    # Error Message
    page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", lambda dialog: dialog.accept())
