# todo

## database 

### user_app

#### User

* username
* first_name
* last_name 
* email
* password

#### UserProfile

* user = models.OneToOneField(User, on_delete=models.CASCADE)
* profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
* birth_date

### Goal_app

#### Goal

* title = models.CharField(max_length=200)
* description = models.TextField(max_length=600)
* total_time = models.IntegerField()
* total_spend = models.IntegerField(default=0)
* is_done = models.BooleanField(default=False)
* created_at = models.DateTimeField(auto_now_add=True)
* finished_at = models.DateTimeField()
* parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
* user_id
* type
* picture 

#### Task

* title = models.CharField(max_length=200)
* description = models.TextField(max_length=1000)
* date = models.DateTimeField(default=datetime.datetime.now)
* duration = models.IntegerField()
* created_at = models.DateTimeField(auto_now_add=True)
* goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)
* user_id
* day_id
* interval (from to)
* type

#### Comment

* content
* created_at = models.DateTimeField(auto_now_add=True)
* goal_id

#### Tag

* name
* color
* icon

#### GoalTag

* goal_id
* tag_id

#### TaskTag

* task_id
* tag_id


### day_app

#### Day

* date
* user_id

#### Report

* content = models.TextField(max_length=800)
* created_at = models.DateTimeField(auto_now_add=True)
* day_id = one to one

#### Question

* content 
* type

#### Answer 

* content 
* question_id

#### DayQuestion

* day_id
* question_id
* value(777)




### to do


* register all models in admin
* add urls.py file for each app and configure the main urls file
* add route to each operation in urls file
* creating view for each rout and show basic message
* complete the simple views ex: index ... etc
* handel user login and logout
* create form for (goal, task, report, question, use)
* handel update and delete for each prev item

* add choices to type and maybe colors
* add validation to forms
* some filters and queries to show data in good form.
* use react as front end framework
* user react calendar to view month, week, and day.
* make chorme extension for timer and logger and add tasks


* add comments and docs
* test all scenarios of the app
* add more features


