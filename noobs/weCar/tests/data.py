

class Logins:
    login_path = 'localhost:8000/wecar'
    login_url = 'http://localhost:8000/wecar/'
    login_username = '//*[@id="username"]'
    login_password = '//*[@id="password"]'
    username = 'admin'
    password = 'pass123'

class Logouts:
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

class AddDeals_vars:
    addDeal_url = 'localhost:8000/wecar/add'
    addDeal_labels = ['Title:','Details:','RRP:','Price:','TippingPoint:','Expiry:','Pic:']


class ToolBar:
        carName = 'tesla'
        btDeals = '//*[@id="topNavBar"]/ul[1]/li[1]/a'
        btweCar = '/html/body/nav/div/div[1]/a'
        txtSearch = '//*[@id="topNavBar"]/form/div/input'
        btSearch = '//*[@id="topNavBar"]/form/button'
        searched_url = 'http://localhost:8000/wecar/?q='
