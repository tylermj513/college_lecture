import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) 
web= webdriver.Chrome(options=options)

def run_webdriver(url):
    
        web.get(url)
 
 
        js_code = """
              console.log('Running JavaScript code');
              var checkbox = document.querySelector('input[type="checkbox"][value="1"]');
              if (checkbox) {
                  checkbox.click();
              }

              var selectElements = document.querySelectorAll('select[name="roomCount[]"]');
              if (selectElements.length >= 2) { 
                  selectElements[1].value = "1";
              }

              document.querySelector('input[value="下一步"]').click();
        """

        web.execute_script(js_code)


def run_webdriver2(url):
     
        web.get(url)
        js_code2 = """
         var appNameInput = document.querySelector('input[name="app_name"]');
	 
         appNameInput.value = "張耕齊";
        
          console.log("app_name:", appNameInput.value);
        
        
          var app_tel = document.querySelector('input[name="app_tel"]');
        
          app_tel.value = "0938889077";
        
                console.log("app_tel:", app_tel.value);
              
              
                var app_email = document.querySelector('input[name="app_email"]');
              
                app_email.value = "jason2000891121@gmail.com";
                
                console.log("app_email:", app_email.value);
                
                var checkbox = document.querySelector('input[name="applicant_type"][value="4"]');
                
                checkbox.click();
                
                console.log("Checkbox is checked:", checkbox.checked);
                
                var other_reason = document.querySelector('input[name="other_reason"]');
              
                other_reason.value = "考試";
                
                
                var cardRadio = document.querySelector('input[name="paymethod"][value="card"]');
                cardRadio.checked = true;

                document.querySelector('input[name="contact_name[]"]').value = "張耕齊";

                var checkbox = document.querySelector('input[name="applicant_type"][value="4"]');
                  
                  checkbox.click();
                  
                  const selectElement = document.querySelector('select[name="adult[]"]');

              const options = selectElement.querySelectorAll('option');
              
              
              options.forEach(option => {
                if (option.value === '2') {
                  option.selected = true;
                }  
              });
              
              var checkbox = document.getElementById("iagree");
                
                checkbox.checked = true; 
              
              
                
              
              var submitButton = document.querySelector("input[type='submit']");
            if (submitButton) {
              submitButton.click();
              setTimeout(function() {
                keyboard.press_and_release('enter');
              }, 1); 
            }
 
        """

        web.execute_script(js_code2)


def run_webdriver3( ):
     
        js_code3 = """
                
        const inputElement = document.getElementById("card_1");

        inputElement.value = "1234";
        
        
        const inputElement1 = document.getElementById("card_2");

        inputElement1.value = "5678";




        const inputElement2 = document.getElementById("card_3");


        inputElement2.value = "1234";

        const inputElement3 = document.getElementById("card_4");


        inputElement3.value = "5678";





        var cvv2Input = document.getElementById("cvv2");


        cvv2Input.value = "123";




        var selectElement = document.querySelector('select[name="expiry_month"]');


        selectElement.value = "1"; 
        

        var selectElement1 = document.querySelector('select[name="expiry_year"]');


        selectElement1.value = "6"; 
 
  
        """

        web.execute_script(js_code3)

def run_webdriver4( ):
     
        js_code4 = """
        console.log(1);

          var btnSubmitForm = document.getElementById("btnSubmitForm");
          console.log(2);

          if (btnSubmitForm) { 
            btnSubmitForm.click();
          }
          console.log(3);

        """

        web.execute_script(js_code4)

if __name__ == '__main__':
    url = "https://affairs-guesths.vm.nthu.edu.tw/guest10/index.php?liveFromYear=2024&liveFromMonth=2&liveFromDay=1&liveEndYear=2024&liveEndMonth=2&liveEndDay=2"
    run_webdriver(url)#房
    target_url = "https://affairs-guesths.vm.nthu.edu.tw/guest10/order.php"  
    response = requests.get(target_url, verify=False)
    if response.status_code == 200:
      run_webdriver2(target_url)#資訊
      pyautogui.press('enter')
 
      run_webdriver3() #信
      pyautogui.press('enter') 
      
      target_url2 = "https://webauthen.nccc.com.tw/acsn2_kernel/2/browser/challenge-request"  
      response2 = requests.get(target_url2)
      if (response2.status_code ):
        print(response.status_code)  # Print the status code of the first response

        run_webdriver4() #信
        
 
        print(response2.status_code)  #
        
        time.sleep(4294967)  # Sleep for 1 second
            

