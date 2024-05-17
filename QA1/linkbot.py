from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path
class Linkbot:
    def __init__(self, url):
        self.starturl = url
        self.past_data = {}
        self.current_data = {}
        self.current_element_info = {}
        self.current_element = None
        self.current_elements = None
        self.driver = None
        self.current_url = None
        self.is_update_current_element = None
        self.fun_name = None
        self.pass_current_element = None
        self.one_param = None


    def startpoint_load(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.starturl)
        self.driver.implicitly_wait(2)
        self.current_url = self.driver.current_url
        

    def find_elements_by_tag(self, tag:str, filter=True, one_param=False):
        temp_fun_name:str = 'find_elements_by_tag'
        self.current_url = self.driver.current_url
        if one_param == False:
            if filter == True:
                filter_elements = []
                for element in self.current_elements:
                    self.current_element = element.find_element(by=By.TAG_NAME, value=tag)
                    filter_elements.append(self.current_element)
                    self.processing_elements(fun_name=temp_fun_name, value=tag, one_param=True, tag=tag)
                self.current_elements = filter_elements
                return filter_elements
            elif filter == False:
                self.current_elements = self.driver.find_elements(by=By.TAG_NAME, value=tag)
                self.processing_elements(fun_name=temp_fun_name, value=tag, tag=tag)
                return self.current_elements
            else:
                pass
        elif one_param == True:
            if filter == True:
                self.current_element = self.current_element.find_element(by=By.TAG_NAME, value=tag)
                self.processing_elements(fun_name=temp_fun_name, value=tag, one_param=True, tag=tag)
                return self.current_element
            else:
                self.current_element = self.driver.find_element(by=By.TAG_NAME, value=tag)
                self.processing_elements(fun_name=temp_fun_name, value=tag, one_param=True, tag=tag)
                return self.current_element
        else:
            pass       
    def filter_hrefs(self, index:int, string): # -> elements
        filtered_elements = []
        self.current_url = self.driver.current_url
        for element in self.current_elements:
            if len(Path(element.get_attribute('href')).parts) < index + 1:
                pass
            elif string in Path(element.get_attribute('href')).parts[index]:
                self.current_element = element
                filtered_elements.append(self.current_element)
                self.processing_elements(fun_name='filter_hrefs', value=string, one_param=True)
            else:
                pass
        self.current_elements = filtered_elements
        return filtered_elements


        #The function below updates current_element_info & current_data_info % past_data_info
    def update_current_element_info(self, function=None, Value=None, tag=None):
        tag_name, value_name, function_name = [],[],[]
        if len(self.past_data) == 0:
            tag_name.append(tag)
            value_name.append(None if Value is None else Value)
            function_name.append(None if function is None else hash(function))
        elif self.current_element in self.past_data[self.current_url].keys():
            past_data_tag:list = self.past_data[self.current_url][self.current_element]['tag']
            past_data_value:list = self.past_data[self.current_url][self.current_element]['value']
            past_data_function:list = self.past_data[self.current_url][self.current_element]['function']
            tag_name:list = past_data_tag.append(tag)
            value_name:list = past_data_value.append(None if Value is None else Value)
            function_name:list = past_data_function.append(None if function is None else hash(function))
        elif self.current_element:
            tag_name.append(tag)
            value_name.append(None if Value is None else Value)
            function_name.append(None if function is None else hash(function))
        else:
            pass
        self.pass_current_element = {'id': self.current_element.get_attribute('id'),
                          'tag': tag_name, 
                          'text': self.current_element.text,
                          'value': value_name, 
                          'function': function_name} 
        self.current_element_info.update(self.pass_current_element)
        self.is_update_current_element = True
        self.update_current_data_info(self.pass_current_element) 
        self.update_past_data_info(self.pass_current_element)
        self.is_update_current_element = False


    def update_current_data_info(self, pass_element):
        if self.is_update_current_element == True:
            self.current_data.update({self.current_element : pass_element})
        else:
            pass


    def update_past_data_info(self, pass_element):
        if self.is_update_current_element == True:
            if not self.current_url in self.past_data.keys():
                self.past_data.update({self.current_url:{self.current_element : pass_element}})
            else:
                self.past_data[self.current_url].update({self.current_element : pass_element})
        else:
            pass
        
        #processing_elements function unifies all updating functions
    def processing_elements(self, fun_name=None, value=None, one_param = False, tag=None):
        if one_param == False:
            for current_element in self.current_elements:
                self.current_element = current_element
                self.update_current_element_info(function=fun_name, Value=value, tag=tag)
        elif one_param == True:
            self.update_current_element_info(function=fun_name, Value=value, tag=tag)
        else:
            pass


