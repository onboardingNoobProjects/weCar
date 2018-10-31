

class logins:
    login_url = 'localhost:8000/wecar/add'
    login_username = '//*[@id="username"]'
    login_password = '//*[@id="password"]'


class logouts:
    logout_bt = '//*[@id="topNavBar"]/ul[2]/li/a'

class Details:
    detailsURL = 'localhost:8000/wecar/1'
    indexURL = 'http://localhost:8000/wecar/'
    imageElement = '/html/body/img'
    titleElement = '/html/body/h1'
    priceElement = '/html/body/h3'
    tippingPoint = 'Tipping point:'
    expiryDate = 'Expiry date:'
    descriptionElement = '/html/body/div'
