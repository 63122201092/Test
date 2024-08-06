from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have the chromedriver installed and added to your PATH

# 1. File Upload
def test_file_upload():
    # Open the page
    driver.get("https://www.autospinn.com/2023/08/bike-review-honda-giorno-125-132331")  # Replace with the actual URL
    
    # Locate the file input element and upload the file
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys("/path/to/your/file.txt")  # Replace with the actual file path
    
    # Click the upload button
    upload_button = driver.find_element(By.ID, "file-submit")
    upload_button.click()
    
    # Wait for the upload to complete
    time.sleep(5)  # You can use WebDriverWait for a better approach
    
    # Assert the file upload success
    success_message = driver.find_element(By.ID, "uploaded-files").text
    assert "file.txt" in success_message
    print("File upload test passed.")

# 2. Multiple Windows
def test_multiple_windows():
    # Open the page
    driver.get("https://www.autospinn.com/2023/08/bike-review-honda-giorno-125-132331")  # Replace with the actual URL
    
    # Click the link that opens a new window
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    
    # Get the window handles
    original_window = driver.current_window_handle
    windows = driver.window_handles
    
    # Switch to the new window
    for window in windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    
    # Perform actions in the new window
    time.sleep(2)  # You can use WebDriverWait for a better approach
    assert "New Window" in driver.title
    driver.close()
    
    # Switch back to the original window
    driver.switch_to.window(original_window)
    print("Multiple windows test passed.")

# 3. Sortable Data Tables
def test_sortable_data_tables():
    # Open the page
    driver.get("https://www.autospinn.com/2023/08/bike-review-honda-giorno-125-132331")  # Replace with the actual URL
    
    # Locate the table headers and click to sort
    header = driver.find_element(By.XPATH, "//table[@id='table1']/thead/tr/th[1]")
    header.click()
    
    # Wait for sorting to complete
    time.sleep(2)  # You can use WebDriverWait for a better approach
    
    # Verify the table is sorted
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td[1]")
    data = [row.text for row in rows]
    assert data == sorted(data), "Table is not sorted correctly."
    print("Sortable data tables test passed.")

# Run the tests
test_file_upload()
test_multiple_windows()
test_sortable_data_tables()

# Close the WebDriver
driver.quit()
