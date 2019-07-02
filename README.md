# selenium_background CentOS_7

Este es un pequeño ejemplo para correr en background, esto quiere decir que no va interactura el navegador, para ello se uso chrome.

Paso de instalación, se debe tener una version superior a python 2.7. 

* Instalar módulo de selenium para python
    * pip install selenium
* Descargar el  webdriver de Chrome
    * https://sites.google.com/a/chromium.org/chromedriver/
* Descargar el IDE para configurar o grabar las interacciones del usuario(En la maquina donde se realiza las grabaciones)
    * https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd
*  Descargar el rpm para el binary de chrome
    * wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
*   Instalar el RPM del binary del chrome
    * yum localinstall google-chrome-stable_current_x86_64.rpm
