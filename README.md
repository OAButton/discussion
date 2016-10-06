<a href="https://zenhub.com"><img src="https://raw.githubusercontent.com/ZenHubIO/support/master/zenhub-badge.png"></a>
#  Open Access Button and Open Data Button

We're currently working on revamping out Github presence, so our Readme's are in flux. They contain a host of useful information alongside notes. Stay tuned for more. 

## About the project

## Getting Started

If you want to help us build the tools, here are some helpful bigs of information! We'll start putting more here soon as it's harder than it should be to dive in and help right now! Let us know what you'd like to see. 

## Ways to contribute

* Help us test
* Dig into a "non-code" issue
* Do some coding

### Metrics

All current metrics found at: [a URL I need to know if Mark is willing to share]
All users can be found here if you have admin access: https://openaccessbutton.org/admin/openaccessbutton

### Testing Sites

* Website: oab.test.cottagelabs.com
* Plugin: oabe.test.cottagelabs.com/html/main.html

### Open Access/Data Button Repositories

First of all, we have a few different repos here:

* https://github.com/OAButton/backend
    - This repo is used to discuss backend work. However, openaccessbutton and opendatabutton actually work by using the Cottage Labs API, so there is no functional code in this repo. Any future code specifically required for backend functionality for OAB / ODB could be put here if it cannot go in the CL API.
    - OAB and ODB are the first examples of developing various front-end services that can work entirely via the CL API, saving the need for dedicated backend development and maintenance.
    - The CL API code can be found at https://github.com/CottageLabs/api
* https://github.com/OAButton/oab_static
    - the static site content for https://openaccessbutton.org
    - you'll find info on editing the site here
* https://github.com/OAButton/odb_static
    - The static site content for https://opendatabutton.org
    - You'll find info on editing the site here
* https://github.com/OAButton/unified-extension
    - This is where we are developing our new unified extension, for use in chrome and firefox (to become live in Autumn 2016)
* https://github.com/OAButton/oab-fxaddon
    - This is the Firefox addon (soon to be deprecated)
* https://github.com/OAButton/oab-chromeaddon
    - Our Chrome (and Chromium) addon (soon to be deprecated)
* we have other repo's but they're not being actively worked on or supported. 

### Getting in touch

We have decided not to use a general mailing list (because who needs another list?), and have decided to work through issues here on Github. General queries and issues are best dealt with in the [backend repo](https://github.com/OAButton/backend/issues). We use Zenhub for some extra lays of co-ordination Github isn't so good at yet.

### Labels and Milestone crib sheet

What do the various labels/assignments mean for the project?
* Bug: something that isn't working as expected
* Enhancement: a way to improve something
* Question: a question or topic of discussion
* help wanted: we'd love help here! (coming soon: good first bugs)

Assignment to a milestone is confirmation we're planning to do something. Otherwise, we're not currently planning to do much with it and the issue is just there for safe keeping incase one day we do. 

### People [work in progress]

Who are the people you see commonly in this repo at the moment? 

* Joe: Co-founder of the project
* Mark: Lead dev from Cottage Labs
* Steve: Dev from Cottage Labs, usually working on plugins
* Chealsye: Our communications lead who discusses bits and pieces
* a variety of other contributors who pop in and out

we're all super friendly, say hello! The people involved in the project more broadly can be found here: https://openaccessbutton.org/about#team

### Terms [work in progress]

We have lots of different names and concepts in the tools now, and it can be hard to know what on earth people are talking about. Below is a work in progress glossary. 

* Sign up: Someone for whom we have an email
* User: Someone with the app installed
* Advocate: Someone who as taken action to directly engage an author, or share the tool. 
* External User: Someone making a block or request via external service (not via request page or apps) e.g PeerLibrary or Sparrow
* People: Catch all for all user types
* Resource: A paper, dataset, program or other material associated with a paper (e.g plasmid)
* Block Story: User or advocate generated message associated with a story
* Block:Any instance an individual can’t access a resource they want. A paper can have multiple blocks associated with it, e.g one block for the paper and one for the data.
* Found: A resource delivered automatically via a repository or search engine (i.e available and discoverable) 
* Block Meta-Data: Paper URL, paper metadata, User type, User location associated with a block
* Inactive Block Rate: A block whose resource wasn’t found, and with no associated request
* Request: An active request from a user for us to find access to a resource, usually via an author
* Support: Taking an action to ... ??? 
* Success: Delivery of a resource to a user or advocate (or acceptable reason why resource can’t be delivered) that couldn’t be found via automated means
* Active *: Interacting with or logging a block in the past month
* Former *: Not interacting with or logging a blog in the past 4 months
* Service ready * A person, resource, request, story, block can be tied to an institution part of the OAB service (e.g funder, university, publisher)

## License

We <3 Open Source. All of our code is licenced under an MIT licence and all site content is licenced CC-BY.
