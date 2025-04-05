from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def test_scores_service(url):
    options = Options()
    options.add_argument('--headless')  # run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(2)  # give page time to load

        score_element = driver.find_element("id", "score")
        score = int(score_element.text)
        return 1 <= score <= 1000
    except Exception as e:
        print(f"Test failed with exception: {e}")
        return False
    finally:
        driver.quit()

def main():
    test_result = test_scores_service("http://localhost:8777")
    if test_result:
        exit(0)
    else:
        exit(-1)

if __name__ == "__main__":
    main()
