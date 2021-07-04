# CommentAPI

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<p align="center">
  <h3 align="center">Codingal : backend assessment</h3>

  <p align="center">
    threaded comments application.
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a threaded comment application .As per codingal backend assesment task requirement . 

I have made a django webapp for implementing threaded comment functionality . I have choosen a theam of open form discussion and implemented accordingly .The user can see the multiple open discussion form where people can comment their opnion and discuss things with the world . 

User can read everyones comments and login to write comment or reply to others comments .
Admin can delete any single or whole thread of comments by deleting the parent comment or by deleting the form/page itself.Admin can delete all comment by deleting the page itself. Admin can also edit comments .

### Built With

These are the tech stack i have used to build this 
* [Bootstrap](https://getbootstrap.com)
* [Django] (https://www.djangoproject.com/)
* [Python] (https://www.python.org/)
* [Django Rest Framework] (https://www.django-rest-framework.org/)
* [Django-ORM] (https://tutorial.djangogirls.org/en/django_orm/)



<!-- GETTING STARTED -->
## Getting Started

Follow the below instruction to run the project in your system

### Installation and setup

1. Clone the repo
   ```sh
   git clone https://github.com/montukv/CommentAPI.git
   ```
2. CommentAPI folder 
   ```sh
   cd commentAPI
   ```
3. Install  packages
   ```sh
   pip install -r requirements.txt
   ```
4. configure database
   ```JS
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run django application
   ```sh
   python manage.py runserver
   ```
6. Login to admin '/admin'
   ```sh
   ID :- montu
   Pass :- 1234
   ```
7. Now you can comment on pages
   Go to '/'

<!-- USAGE EXAMPLES -->
## Usage

Home Page
![home](https://github.com/montukv/CommentAPI/blob/main/Screenshots/home.PNG)
![discussion form](https://github.com/montukv/CommentAPI/blob/main/Screenshots/btc.PNG)
![user can reply to other](https://github.com/montukv/CommentAPI/blob/main/Screenshots/btcreply.PNG)
![API call to get comment list ](https://github.com/montukv/CommentAPI/blob/main/Screenshots/getall.PNG)
![Parent comment in database with parent field as null](https://github.com/montukv/CommentAPI/blob/main/Screenshots/parent%20comment.PNG)
![Child comment in database as parent field pointing to parent comment](https://github.com/montukv/CommentAPI/blob/main/Screenshots/child%20comment.PNG)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Name -Montukeshwar Vaishnaw - Montukeshwar@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/montukeshwar-vaishnaw-199054164/
[home]: screenshot/home.png
[btc]: screenshot/btc.png
[comment1]: screenshot/parent_comment.png
[comment2]: screenshot/btcreply.png
[comment3]: screenshot/getall.png
[com4]: screenshot/usercomment.png
[com5]: screenshot/child_comment.png
