What happens when you press the “submit” button? Paste the full URL you are sent to on submit.

When I press the submit button, it goes to this dead link: file:///fortune_results.php?firstname=William&favcolor=%23353dff&airspeed=African-or-European%21&title=Sorceror&knighted=2019-10-26&knight5=Odysseus&drink=Gorilla+Punch

What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?

The keys of this URL query string are firstname, favcolor, airspeed, title, knighted, knight5, and drink. 
They correspond to the questions asked by the form, in order.


What are the values of the URL query string? How do they correspond to what the user entered or typed?

The values or the URL query string are William, %23353dff&,  African-or-European, Sorceror, 2019-10-26, Odysseus, Gorilla+Punch.

They correspond to the answers given by the user to each question: respectively, to the name entered, the favorite color, the chosen answer to the question about swallow airspeed, the title given, when they were knighted, their hero, and their chosen drink.

Stretch challenge question:

Is there a way to pass multiple values through the URL query string for a single key? How can we do so?

Yes. You need to use a Checkbox form element, which allows you to select more than one answer to a question, and therefore more than one value per key.