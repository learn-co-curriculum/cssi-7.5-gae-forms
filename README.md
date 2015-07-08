##7.5 FORMS ON GOOGLE APP ENGINE
###STUDENT NOTES
#### HTML Forms (review)

The form element has two attributes: method and action.
* The method attribute specifies the HTTP method (GET or POST) to be used when submitting the forms. 
  * When you use GET, the form data will be visible in the page's url
  * When you use POST, the submitted data is not visible in the page address
* The action attribute tells what script to run or which page to return to once the submit button is pressed. Since the handler in the python code takes care of the response, don't worry about the action attribute and leave it blank. 

```
	<form method="post" action ="">
		<p>Question 1: <input type="text" name="answer1"/></p>
		<p>Question 2: <input type="text" name="answer2"/></p>
		<p><input type="submit"></p>
	</form>
```


####Adding the  Post Method
If you use a post method in your template, you need to add a way for your handler to take care of those post requests.


```python
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('templates/main.html')
    	self.response.out.write(template.render(template))
    def post(self): ##here's the new post method in the MainHandler
    	self.response.out.write("You have submitted your quiz")
```
In the code above
* When the handler recieves a get request, it's response is to render a template
* When the handler recieves a post request, it's response is to write a message. 

####LINKING the HTML Form and the Handlers
In order to grab the values from our form, we just need to take advantage of the self.request.get() method and grab our values for answer1 and answer2.


```python
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('templates/main.html')
    	self.response.out.write(template.render())
    def post(self):
    template = jinja_environment.get_template('templates/complete.html')
    ##the variables that are sent to complete.html are user_answer_1 and user_answer_2
    ##they contain the input values from the main.html form with names answer1 and answer2
    template_variables = {'user_answer_1': self.request.get(answer1),
    			  		'user_answer_2': self.request.get(answer2)}
    self.response.out.write(template.render(template_variables))
```    		
###CHALLENGE
* If the user gets all of the answers correct, display a fun image about your city.
* Add a new form in main.html that gets the user’s name and displays it at the top of the results page.
* Add additional other quiz questions by making more input elements on  the form. 
*  Finish the answer_count by displaying the correct # of answers on the results.html page. You should have gone over an answer count in class, but if not, the syntax for the loop is below
  
> ```
user_answers = [self.request.get('answer1'), self.request.get('answer2')]
    	correct_answers = ['correct answer 1', 'correct answer 2']
for i in range(len(correct_answers)):
	    	if user_answers[i].lower() == correct_answers[i]:
	    		answer_count += 1
```

###STRETCH LAB 
* All of the above. 
* There is a way to iterate through 2 lists at a time - you have to use the zip function. Use it to zip the messages list with the answers list. This will allow you to access the first message in your messages list and the first answer in your answers list at the same time.
  * In your handler use `quiz_list = zip(msg_list, answer_list) 
  template.render({'combined_list': quiz_list }`
  * In your template use
  `{% for msg, answer in combined_list %}`
  to iterate through both lists
* Simplify the message logic to loop through the conditions and assign the appropriate message. 
