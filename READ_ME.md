First thought: manipulating a dictionary seems to be the way to conquere this problem. It also seems simple while simultaneously seeming like something I will overthink.
^This was overthinking. Doing everything in minutes was much easier.

Create `split_time` function to take input in the form of hh:mm AM/PM and store it in a dictionary with keys of hour, minute, and meridian. Guess we'll find out if this is the right first step.

Update `split_time` to handle duration

Update `add_time` to handle very basic calculation (w/in same meridian) Meridian calculation not worked on yet, just testing the hour and minute addition. Need to work on changing meridian.
^This approach obsolete when basing all calculations on minutes

Add `meridian_cycle` to switch from AM to PM as needed.
^update to `make_mer` Meridian now determined by minutes from midnight

Add `day_checker` function to see how many days elapsed since the first time entered.
^replaced by `make_days`

I think that doing all the calcuations in minutes and then translating that back to days, hours, and minutes would work better. Added a function called `make minute` that takes a time in minutes and returns the minutes and hours.
^This thought seems to have been correct

Updated all functions to work based off of minutes. New functions include:
`make_days`
`make_hours`
`make_minutes`
`make_mer`

Made `make_day_of_the_week` function to loop through days of the week based on the minutes. Now I need to handle a variety of string input errors and this project will be completed.

All functions updated and all tests passed. This project is complete. The functions are a bit verbose, but at this stage in my learning, that is okay. On to the next challenge!
