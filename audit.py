from playwright.sync_api import sync_playwright

URL = "https://www.etsmtl.ca"


with sync_playwright() as p:
    formats = {
        "mobile" : p.devices["iPhone 13"],
        "desktop" : {"viewport": {"width": 1440, "height": 900}}
    }

    browser = p.chromium.launch()
    for nom, options in formats.items():
        context = browser.new_context(**options)
        page = context.new_page()
        page.goto(URL)
        page.screenshot(path=f"{nom}.png", full_page= True)
        largeur_contenu = page.evaluate("document.documentElement.scrollWidth")
        largeur_ecran = page.evaluate("window.innerWidth")
        print(nom, largeur_contenu, largeur_ecran)
        if largeur_contenu > largeur_ecran:
            print(f"{nom}: la page deborde de {largeur_contenu-largeur_ecran} px")
        else: 
            print(f"{nom} : OK")
        context.close()
    browser.close()

