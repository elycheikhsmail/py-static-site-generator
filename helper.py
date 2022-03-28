
# Python program to explain shutil.copytree() method 
       
# importing os module 
import os 
   
# importing shutil module 
import shutil  
def copy_static_file(src:str,dest:str):
    try: 
        shutil.rmtree(dest)
    except Exception as e:
        pass 
    shutil.copytree(src, dest,symlinks=False) 
   
