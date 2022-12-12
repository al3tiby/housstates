<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT LOGO -->
<br />

<h3 align="center">Housstates project</h3>

  <p align="center">
    A website for real estate company
    <br />
    <a href="https://github.com/al3tiby/housstates"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

This project have a website for company th show the world thier latest project and thier blog, the website also have "contact us" page and a newsletter subscription.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To have the same project I have, git tis repo and follw my steps.


### Installation

1. Clone the repo and enter the repo folder
   ```sh
   git clone https://github.com/al3tiby/housstates.git
   cd housstates
   ```
2. Install Pipenv and make a shell
   ```sh
   pip install pipenv
   pipenv shell
   ```
3. Install `Django` and the required packages
   ```sh
   pipenv install django
   pipenv install -r requirements.txt
   ```
4. Go to `project_management/.env` file and replace * with your needed informations
   ```env
   DATABASE_NAME=postgres
   .....
   ```
5. Now migrate the changes to tha Database
  ```sh
   python manage.py migrate
   ```
6. Now Run the server and enjoy
  ```sh
   python manage.py runserver
   ```
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

