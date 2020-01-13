# SAGE-WebScraping
Getting the number of orbital launches in the 'Orbital launches' table in Wikipedia Orbital Launches if at least one of its payloads is reported as 'Successful', 'Operational', or 'En Route'. 
For each launch, listed by date, the first line is the launch vehicle and any lines below it correspond to the payloads, of which there could be more than one. Please note that there might be multiple launches on a single day with multiple payloads within a single launch (we are only interested in the number of distinct launches)([Data source](https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches))

### [XPath](https://en.wikipedia.org/wiki/XPath)
The XPath of different \<tr\> in \<table\>:
- Month Header:

Month Header is the \<tr\> that merging all the column, so we could locate it with relative xpath as ```'.//td[@colspan="7"]'```
- First Line of each launch:

First Line of each launch contains the launch time which is the \<tr\> that has no background style, so we could locate it with relative xpath as the \<tr\> whose ```'attribute::style'``` is none
- Comment Line of each launch:

Comment Line of each launch is the \<tr\> that merging all the column except first column, so we could locate it with relative xpath as ```'.//td[@colspan="6"]'```
- Number of payloads of each launch:

The launch time sell merge all payload row, so we could get the number of payloads through ```'attribute::rowspan'```
