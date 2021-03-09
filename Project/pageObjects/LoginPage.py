class LoginPage():
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    #link_logout_linkText = "welcome"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        userbox = self.driver.find_element_by_id(self.textbox_username_id)
        userbox.clear()
        userbox.send_keys(username)

    def setPassword(self, password):
        passwordBox = self.driver.find_element_by_id(self.textbox_password_id)
        passwordBox.clear()
        passwordBox.send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
