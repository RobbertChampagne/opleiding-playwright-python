# pytest tests/assignments/assignment11_network.py --headed

# Assignment 11 (Network) .json()

from playwright.sync_api import Page, expect

def test_assignment_11(page):
    
    page.goto("https://reqres.in/")
    
    # Wait for a specific network response
    with page.expect_response("**/api/users/2") as response_info:
        page.locator("li").filter(has_text="Single user").first.click()
    response = response_info.value
    
    # Parse the response body as JSON
    json_response = response.json()
    
    # Verify the JSON response
    assert json_response["data"]["first_name"] == 'Janet'
    assert json_response["data"]["last_name"] == 'Weaver'
    
