from pages.base_page import BasePage


class Open_New_Account(BasePage):
    OPEN_NEW_ACCOUNT_LINK = "//a[normalize-space()='Open New Account']"
    SAVINGS_OR_CHECKING = "#type"
    OPEN_NEW_ACCOUNT_BUTTON = "//input[@value='Open New Account']"
    NEW_ACCOUNT_ID = "//a[@id='newAccountId']"
    CONGRATULATIONS_MESSAGE = "//p[normalize-space()='Congratulations, your account is now open.']"
    PRINTED_ACCOUNT_NUMBER = '//*[@id="accountId"]'
    BALANCE = '//*[@id="balance"]'
    AVAILABLE_BALANCE = '//*[@id="availableBalance"]'
    GO_BUTTON = '//input[@value="Go"]'
    DATE_OF_TRANSACTION = '//*[@id="transactionTable"]/tbody/tr/td[1]'
    FUNDS_TRANSFER_RECEIVED = '//*[@id="transactionTable"]/tbody/tr/td[2]/a'
    TRANSACTION_ID = '//*[@id="rightPanel"]//tr[1]/td[2]'
    DATE_OF_TRANSACTION_ON_TRANSACTION_DETAILS_PAGE = '//*[@id="rightPanel"]//tr[2]/td[2]'
    DESCRIPTION = '//*[@id="rightPanel"]//tr[3]/td[2]'
    TYPE = '//*[@id="rightPanel"]//tr[4]/td[2]'
    AMOUNT = '//*[@id="rightPanel"]//tr[5]/td[2]'

    def click_open_new_account(self):
        self.click(self.OPEN_NEW_ACCOUNT_LINK)

    def select_account_type(self, value):
        self.page.select_option(self.SAVINGS_OR_CHECKING, value=value)

        if value == "1":
            print("Savings account selected")
        elif value == "0":
            print("Checkin account selected")

    def click_open_account_button(self):
        self.click(self.OPEN_NEW_ACCOUNT_BUTTON)

    def get_newly_added_account_number(self):
        self.page.wait_for_selector(self.NEW_ACCOUNT_ID, state="attached")
        account_number = self.page.locator(self.NEW_ACCOUNT_ID).text_content().strip()
        print("Account Number:", account_number)
        return account_number

    def click_newly_added_account_number(self):
        self.page.wait_for_selector(self.NEW_ACCOUNT_ID, state="attached").click()

    def verify_congratulation_message(self):
        self.page.wait_for_selector(self.CONGRATULATIONS_MESSAGE, state="attached").text_content().strip()
        message = self.page.locator(self.CONGRATULATIONS_MESSAGE).text_content().strip()
        print("Message printed:", message)
        return message

    def verify_printed_account_number(self):
        clicked_account_number = self.page.wait_for_selector(self.PRINTED_ACCOUNT_NUMBER).text_content().strip()
        print(clicked_account_number)
        return clicked_account_number

    def verify_balance(self):
        balance = self.page.wait_for_selector(self.BALANCE).text_content().strip()
        print("balance is: ", balance)
        return balance

    def verify_available_balance(self):
        available_balance = self.page.wait_for_selector(self.AVAILABLE_BALANCE).text_content().strip()
        print("Available balance is:", available_balance)
        return available_balance

    def handle_month(self, month):
        if month.upper() == "ALL":
            months = self.page.locator("#month option").all_text_contents()
            for m in months:
                self.page.select_option("#month", label=m)
        else:
            self.page.select_option("#month", label=month)

    def transactionType(self, transactions):
        if transactions.upper() == "ALL":
            transaction = self.page.locator("#transactionType option").all_text_contents()
            for t in transaction:
                self.page.select_option("#transactionType", label=t)
        else:
            self.page.select_option("#transactionType", label=transactions)

    def go_button(self):
        self.click(self.GO_BUTTON)

    def date_of_transaction(self):
        dot = self.page.wait_for_selector(self.DATE_OF_TRANSACTION, state="attached").text_content().strip()
        print("Date of transaction is: ", dot)

    def funds_transfer_received_link(self):
        self.click(self.FUNDS_TRANSFER_RECEIVED)

    def transaction_id(self):
        id_transaction = self.page.wait_for_selector(self.TRANSACTION_ID, state="attached").text_content().strip()
        print("Transaction ID is :", id_transaction)

    def date_of_transaction_on_transaction_page(self):
        transaction_date = self.page.wait_for_selector(self.DATE_OF_TRANSACTION_ON_TRANSACTION_DETAILS_PAGE,
                                                       state="attached").text_content().strip()
        print("Date of transaction is:", transaction_date)

    def verify_description(self):
        description_details = self.page.wait_for_selector(self.DESCRIPTION, state="attached").text_content().strip()
        print("Description is: ", description_details)

    def verify_type_of_transaction(self):
        type_of_transaction = self.page.wait_for_selector(self.TYPE, state="attached").text_content().strip()
        print("Type is: ", type_of_transaction)

    def verify_amount(self):
        amount = self.page.wait_for_selector(self.AMOUNT, state="attached").text_content().strip()
        print("Amount is:", amount)
