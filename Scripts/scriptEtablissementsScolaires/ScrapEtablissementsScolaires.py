from selenium import webdriverfrom
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

import pandas as pd
import time 

driver = webdriver.Chrome('chromedriver')
#This line creates a ChromeOptions object, which allows you to customize the behavior of the ChromeDriver.
options=webdriver.ChromeOptions()

#This is useful for running automated tests or performing web scraping tasks without displaying the browser window.
#options.add_argument('-headless')

#disable chrome contenairiation in order to modify options
options.add_argument('-no-sandbox')

#disable shared memory space in Chrome cause might be troublesome in headless mode
options.add_argument('-disable-dev-shm-usage')

#ignores SSL certificate errors
options.add_argument('--ignore-certificate-errors')

#pass in incognito mode
options.addArguments("incognito");

#pass arguments
driver = webdriver.Chrome('chromedriver',options=options)

#Navigate to page
driver.get('https://www.enseignement-prive.info/annuaire-enseignement-prive/ile-de-france')
# print('source code\n' *10 + driver.page_source + 'source code\n' *10)
# # Get etablissements source code
# HtmlEtablissements = driver.page_source

# # Print the HTML content
# print(HtmlEtablissements)

#Sandbox
# AccessEtablissement =  driver.find_element(By.TAG_NAME,'figure')
# #Navigte to etablissement page
# AccessEtablissement.click()
# NomEtablissementScolaireNminus4 = driver.find_element(By.CLASS_NAME,'wrap')
# ParentNomEtablissementScolaire = driver.find_element(By.CLASS_NAME,'description')
# NomEtablissementScolaire = ParentNomEtablissementScolaire.find_element(By.TAG_NAME,'h1').text
# print(NomEtablissementScolaire)
# print(driver.current_url)
# driver.back()
# print(driver.current_url)
#print source code
#

# AccesEtablissementsNminus3 = driver.find_elements(By.CSS_SELECTOR,'article.isClient:nth-child(1)')

# AccesEtablissementsNminus2 =  driver.find_elements(By.CSS_SELECTOR,'header:nth-child(1)')

# AccesEtablissementsNminus1 =  driver.find_elements(By.CSS_SELECTOR,'strong:nth-child(3)')

Etablissements =  driver.find_elements(By.CSS_SELECTOR,"body > section > div.wrap > section > div.clearfix.establishments-list > article:nth-child(n) > header > strong > a")
articles=[]                                            
i=1                                                    
#Adresse CSS selector
AdresseSelector = 'body > section > div.wrap > section > article > header > div.coords > p.address'


for Etablissement in Etablissements :
    #Next rank if i divisible by 11
    if i%11 == 0:
        i+=1
        print(driver.current_url)
        #Indent url etablissement CSS selector
        IndentedEtablissementLinkSelector = f"body > section > div.wrap > section > div.clearfix.establishments-list > article:nth-child({i}) > header > strong > a"   
        #Wait for UrlEtablissementContainer to be available
        WebDriverWait(driver,60).until(
             EC.element_to_be_visible(By.CSS_SELECTOR, IndentedEtablissementLinkSelector)
        )
        #find url container                
        UrlEtablissementContainer = driver.find_element(By.CSS_SELECTOR,IndentedEtablissementLinkSelector)                             
        #retrieve  NomEtablissementScolaire
        NomEtablissementScolaire = UrlEtablissementContainer.text
        #Get url
        url = f'https://www.enseignement-prive.info/annuaire-enseignement-prive/ile-de-france{UrlEtablissementContainer.get_attribute("href")}'
        print(url)
        #Navigate to fiche etablissement
        #driver.get(f)












for Etablissement in Etablissements :
    #Next rank if i divisible by 11
    if i%11 == 0:
        i+=1
    try:
        print(driver.current_url)
        #Indent url etablissement CSS selector
        IndentedEtablissementLinkSelector = f"body > section > div.wrap > section > div.clearfix.establishments-list > article:nth-child({i}) > header > strong > a"   
        #Wait
        time.sleep(10)
        #find url container                
        LinkEtablissementContainer = driver.find_element(By.CSS_SELECTOR,IndentedEtablissementLinkSelector)                             
        #retrieve  NomEtablissementScolaire
        NomEtablissementScolaire = LinkEtablissementContainer.text
        #Wait for fiche etablissement link to be available
        WebDriverWait(driver,60).until(
            EC.element_to_be_clickable(LinkEtablissementContainer)
        )
        #Navigate to fiche etablissement
        LinkEtablissementContainer.click()
    # If ElementClickInterceptedException occures
    except ElementClickInterceptedException as e:
        #
        print("ElementClickInterceptedException:", e.args)
        #Indent url etablissement CSS selector with different CSS Selector
        IndentedEtablissementLinkSelector =  f"body > section > div.wrap > section > div.clearfix.establishments-list > article:nth-child({i}) > header > li > strong > a" 
        #find url container  
        LinkEtablissementContainer = driver.find_element(By.CSS_SELECTOR,IndentedEtablissementLinkSelector) 
        #retrieve  NomEtablissementScolaire
        NomEtablissementScolaire = LinkEtablissementContainer.text
        #Wait for fiche etablissement link to be available
        WebDriverWait(driver,60).until(
            EC.element_to_be_clickable(LinkEtablissementContainer)
        )
        #Navigate to fiche etablissement
        LinkEtablissementContainer.click()
    print(driver.current_url)
    print(i)
    driver.back()
    i+=1
    

    #Loading
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located(By.CSS_SELECTOR, AdresseSelector)
    )
    #Retrieve Adresse
    AdresseEtablissementScolaire = driver.find_element(By.CSS_SELECTOR,AdresseSelector).text
    #Add new values
    articles.append([NomEtablissementScolaire, AdresseEtablissementScolaire])
    #Return to etablissement
    driver.back()
    #Loading
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.CSS_SELECTOR,IndentedEtablissementLinkSelector)
    )
    #Next Rank
    i+=1
print(i)
print(articles)






# df = pd.DataFrame(articles, columns=[NomEtablissementScolaire, AdresseEtablissementScolaire])

# print(df.iloc[0][0])

# #     AccesTelephone = driver.find_element(By.XPATH,'/html/body/section/div[3]/aside/header/div[2]/div/span')
# #     #
# #     AccesTelephone.click()
# #     #
# #     time.sleep(2)
# #     #
# #     Telephone = driver.find_element(By.XPATH,'/html/body/section/div[3]/aside/header/div[2]/div/a').text
# #     #
# #     articles.append([NomEtablissementScolaire, AdresseEtablissementScolaire, Telephone])
#     driver.back()

# df = pd.DataFrame(articles,columns=['NomEtablissementScolaire', 'AdresseEtablissementScolaire', 'Telephone'])

# print(df.iloc[0][0])


