from playwright.sync_api import Page

class GoogleSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = "textarea[name='q']"  # 検索ボックスのロケーターを修正

    def load(self):
        self.page.goto("https://www.google.com")
        self.page.wait_for_load_state('load')  # ページが完全にロードされるまで待機
        self.page.wait_for_selector(self.search_box)  # 検索ボックスが表示されるまで待機

    def search(self, query: str):
        self.page.fill(self.search_box, query)
        self.page.press(self.search_box, 'Enter')  # 検索ボタンの代わりにEnterキーを押す

    def get_results(self):
        self.page.wait_for_selector('h3')
        return self.page.query_selector_all('h3')
