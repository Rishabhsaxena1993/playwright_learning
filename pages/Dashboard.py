from pages.base_page import BasePage


class DashboardPage(BasePage):
    ACCOUNT_LINK = 'a[href^="activity.htm?id="]'
    ACCOUNT_NUMBER_TEXT_ON_ACCOUNT_DETAILS = '//*[@id="accountDetails"]/table/tbody/tr[1]/td[1]'
    ACTUAL_ACCOUNT_NUMBER = '//*[@id="accountId"]'

    def open_account_and_get_number(self):
        link = self.page.locator(self.ACCOUNT_LINK).first
        account_no = link.text_content().strip()
        print("Dashboard account number:", account_no)
        link.click()
        return account_no

    def get_account_number_from_details(self):
        account_no = self.page.text_content(self.ACTUAL_ACCOUNT_NUMBER).strip()
        print("Account details page number:", account_no)
        return account_no
