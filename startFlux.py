# coding: utf8
# Boilerplat for flux paradigm using React JS
# Creat a workspace in the current directory
# ---------------------------------------------------
import os
# ---------------------------------------------------
APP_NAME = "YourAppName"
APP_DIR = "./"
JS_DIR = APP_DIR + "js/"
# ---------------------------------------------------
_dirs_js = ["actions","components","constants","dispatcher","stores"]

DIRS = {i : JS_DIR + i + "/" for i in _dirs_js}
DIRS["js"] = JS_DIR
DIRS["css"] = APP_DIR + "css/"
# ---------------------------------------------------
FILES = {"app.js" : DIRS["js"] + "app.js"}
FILES["app.css"] = DIRS["css"] + "app.css"
FILES["actions"] = DIRS["actions"] + APP_NAME + "Actions.js"
FILES["components"] = DIRS["components"] + APP_NAME + ".react.js"
FILES["constants"] = DIRS["constants"] + APP_NAME + "Constants.js"
FILES["dispatcher"] = DIRS["dispatcher"] + "AppDispatcher.js"
FILES["stores"] = DIRS["stores"] + APP_NAME + "Store.js"
FILES["index"] = APP_DIR + "index.html"
FILES["package.json"] = APP_DIR + "package.json"


# ---------------------------------------------------
APP_CONF = {
	"app_id" : "react_app",
	"app_title" : "Flux • App",
	"app_lang" : "en",
	"app_section_id" : "section_my_app"
  }
# ----------------------------------------------------
APP_ACTIONS = """
 */
 * {app_name}Actions
 */

var AppDispatcher = require('../dispatcher/AppDispatcher');
var {app_name}Constants = require('../constants/{app_name}Constants');

var {app_name}Actions = {{
  
}};
""".format(app_name = APP_NAME)
# ---------------------------------------------------
APP_COMPONENT = """
var React = require('react');

var {app_name} = React.createClass({{

  getInitialState: function(){{
    return {{
      text : "Hello World - this a React App named : {app_name}"
    }};
  }},

  componentDidMount: function() {{
    alert("{app_name} mounted !");
  }},

  /**
   * @return {{object}}
   */
  render: function() {{
    return (
      <div id="{app_id}">
        <p> {{this.state.text}} </p>
      </div>
    );
  }},
}});

module.exports = {app_name};
""".format(app_name = APP_NAME, app_id = APP_CONF["app_id"])
# ---------------------------------------------------
APP_CONSTANT = """
/*
 * Constants
/*
var keyMirror = require('keymirror');

module.exports = keyMirror({
  {

  }
});
"""
# ---------------------------------------------------
APP_DISPATCHER = """
/*
 * A singleton that operates as the central hub for application updates.
 */

var Dispatcher = require('flux').Dispatcher;

module.exports = new Dispatcher();
"""
# ---------------------------------------------------
APP_STORE = """
/*
 * Store
 */
"""
# ---------------------------------------------------
APP_JS = """
var ReactDOM = require('react-dom');
var React = require('react');

var {app_name} = require('./components/{app_name}.react');

ReactDOM.render(
  <{app_name} />,
  document.getElementById('{app_id}')
);
""".format(
    app_id = APP_CONF["app_section_id"] ,
    app_name = APP_NAME
  )
# ---------------------------------------------------
APP_CSS = """
/* css of your app here */
#{app_id}{{
	
}}
""".format(app_id=APP_CONF["app_id"])
# ---------------------------------------------------
APP_INDEX = """
<!doctype html>
<html lang="{app_lang}">
  <head>
    <meta charset="utf-8">
    <title>{app_title}</title>
    <link rel="stylesheet" href="css/app.css">
  </head>
  <body>
  	<header>
  		<p> The Header :) </p>
  	</header>
    <section id="{app_id}"></section>
    <footer>
      <p>The Footer :)</p>
    </footer>
    <script src="js/bundle.js"></script>
  </body>
</html>
""".format(
	app_lang	= APP_CONF["app_lang"],
	app_title = APP_CONF["app_title"],
	app_id 		= APP_CONF["app_section_id"] 
	)
# ---------------------------------------------------
APP_PACKAGE_JSON = """
{{
  "version"     : "1.0.0",
  "description" : "{app_name} : A React App based on Flux",
  "author"      : "{app_name}",
  "scripts": {{
    "start": "watchify -o js/bundle.js -v -d js/app.js"
  }},
  "browserify": {{
    "transform": [
      "reactify",
      "envify"
    ]
  }}
}}
""".format(app_name = APP_NAME)
# ---------------------------------------------------
FILES["app.js"] = (FILES["app.js"],APP_JS)
FILES["app.css"] = (FILES["app.css"],APP_CSS)
FILES["actions"] = (FILES["actions"],APP_ACTIONS)
FILES["components"] = (FILES["components"],APP_COMPONENT)
FILES["constants"] = (FILES["constants"],APP_CONSTANT)
FILES["dispatcher"] = (FILES["dispatcher"],APP_DISPATCHER)
FILES["stores"] = (FILES["stores"],APP_STORE)
FILES["index"] = (FILES["index"],APP_INDEX)
FILES["package.json"] = (FILES["package.json"],APP_PACKAGE_JSON)
# ---------------------------------------------------
# Creating directories
for name,path in DIRS.items(): 
	os.makedirs(path,exist_ok=True)
# ---------------------------------------------------
# Creating empty files
for name,item in FILES.items():
  path,content = item
  print("- ",name," -")
  print(content,file=open(path,"w"))
  print("-" * 20)
	# f = open(path,"w")
 #  f.write(FILES)
 # ---------------------------------------------------
import subprocess
_savedPath = os.getcwd()
 # WINDOWS ONLY : npm package
  # flux
os.chdir(APP_DIR)
subprocess.call(["npm","install","--save","flux"],shell=True)
subprocess.call(["npm","install","--save","keymirror"],shell=True)
subprocess.call(["npm","install","--save","react"],shell=True)
subprocess.call(["npm","install","--save","react-dom"],shell=True)

subprocess.call(["npm","install","--save-dev","watchify"],shell=True)
subprocess.call(["npm","install","--save-dev","reactify"],shell=True)
subprocess.call(["npm","init","--yes"],shell=True)
subprocess.Popen(["cmd","/K","npm","start"])
os.chdir(_savedPath)