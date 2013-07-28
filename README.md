Backstory
---------

I wanted to have a creative business card that I could give out at [DBX](https://www.dropbox.com/dbx), which also involves Dropbox. Assuming that it is a Dropbox conference and everyone would obviously have Dropbox accounts and smartphones, I built this with the Core API and Google App Engine. It's a very small and rough app that I built in very less time. 

How does it work?
-----------------

I would have cards printed with the attached images, very simple and clutter-less. When I  meet someone, I would give out the card and depending on the situation, I would ask them to scan the QR code with their smartphone, which will take them to the GAE App I built, which will be taken to the Dropbox's app authorization page. When authorized, my app would add my details to the person's Dropbox. I also had few NFC tags ready to go with the cards, which can be used to replace the QR code. This right here is a very small and simple example in one of the many ways how the developers use Dropbox's API. This is just a very basic concept, which could have some flaws, but I wanted to try it out.

![back of the card](https://raw.github.com/var/dbxcard/master/static/img/back.jpg)
![front of the card](https://raw.github.com/var/dbxcard/master/static/img/front.jpg)

Code
-----
* The entire code is above, including the Dropbox's SDK
* Built with Google App Engine's webapp2, NDB, jinja2, Dropbox Core API, OAuth 1.0