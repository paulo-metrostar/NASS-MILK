# Monthly Milk Production
## dummy-data
- contains all the data objects that should be available for a user
    - you'll note there is A LOT of scemantic-redundancy as the same data is "prepared" in various formats to maximize efficiency and accessibility for users.
    - if memory-bloat becomes a concern we can discuss "on-demand" ETL processes
    - But _how_ we make all of the data available to the user is not the question I'm trying to answer here. I'm just trying to show _what_ should be available to the user.
        - (we can, add or subtract objects as we move forward)

## current-report.pdf
- a copy of the current monthly milk-production report

## tidy-report.pdf
- a "static" pdf export of the tidy-report that is generated in `report-generator`
- I haven't figured out how to make the "internal navigation links" work in the static version yet.
- You'll really want to see the "live version" when I demo it.
    - anything in brackets indicates I can programatically automate it's content based on access to the data

## report-generator
- contains a python app which can automate report generation provided it has access to the tidy-data
- there isn't really any "data" in there so this need not be in the data-mart