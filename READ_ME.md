First thought: manipulating a dictionary seems to be the way to conquere this problem. It also seems simple while simultaneously seeming like something I will overthink.

Create `split_time` function to take input in the form of hh:mm AM/PM and store it in a dictionary with keys of hour, minute, and meridian. Guess we'll find out if this is the right first step.

Update `split_time` to handle duration

Update `add_time` to handle very basic calculation (w/in same meridian) Meridian calculation not worked on yet, just testing the hour and minute addition. Need to work on changing meridian.

Add `meridian_cycle` to switch from AM to PM as needed.

Add `day_checker` function to see how many days elapsed since the first time entered.

I think that doing all the calcuations in minutes and then translating that back to days, hours, and minutes would work better. Added a function called `make minute` that takes a time in minutes and returns the minutes and hours.

Bugs:
`day_checker` does not account for minutes
hours > 12 does not account for more than 12 hours in:
`   if minutes < 10:
            minutes = "0" + str(minutes)
        if hours // 12 % 2 != 0:
            mer = meridian_cycle(mer)
        if hours > 12:
            hours = hours - 12
  `
