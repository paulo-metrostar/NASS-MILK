# Druid Team,
- We need to make a group decision about the minimum level of data manipulation and analysis skills we assume a user will have

## I recommend including both the wide and long formats of every table in a release download
- the tables are small enough (per release) that the redundancy in memory shouldn't be a significant issue
- this will make the data auto-visualizable and auto-analyzable "out of the box" especially for users who do not already know how to do tabular manipulations
- I also think this reduces our "educational burden" because users can simply browse and use the table the "like" and ignore the rest

### If we assume users do know how to manipulate tables we can give them one format and let them do the manipulation (I don't recommend this)
- This isn't too different from the current QS which assumes users will "figure it out"
- Alternatively, we could educate users on when and how to pivot a long table to a wide one, and "melt" a wide table toa long one
    - I also don't recommend this because each tool will have their own idiosyncratic process which we either research and digest for them or abandon them to do it themselves

### Another option is to give the users a choice between requesting either the long or the wide data and educatinig them on the difference
- I also don't recommend this approach, as it reminds me of requiring users to know or learn the difference between survey and census before they can "just see" the data
- Also, we would have to then handle the implementation of the choice at various "stops" along a user's journey.

## Note:
- the data dictionary and metadata are just placeholders for now
    - eventually, someone, likely me, will need to create a "master data dictionary" and each data-mart can just pull the entries included in its use case.
