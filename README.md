# dad-joke-term-counter
Simple web application that counts the number of terms in dad jokes. A combination of React and Flask was used for this project. The backend queries for massively entertaining dad jokes using the https://icanhazdadjoke.com/api.
Here are some images of the application running:
<img align="center" src="/sample_images/app_pic1.png"
	title="Application Running" width="200" />
<img align="center" src="/sample_images/app_pic2.png"
	title="Application Running" width="200" />  
  
  Enjoy!

## Dependencies
Python
* flask
* requests
* grequests
* flask-cors
* ... amongst others

JavaScript
* ReactJS
* Babel
* Node.js



## Installation Guide
This installation guide has been written with Windows users in mind.  
First off, clone the repository.
```
git clone https://github.com/choi-william/dad-joke-term-counter.git
```
### Front-end
Recent version of Node.js should already be installed.
1. Change directory 
```
cd dad-joke-term-counter\frontend
```

2. Install npm dependencies

```
npm install
```

3. Run the app locally.

```
npm start
```
### Back-end
For the back-end, the assumption is that you have Python 3.5 or newer installed. As usual, it's recommended that the latest version of python is used. Also, it's recommended that a virtual environment is used to manage dependencies in the project.

1. Change directory 
```
cd dad-joke-term-counter\backend
```
2. Create and activate the virtual environment
```
py -3 -m venv venv
venv\Scripts\activate
```
3. Install Python Packages using pip
```
pip install -r requirements.txt
```
4. Run the app locally
```
python backend.py
```


