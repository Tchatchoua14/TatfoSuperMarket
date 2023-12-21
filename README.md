<h2 align="center"> E-commerce | TatfoSuperMarket </h2>

<p align="center">
  ![Aperçu] <img width="250" height="auto" src="./images/apple-touch-icon-114x114.png">
</p>

![home](./images/loader.gif)

# Django E-commerce TatfoSuperMarket
Django-ecommerce is an open-source ecommerce platform built on the Django Web Framework.
## Features Included
- Custom Admin dashboard
- Search Functionality
- Shopping Cart
- Order Management
- Coupon system
- Payments Using NOTCHPAY 
- Much more...

### Prerequisites

To run this project in production or development mode you have to make sure, [Python](https://www.python.org/downloads/) is installed on your computer. If you opted to install an older version of Python, it is possible that it did not come with `Pip` preinstalled.

- To check Python and Pip are installed on your machine:
```bash
# Python
python --version

# Pip
pip --version

## Installation

```bash
pip install virtualenv
```
In a terminal, run the following command to create virtual environment in the base directory of this project:

```bash
virtualenv venv
```
This command will create a new `venv` folder in your project directory. You can activate the python environment by running the following command:

```bash
# Mac OS or Linux
source venv/bin/activate


**1.clone Repository & Install Packages**
```sh
git clone https://github.com/Tchatchoua14/TatfoSuperMarket.git
pip install -r requirements.txt
```
**2.Setup Virtualenv**
```sh
virtualenv env
source env/bin/activate
```
**3.Migrate & Start Server**
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Built with
Technologies such as **Python** (v3.12) and **Django** in the backend, **SQLite3** in the database architecture and 
**JavaScript**, **Bootstrap4**, **JQuery**, **AJAX**, **HTML5** and **CSS3** in the frontend were used in the development of the project.

- [Python](https://www.python.org/) - Python is an interpreted high-level general-purpose programming language.
- [Django](https://www.djangoproject.com/) - Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern.
- [SQLite](https://www.sqlite.org/index.html) - SQLite is a relational database management system contained in a C library.
- [JavaScript](https://www.javascript.com/) - JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.