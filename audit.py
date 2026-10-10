from playwright.sync_api import sync_playwright

URL = "https://www.etsmtl.ca"

with sync_playwright() as p:
    devices = {
        "mobile": p.devices["iPhone 13"],
        "desktop": {"viewport": {"width": 1440, "height": 900}},
    }

    browser = p.chromium.launch()
    for device_name, options in devices.items():
        context = browser.new_context(**options)
        page = context.new_page()
        page.goto(URL)
        page.screenshot(path=f"{device_name}.png", full_page=True)

        content_width = page.evaluate("document.documentElement.scrollWidth")
        viewport_width = page.evaluate("window.innerWidth")
        print(device_name, content_width, viewport_width)

        if content_width > viewport_width:
            print(f"{device_name}: page overflows by {content_width - viewport_width} px")
        else:
            print(f"{device_name}: OK")
        context.close()
    browser.close()
    