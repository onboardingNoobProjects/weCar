

class Logins:
    login_path = 'localhost:8000/accounts/login/'
    login_url = 'http://localhost:8000/accounts/login/'
    login_username = '//*[@id="username"]'
    login_password = '//*[@id="password"]'
    username = 'admin'
    password = 'pass123'

class Logouts:
    logout_bt_path = '//*[@id="topNavBar"]/ul[2]/li/a'

class Details:
    detailsURL = 'http://localhost:8000/wecar/1'
    indexURL = 'http://localhost:8000/wecar/'
    imageElement = '/html/body/img'
    titleElement = '/html/body/h1'
    priceElement = '/html/body/h3'
    tippingPoint = 'Tipping point:'
    expiryDate = 'Expiry date:'
    descriptionElement = '/html/body/div'

class Register:
    registerURL = 'http://localhost:8000/wecar/register/'
    loginURL = 'http://localhost:8000/accounts/login/'
    usernameField = '//*[@id="id_username"]'
    emailField = '//*[@id="id_email"]'
    passwordField = '//*[@id="id_password"]'
    submitBtn = '/html/body/form/div[4]/div/button'

class AddDeals_vars:
    addDeal_url = 'http://localhost:8000/wecar/add'
    addDeal_labels = ['Title:','Details:','RRP:','Price:','TippingPoint:','Expiry:','Pic:']
    addDeal_title = 'BMW i3'
    addDeal_details = 'Great Green car helping the enviorment'
    addDeal_rrp = '£35000'
    addDeal_price = '£40000'
    addDeal_tippingPoint = '100'
    addDeal_expiry = '2020-01-01 00:10:00'
    addDeal_pic = 'http://trotters-van-hire.co.uk/wp-content/uploads/2016/11/DelBoyVan.jpg'


    addDeal_title_xpath = '//*[@id="id_title"]'
    addDeal_details_xpath = '//*[@id="id_details"]'
    addDeal_rrp_xpath = '//*[@id="id_RRP"]'
    addDeal_price_xpath = '//*[@id="id_price"]'
    addDeal_tippingPoint_xpath = '//*[@id="id_tippingPoint"]'
    addDeal_expiry_xpath = '//*[@id="id_expiry"]'
    addDeal_pic_xpath = '//*[@id="id_pic"]'
    addDeal_btSubmit_xpath = '/html/body/form/div[8]/div/button'

class ToolBar:
    carName = 'tesla'
    btDeals = '//*[@id="topNavBar"]/ul[1]/li[1]/a'
    btweCar = '/html/body/nav/div/div[1]/a'
    txtSearch = '//*[@id="topNavBar"]/form/div/input'
    btSearch = '//*[@id="topNavBar"]/form/button'
    searched_url = 'http://localhost:8000/wecar/?q='

class Index_vars:
    index_url = 'http://localhost:8000/wecar/'
