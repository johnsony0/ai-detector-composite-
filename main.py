from playwright.sync_api import sync_playwright
import argparse
import time
import re

'''
Check if a text is AI generated or assisted through multiple sources
such as ZeroGPT, GPTZero, Grammarly, Quillbot, Copyleaks
'''

'''def get_grammarly_prediction(text):
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.grammarly.com/ai-detector")

    text_area_xpath = ''
    page.fill(text_area_xpath,text)

    button_xpath = ''
    page.click(button_xpath)

    output_xpath = ''
    output_text = page.locator(output_xpath).inner_text()
    print(f'Grammarly predicts: {output_text}')

    browser.close()'''

def get_zerogpt_prediction(text,headless,timeout):
  try:
    print("trying zerogpt")
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=headless)
      page = browser.new_page()
      page.goto("https://www.zerogpt.com/")
      page.set_default_timeout(timeout)

      text_area_xpath = '//*[@id="textArea"]'
      page.fill(text_area_xpath,text)

      button_xpath = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]/button'
      page.click(button_xpath)


      output_xpath = '//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/span'
      output_text = page.locator(output_xpath).inner_text()
      percentage = re.search(r'\d+(\.\d+)?%', output_text)

      browser.close()

      return(f'ZeroGPT predicts: {percentage.group(0)} AI influence \n')
  except:
    return(f'ZeroGPT predicts: 0% AI influence \n')

def get_grammarly_prediction(text,headless,timeout):
  try:
    print("trying grammarly")
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=headless)
      page = browser.new_page()
      page.goto("https://www.grammarly.com/ai-detector")
      page.set_default_timeout(timeout)

      text_area_xpath = '//*[@id="form-ai-detector-desktop-AI Detector Text Input"]'
      page.fill(text_area_xpath,text)

      button_xpath = '//*[@id="form-ai-detector-desktop"]/div[2]/button/span'
      page.click(button_xpath)

      time.sleep(10)

      output_xpath = '//*[@id="sectionDynamic_1v5gbqFLDsXZ6weV2LjfjG"]/div[2]/div[1]/div/div[1]/h2/b'
      output_text = page.locator(output_xpath).inner_text()

      browser.close()
      return(f'Grammarly predicts: {output_text} of this text appears to be AI-generated \n')
  except:
    print("grammarly failed")
    return('')

def get_quillbot_prediction(text,headless,timeout):
  try:
    print("trying quillbot")
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=headless)
      page = browser.new_page()
      page.goto("https://quillbot.com/ai-content-detector")
      page.set_default_timeout(timeout)

      text_area = page.locator('//*[@id="editable"]')
      text_area.fill(text)
      text_area.fill(text)
      text_area.fill(text)

      text_area.press("Space")
      text_area.press("Backspace")

      button_xpath = '//*[@id="ai-container-tool"]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div/div/div/div[3]/div/span/button'
      page.click(button_xpath)
      page.click(button_xpath)

      time.sleep(5)
      output_xpath = '//*[@id="ai-container-tool"]/div[1]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div'
      output_text = page.locator(output_xpath).inner_text()

      browser.close()

      return(f'QuillBot predicts: {output_text} of text is likely AI-generated \n')
  except:
    print("quillbot failed")
    return('')

def get_hive_prediction(text,headless,timeout):
  try:
    print("trying hive")
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=headless)
      page = browser.new_page()
      page.goto("https://hivemoderation.com/ai-generated-content-detection")
      page.set_default_timeout(timeout)

      edit_button_xpath = '//*[@id="root"]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div/button'
      page.click(edit_button_xpath)

      text_area_xpath = '//*[@id="input_area_only"]/textarea'
      page.fill(text_area_xpath,text)

      button_xpath = '//*[@id="root"]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div/button'
      page.click(button_xpath)

      time.sleep(5)

      output_xpath = '//*[@id="root"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div/span'
      output_text = page.locator(output_xpath).inner_text()

      extra_xpath = '//*[@id="root"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/h6/span'
      extra_text = page.locator(extra_xpath).inner_text()

      browser.close()

      return(f'Hive predicts: {output_text} and {extra_text} \n')
  except:
    print("hive failed")
    return('')

def get_writer_prediction(text, headless, timeout):
  try:
    print("trying writer")
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=headless)
      page = browser.new_page()
      page.goto("https://writer.com/ai-content-detector/")
      page.set_default_timeout(timeout)

      text_area_xpath = '//html/body/div[1]/div[2]/div[2]/div[1]/form/div[2]/textarea'
      text_area = page.locator(text_area_xpath)
      text_area.fill(text)
      text_area.press("Space")
      text_area.press("Backspace")

      button_xpath = '//html/body/div[1]/div[2]/div[2]/div[1]/form/button'
      page.click(button_xpath)

      time.sleep(5)

      percent_xpath = '//*[@id="ai-percentage"]'
      percent_text = page.locator(percent_xpath).inner_text()

      output_xpath = '//html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]'
      output_text = page.locator(output_xpath).inner_text()

      browser.close()
      return(f'Writer predicts: {percent_text}% {output_text}')
  except:
    print("writer failed")
    return('')



def main():
  text = '''If the email text field element is not easily identifiable for some reason, 
  but the password text field element is, we can locate the text field element using the 
  fact that it is an “input” element “above” the password element. If the password text 
  field element is not easily identifiable for some reason, but the email text field element is, 
  we can locate the text field element using the fact that it is an “input” element “below” the 
  email element. If the email text field element is not easily identifiable for some reason, 
  but the password text field element is, we can locate the text field element using the 
  fact that it is an “input” element “above” the password element. If the password text 
  field element is not easily identifiable for some reason, but the email text field element is, 
  we can locate the text field element using the fact that it is an “input” element “below” the 
  email element.'''

  #text = input("Please enter the text you want to analyze: ")
  headless = True
  timeout = 30000

  text_length = len(text)
  text_words = len(text.split())
  
  output_results = ""

  output_results += get_zerogpt_prediction(text,headless,timeout)

  if (text_words > 40):
    output_results += get_grammarly_prediction(text,headless,timeout)
  else:
    print(f"not enough words for grammarly prediction: {text_words}/40 words")

  if(text_words > 80):
    #quillbot is just shit
    output_results += get_quillbot_prediction(text,headless,timeout)
  else:
    print(f"not enough words for quillbot prediction: {text_words}/80 words")

  if (text_length > 750):
    #hive might fail due to captcha
    output_results += get_hive_prediction(text,headless,timeout)
  else:
    print(f"not enough characters for hive prediction: {text_length}/750 characters")
  
  if (text_words > 60):
    output_results += get_writer_prediction(text,headless,timeout)
  else:
    print(f"not enough characters for merlin prediction: {text_length}/500 characters")
  
  print(output_results)

if __name__ == "__main__":
  main()