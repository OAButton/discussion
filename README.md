<a href="https://zenhub.com"><img src="https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png"></a>
<a href="https://www.browserstack.com/start"><img src="https://github.com/OAButton/discussion/blob/master/Screen%20Shot%202017-01-08%20at%2008.52.37.png?raw=true"></a>

#  Open Access Button

## Welcome! 

Hi, welcome to Github. Github is where the Open Access Button keeps all it's code, discusses huge amounts of our work & more. It's all openly availiable, and we do it here because we want your help. 

## About the project

The Open Access Button is an app that helps researchers, patients, students and the public get legal access to research they need and request research be made available. Since November 2013, we have made 15,000 requests for research articles and data.

## Getting Started

If you want to help us build the tools, here are some helpful bits of information! We'll start putting more here soon as it's harder than it should be to dive in and help right now! Let us know what you'd like to see. 

### Quick Guide

* Make an issue (to start a discussion, file a bug or make a suggestion) in the "discussion" repository: https://github.com/OAButton/backend/issues/new 
* Contibute code: You're in the wrong place, see our other repos (below)

### Ways to contribute

* [Take an hour out of your day give us some feedback on the tool]
(https://docs.google.com/forms/d/e/1FAIpQLSdK3wRKixTVtjn0o8RWvU1MlPPIIKRBsBrHHi6ER_4A3YAmUA/viewform?c=0&w=1&usp=send_form)
* Dive into a [starter issue](https://github.com/OAButton/backend/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)
* Take on a [quick fix](https://github.com/OAButton/backend/issues?q=is%3Aopen+is%3Aissue+label%3A%22Quick+Fix%22), or [bug](https://github.com/OAButton/backend/issues?q=is%3Aopen+is%3Aissue+label%3A%22Quick+Fix%22+label%3Abug). 

or if you're not interesting in the technical side of things we'd love your help talking to users (potential, new & old) and scheming for how to making things better. 

### Open Access Button Repositories

We have a few different repos here:

* https://github.com/OAButton/backend
    - This repo is used to discuss all technical work. However, open access button works by using the Cottage Labs API, so there is no functional code in this repo.
    - OAB is the first examples of developing various front-end services that can work entirely via the CL API, saving the need for dedicated backend development and maintenance. The CL API code can be found at https://github.com/CottageLabs/api
* https://github.com/OAButton/oab_static
    - Contains code for
        - site content for https://openaccessbutton.org
        - bookmarklet code
        - emails
    - you'll find info on editing the site in the readme
* https://github.com/OAButton/unified-extension
    - This is where we have developed our unified extension, for use in chrome and firefox
* https://github.com/OAButton/project-management
    - This is where we discuss project management, and roughly plan the future.

* we have other repo's but they're not being actively worked on or supported.

### Getting in touch

We have decided not to use a general mailing list (because who needs another list?), and have decided to work through issues here on Github. General queries and issues are best dealt with in the [backend repo](https://github.com/OAButton/backend/issues/new). We use Zenhub for some extra layers of co-ordination that Github isn't so good at yet.

### Labels, Milestones, Assignments & other notes on how we use issues

Important: Before a change is tested on the development site, an issue can't be considered completed. This counts even for simple copy changes. 

What do the various labels/assignments mean for the project?

* Bug: something that isn't working as expected
* Enhancement: a way to improve something, usually a new requirement
* Question / Discussion: a question or topic of discussion. Doesn't denote we should actually do something, just think about it. 
* help wanted: we'd love help here! (coming soon: good first bugs)
* Plugin / Bookmarklet / Website / Emails / Admin: the place the issue relates too
* Priority: more important than other things in a catagory
* Blocked x : We need x in order the close the issue. These labels are added when an issue is created as part of estimating how much work will be needed to close it (and how to close it). They are not removed. 
* Jisc: This label shows work supported by Jisc (thanks Jisc!). 

Assignmenting to a milestone is confirmation we're planning to do something. Otherwise, we're not currently planning to do much with it and the issue is just there for safe keeping incase one day we do. 

Assignmenting to a person means it is currently possible for that person to work on that issue & signifies who is currently needed to move an issue forwards. An issue can be assigned to multiple people at once. If you're assigned an issue, but don't know what you should be doing (or can't do it for some reason) just say. 

@comment someone if you need them to see a message. 

### People

Who are the people you see commonly in this repo at the moment? 

* Joe: Co-founder of the project
* Mark: Lead dev from Cottage Labs
* Chealsye: Our communications lead who discusses bits and pieces
* Megan: Does a lot of testing for the Button
* a variety of other contributors who pop in and out

we're all super friendly, say hello! The people involved in the project more broadly can be found here: https://openaccessbutton.org/about#team

### How we handle bugs

* Bugs are considered maintainance, rather than development. They are handled on a bug - by - bug basis independantly of sprints.
* When a bug is filed on Github we will triage it to understand it's severity, and complexity. 
* A bug fix can be intergrated into a current sprint if desired - if needed we can move issues out of the sprint in this case. 

### Terms

We have lots of different names and concepts in the tools now, and it can be hard to know what on earth people are talking about. Below is a work in progress glossary. 

* Sign up: Someone for whom we have an email
* User: Someone with the app installed
* Advocate: Someone who as taken action to directly engage an author, or share the tool. 
* External User: Someone making a block or request via external service (not via request page or apps) e.g PeerLibrary or Sparrow
* People: Catch all for all user types
* Resource: A paper, dataset, program or other material associated with a paper (e.g plasmid)
* Block Story: User or advocate generated message associated with a story
* Block: Any instance an individual can’t access a resource they want. A paper can have multiple blocks associated with it, e.g one block for the paper and one for the data.
* Found: A resource delivered automatically via a repository or search engine (i.e available and discoverable) 
* Block Meta-Data: Paper URL, paper metadata, User type, User location associated with a block
* Inactive Block Rate: A block whose resource wasn’t found, and with no associated request
* Request: An active request from a user for us to find access to a resource, usually via an author
* Support: Taking an action to ... ??? 
* Success: Delivery of a resource to a user or advocate (or acceptable reason why resource can’t be delivered) that couldn’t be found via automated means
* Active *: Interacting with or logging a block in the past month
* Former *: Not interacting with or logging a blog in the past 4 months

### Admin

All users and email functionality can be found here if you have admin access: https://openaccessbutton.org/admin/

### Testing Sites

* Website: http://oab.test.cottagelabs.com/
* Plugin: http://oabe.test.cottagelabs.com/html/main.html
* Bookmarlet: http://oabb.test.cottagelabs.com/
* Emails: You can see emails via the testing site's admin interface. They're also [viewable here](https://github.com/OAButton/oab_static/tree/develop/emails)

## License

We <3 Open Source. All of our code is licenced under an MIT licence and all site content is licenced CC-BY. Moreover, we try to be an open project general with much of our discussion & plans availiable to all. 
