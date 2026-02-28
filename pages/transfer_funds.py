from pages.base_page import BasePage


class Transfer_Funds(BasePage):
    TRANSFER_FUNDS = "//a[@href='transfer.htm']"
    ENTER_AMOUNT_TO_TRANSFER = "//input[@id='amount']"
    CHOOSE_FROM_ACCOUNT = "#fromAccountId"
    CHOOSE_TO_ACCOUNT = "#toAccountId"
    FROM_ACCOUNT = '//*[@id="fromAccountId"]'
    TO_ACCOUNT = '//*[@id="toAccountId"]'
    TRANSFER_BUTTON = '//*[@id="transferForm"]/div[2]/input'
    TRANSFER_COMPLETE_MESSAGE = "#showResult > h1"
    AMOUNT_TRANSFERRED_PRINTED_IN_MESSAGE = "#amountResult"
    PRINT_FROM_ACCOUNT = "#fromAccountIdResult"
    PRINT_TO_AMOUNT = "#toAccountIdResult"

    def click_on_Transfer_Funds(self):
        self.click(self.TRANSFER_FUNDS)

    def enter_amount(self, value):
        self.page.fill(self.ENTER_AMOUNT_TO_TRANSFER, value)

    def choose_from_accounts(self, value):
        self.page.select_option(self.CHOOSE_FROM_ACCOUNT, value=value)

    def choose_to_accounts(self, value):
        self.page.select_option(self.CHOOSE_TO_ACCOUNT, value=value)

    def click_on_transfer_button(self):
        self.click(self.TRANSFER_BUTTON)

    def verify_transfer_complete_message(self):
        message_transfer_scucess = self.page.wait_for_selector(self.TRANSFER_COMPLETE_MESSAGE).text_content().strip()
        print("Message =", message_transfer_scucess)
        return message_transfer_scucess

    def verify_amount_transffered(self):
        verified_amount = self.page.wait_for_selector(self.AMOUNT_TRANSFERRED_PRINTED_IN_MESSAGE,
                                                      state="attached").text_content().strip()
        print("Amount_transffer is", verified_amount)
        return verified_amount

    def verify_from_account(self):
        transfered_from_account = self.page.wait_for_selector(self.PRINT_FROM_ACCOUNT, state="attached").text_content().strip()
        print("Transfered from account", transfered_from_account)

    def verify_to_account(self):
        transfered_to_account = self.page.wait_for_selector(self.PRINT_TO_AMOUNT, state="attached").text_content().strip()
        print("Transfered to account", transfered_to_account)

    def select_first_from_account(self):
        self.page.select_option("#fromAccountId", index=0)

    def select_second_to_account(self):
        self.page.select_option("#toAccountId", index=1)