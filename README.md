##GAE FORMS CHALLENGE

###CHALLENGE
* Finish the answer_count by displaying the correct # of answers on the results.html page. 
* If the user gets all of the answers correct, display a fun Chicago image
* Add a new form in main.html that get’s the user’s name and displays it at the top of the results page.
* Add additional other quiz questions by making more input elements on  the form. 

###STRETCH LAB 
* All of the above. 
* Use the zip function to zip the messages list with the answers list.
  * In your handler use `list = zip(list1, list2) 
  template.render({'list': list, ... }`
  * In your template use
  `{% for item1, item2 in list %}`
  to iterate through both lists
* Simplify the message logic to loop through the conditions and assign the appropriate message. 
