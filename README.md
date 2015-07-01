##7.5 FORMS ON GOOGLE APP ENGINE
###STUDENT NOTES
#### HTML Forms (review)

The form element has two attributes. 
* The method attribute specifies the HTTP method (GET or POST) to be used when submitting the forms. 
  * When you use GET, the form data will be visible in the page's url
  * When you use POST, the submitted data is not visible in the page address
* The action tells what script to run or which page to return to once the submit button is pressed. Since the handler in the python code takes care of the response, don't need to worry about the action attribute and leave it blank. 
```HTML
	<form method="post" action ="">
		<p>Question 1: <input type="text" name="answer1"/></p>
		<p>Question 2: <input type="text" name="answer2"/></p>
		<p><input type="submit"></p>
	</form>
```


####Adding the  Post Method
If you use a post method in your template, you need to add a way for your handler to handle post requests.


```python
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('templates/main.html')
    	self.response.out.write(template.render(template))
    def post(self):
    	self.response.out.write("You have submitted your quiz")
```
In the code above
* When the handler recieves a get request, it's response is to render a template
* When the handler recieves a post request, it's response is to write a message. 

####LINKING the HTML Form and the Handlers
In order to grab the values from our form, we just need to take advantage of the self.request.get() method and grab our values for answer1 and answer2.

In the example below, the complete.html template is rendered with two variables (user_answer_1 and user_answer_2) that contain the values stored within the form input elements named answer1 and answer 2 

```python
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('templates/main.html')
    	self.response.out.write(template.render())
    def post(self):
    template = jinja_environment.get_template('templates/complete.html')
     self.response.out.write(template.render({'user_answer_1': self.request.get(answer1), 'user_answer_2': self.request.get(answer2)}))
```    		
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
