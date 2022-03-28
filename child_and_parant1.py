from typing import Any
import kajiki  


class ChildAndParent:
    def __init__(
        self,
        child_path:str,
        child_dict:dict,
        parent_path:str, 
        ) -> None:
        # "." mean files in current directory and his subdirectories
        self._config_load_from = "templates"
        self.child_path = child_path 
        self.child_dict = child_dict
        self.parent_path = parent_path
        self.loader = kajiki.FileLoader(self._config_load_from)
        
    def try_load_import(self,path:str):
        try:
            c1 = self.loader.import_(path)
            return c1
        except TypeError :
            print("failed to render temaplate")
            print(path ) 
            print(TypeError)
            exit()
            
    def try_render_template(self,template:Any,d:dict):
        try :
            t_str:str = template(d).render()
            return t_str
        except TypeError :
            print("failed to render temaplate")
            print(self.child_path )
            print("with parametres " )
            print(self.child_dict)
            print(TypeError)
            exit()
            
    def render_template(self):
        c1 = self.try_load_import(self.child_path) 
        c1_str = self.try_render_template(c1,self.child_dict)
        p1 = self.try_load_import(self.parent_path) 
        p1_str = self.try_render_template(p1,{"content":c1_str})
        return p1_str
        
        
    def set_config_load_from(self,path:str):
        self._config_load_from = path


c1 = ChildAndParent("child.html",{},"parent.html",)
html_text = c1.render_template()
print(html_text)