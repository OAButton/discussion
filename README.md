#  Open Access Button
========
## Push Button. Get Research. Make Progress.

We all know the frustration of finding the research paper you need, but you can't afford the $40 to access it. The Open Access Button helps you get the research you want right now, and adds papers you still need to your wishlist.

Following the re-launch of the Open Access Button in Open Access Week, we are working hard to build and expand in the coming months. Clear instructions for contributing will follow soon but until then, feel free to check out the Wiki and Issues to see how you can help, or email Joe@openaccessbutton.org.

## This Repository

In this repository you will find the all the code that runs the backend of the Open Access Button. The client-side code can be found in the following repositories.
[Firefox App](https://github.com/OAButton/oab-fxaddon)
[Chrome App](https://github.com/OAButton/oab-chromeaddon)

We are use the wiki for our project management around the technical development of the Open Access Button, although at the moment that is mostly just the minutes from development calls.

## Open Access Button Repositories

First of all, we have a few different repos here:

* https://github.com/OAButton/backend
    - This is the main backend. It includes the code for the website, as well as the database of user stories that we have gathered from people.
    - The other repos connect to this, and act as different front-ends.
* https://github.com/OAButton/oab-fxaddon
    - This is the Firefox addon.
* https://github.com/OAButton/oab-chromeaddon
    - Our Chrome (and Chromium) addon.
* https://github.com/OAButton/OAButton_old
    - This is the old proof of concept bookmarklet and is no longer supported.

## Development

We have decided not to use a general mailing list, and have decided to work through issues here on Github. General queries and issues are best dealt with in the [backend repo](https://github.com/OAButton/backend/issues). 

## License

All of our code is licenced under an MIT licence and all site content is licenced under a Creative Commons Attribution Licence.

###Setting up a development enviroment

####Ubuntu Linux

1. Copy the project: `git clone https://github.com/OAButton/backend`

1. cd into the project folder. You may wish to create a new virutal environment. `virtualenv venv`.

1. Run `python setup.py`.

1. Install requirements: `sudo apt-get python-dev libxslt1-dev libxml2-dev`

1. Next we'll need to install elasticsearch. [I followed the tutorial here:](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-on-an-ubuntu-vps)

1. cd into portality folder. Open `settings.py` and add the correct IP address and port for Elastic Search. If desired, enter you CORE API key (which you can get from http://core.ac.uk/intro/contact) and your ContentMine API key (which you can get from ???)

1. From the main project folder, run `python load.py` to load oa.json records into elasticsearch.

1. cd into portality. Run `python app.py`. Point your browser to localhost:5004 and away we go.
