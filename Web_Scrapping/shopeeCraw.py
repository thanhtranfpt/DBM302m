import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def auto_login(driver, login_URL):
    user_name = ''
    password = ''

    driver.get(login_URL)

    driver.find_element(By.NAME, value='loginKey').send_keys(user_name)
    driver.find_element(By.NAME, value='password').send_keys(password)

    driver.find_element(By.CLASS_NAME, value='wyhvVD').click()

    time.sleep(200)

    return

def extract_comments(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    # Modify this function to extract and print comments from the soup
    comments = soup.find_all('div')
    print(page_source)
    # for comment in comments:
    #     print(comment.text.strip())
    #     print("---")


def process_product_page(product_url, driver):
    try:
        # Open the product URL
        driver.get(product_url)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        

        # Wait for the product page to load
        # time.sleep(2)  # Adjust the sleep time based on your page load time

        # Extract and print information from the product page

        # product_title = driver.find_element_by_css_selector('span.KmiQIK').text.strip()
        product_title = driver.find_element(By.CSS_SELECTOR, 'span.KmiQIK').text.strip()
        

        # product_price = driver.find_element_by_css_selector('div.pqTWkA').text.strip()
        product_price = driver.find_element(By.CSS_SELECTOR,'div.pqTWkA').text.strip()

        print(f"Product Title: {product_title}")
        print(f"Product Price: {product_price}")
        print("Comments:")

        # Extract comments on the product page
        comment_list = driver.find_element(By.CLASS_NAME, 'shopee-product-comment-list')
        print(comment_list)
        # extract_comments(driver.find_element(By.CSS_SELECTOR, 'div.shopee-product-comment-list').text.strip())

        # Check for pagination and extract comments from additional pages if available
        # next_page_button = driver.find_element_by_css_selector('button.next-page')
        # while next_page_button.is_enabled():
        #     next_page_button.click()

        #     # Wait for the next page to load
        #     time.sleep(2)  # Adjust the sleep time based on your page load time

        #     # Extract comments on the current page
        #     extract_comments(driver.page_source)

        #     # Find the next page button for the next iteration
        #     next_page_button = driver.find_element_by_css_selector('button.next-page')

    except Exception as e:
        print(f"An error occurred: {e}")


# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

driver = webdriver.Chrome()

# test auto login (write the account info in the function def)
# auto_login(driver, r"https://shopee.vn/buyer/login")
driver.implicitly_wait(2)

# Get the comment of product page
target_url = r'https://shopee.vn/a-i.448364971.22087131577'
process_product_page(target_url, driver)

