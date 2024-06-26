import pytest
from playwright.sync_api import sync_playwright
from pages.google_search_page import GoogleSearchPage

@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # ヘッドレスモードをオフに
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_google_search_ptw(setup):
    page = setup
    google_search_page = GoogleSearchPage(page)
    google_search_page.load()
    try:
        google_search_page.search("PTW")
        results = google_search_page.get_results()
        assert any("PTW" in result.inner_text() for result in results)
    except Exception as e:
        page.screenshot(path="error_screenshot.png")  # エラー時にスクリーンショットを撮る
        raise e
