from typing import Any
import kajiki  
import json
from _settings import CONFIG_LOAD_FROM,CONFIG_LAYOUT_NAME

class ChildAndParent2:
    def __init__(
        self,
        child_path:str,  
        ) -> None:
        self._config_load_from = CONFIG_LOAD_FROM
        self._config_layout_name = CONFIG_LAYOUT_NAME
        self.loader = kajiki.FileLoader(self._config_load_from)
        self.child_path = child_path   
        
    def try_load_import(self,path:str):
        try:
            c1 = self.loader.import_(path)
            return c1
        except TypeError :
            print("failed to render temaplate")
            #print(path ) 
            print(TypeError)
            exit()
            
    def try_render_template(self,template:Any,d:dict):
        try :
            t_str:str = template(d).render()
            return t_str
        except TypeError :
            print("failed to render temaplate") 
            print("with parametres " )
            #print(d)
            print(TypeError)
            exit()
            
    def get_json_file_path(self,path:str):
        p =  path.replace(".html",".json")
        p = self._config_load_from+"/"+p
        return p
            
    def render_template(self):
        c1 = self.try_load_import(self.child_path) 
        c1_json_path = self.get_json_file_path(self.child_path)
        with open(c1_json_path) as json_file:
            data = json.load(json_file)
            #print(data)
            c1_str = self.try_render_template(c1,data)
            p1 = self.try_load_import(self._config_layout_name) 
            p1_str = self.try_render_template(p1,{"content":c1_str})
            return p1_str
  



