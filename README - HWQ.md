What happens when you press the “submit” button? Paste the full URL you are sent to on submit.

file:///fortune_results.php?firstname=&favcolor=%23353dff&title=&knighted=&knight3=Tristan&knight6=Etienne+Navarre&drink=

What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?

The keys correspond to the answers given to the questions in the form. The name and key fields are given in the URL as a key value pair. So when I enter William as my name, the key value pair in the URL is "firstname=William"

What are the values of the URL query string? How do they correspond to what the user entered or typed?

Examples of values are William, Tristan, Blue, Mead, etc.

Stretch challenge question:

Is there a way to pass multiple values through the URL query string for a single key? How can we do so?

If the question is the form element question is of the type which allows multiple answers, then you can return multiple values for that single key. For example a question with checkboxes.