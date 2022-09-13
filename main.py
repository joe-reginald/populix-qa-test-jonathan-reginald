import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopulixTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        input_email = driver.find_element(By.ID, "input_email")
        input_password = driver.find_element(By.ID, "input_password")

        input_email.send_keys("jivet.712@gmail.com")
        input_password.send_keys("cumabuattest")
        input_password.send_keys(Keys.ENTER)

        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'dashboard'), "Studi"
            )
        )

    def test_login_fb(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        login_fb = driver.find_element(By.ID, "login_facebook")

        login_fb.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, 'facebook')
            )
        )
    
    def test_login_google(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        login_google = driver.find_element(By.ID, "login_google")

        login_google.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'CMgTXc')
            )
        )

    def test_register(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        btn_register = driver.find_element(By.ID, "btn_to-register")

        btn_register.click()

        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, 'app'), 'Daftar Akun Populix'
            )
        )
    
    def test_playstore(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        btn_playstore = driver.find_element(By.ID, "btn_to-playstore")

        btn_playstore.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'kOqhQd')
            )
        )

    def test_appstore(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        btn_appstore = driver.find_element(By.ID, "btn_to-appstore")

        btn_appstore.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'ac-gn-link-apple')
            )
        )

    def test_login_wrong_email(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        input_email = driver.find_element(By.ID, "input_email")
        input_password = driver.find_element(By.ID, "input_password")

        input_email.send_keys("jivet.712@gmail")
        input_password.send_keys("cumabuattest")
        input_password.send_keys(Keys.ENTER)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, 'input_email-helper-text')
            )
        )
    
    def test_login_wrong_pass(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        self.assertIn("Populix", driver.title)
        input_email = driver.find_element(By.ID, "input_email")
        input_password = driver.find_element(By.ID, "input_password")

        input_email.send_keys("jivet.712@gmail.com")
        input_password.send_keys("cumabuattest1")
        input_password.send_keys(Keys.ENTER)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, 'input_password-helper-text')
            )
        )
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()