# quiz_app

This is flashcard app built to mimic wanikani's study patterns. You can input
or import new databaes as csv files along with the langauge. You can then
choose any of the imported databaese to study from. It integrates with OS
library to input a mac keyboard shortcut to switch the keybaord laungage when
a different language is needed for the answer.

Known bugs:
- The keyboard shortcut simply changes the lauguage when the flashcard's 
laguage does not match the current language. It does not recognize and choose
the desired langauge 
- Inputting new databases through the interface does not currently work
- If the app is started and english is not the default keyboad the shortcut
command will not work correctly

Future Plans:
- Implement spaced repetition system