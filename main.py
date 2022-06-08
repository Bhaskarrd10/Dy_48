from  selenium import webdriver

chrome_driver_path = "/Users/bhaskarreddy/Web/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/")

driver.close()
driver.quit()