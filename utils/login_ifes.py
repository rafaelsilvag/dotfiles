import mechanize

url = "http://192.168.48.1:81"

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [
    (
        "user-agent",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423",
    )
]


try:
    browser.open(url)
    browser.select_form(nr=0)
    # SIAPE Number
    browser.form["UserUsername"] = "........"
    # Password
    browser.form["UserPassword"] = "........"
    browser.find_control("termo").items[0].selected = True
    browser.submit()
except Exception as ex:
    print(f"Error: {ex}")
