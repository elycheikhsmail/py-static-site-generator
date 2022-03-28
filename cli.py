import typer
app = typer.Typer()
import os 
from child_and_parent2 import ChildAndParent2
from pathlib import Path
from _settings import TEMPLATE_PATH
from _settings import STATIC_ROOT, MEDIA_ROOT
from _settings import BUILD_STATIC_ROOT, BUILD_MEDIA_ROOT

from helper import copy_static_file
 
@app.command()
def copystaticfile():
    print(STATIC_ROOT) 
    print(BUILD_STATIC_ROOT)
    copy_static_file(STATIC_ROOT,BUILD_STATIC_ROOT)
    copy_static_file(MEDIA_ROOT, BUILD_MEDIA_ROOT)
    print("static files was copied")

@app.command()
def g(path: str):
    typer.echo(f"... start generatine html from template and data in ...: ")  
    typer.echo(f"{TEMPLATE_PATH/path}")  
    typer.echo(f".......")  
    if (Path.exists(TEMPLATE_PATH/path)):
        c1 = ChildAndParent2(path)
        html_text = c1.render_template() 
        p = DEST+"/"+path
        #str(Path(DEST / path))
        with open(p,"w") as f :
            f.write(html_text)
            typer.echo("generate html from template ")
            typer.echo(".....work  done ..... ")
    else:
        typer.echo("no file found in indicate pathe ")
        typer.echo("path must be relative to templates folder ")
        
        


@app.command()
def gAll():
    print("g all, not yet implemented")


if __name__ == "__main__":
    app()