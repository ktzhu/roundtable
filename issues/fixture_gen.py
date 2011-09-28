from fixture_generator import fixture_generator
from issues import models as issues
from django.contrib.auth import models as auth
from django.contrib.comments import models as comments
from datetime import datetime, timedelta

now = datetime.today()

@fixture_generator(auth.User, issues.User)
def test_users():
    users = issues.User.objects
    users.create(username='missmoderator', 
        first_name='Miss', last_name='Moderator', is_superuser=True, is_staff=True)
    users.create(username='james.joyce', first_name='James', last_name='Joyce')
    users.create(username='john.dewey', first_name='John', last_name='Dewey')
    users.create(username='hannah.arendt', first_name='Hannah', last_name='Arendt')    
    users.create(username='iris.murdoch', first_name='Iris', last_name='Murdoch')

    # create passwords
    for user in users.all():
        user.set_password(user.username)
        user.save()

@fixture_generator(issues.Issue)
def test_issues():
    _issues = issues.Issue.objects
    _issues.create(
        name = 'How can we make Hacktoberfest even better',
        description = 'Hacktoberfest has been great, but how could we make it even better next time around?',
        discover = now - timedelta(hours=10),
        discuss = now + timedelta(hours=4),
        resolve = now + timedelta(hours=12),
        vote = now + timedelta(hours=24),
        )

    _issues.create(
        name = "How can colleges be improved to combat the trend of credential inflation?",
        description = "Read the title, why don't you?",
        discover = now - timedelta(hours=10),
        discuss = now - timedelta(hours=8),
        resolve = now - timedelta(hours=2),
        vote = now - timedelta(hours=1),
        )

    _issues.create(
        name = "The Future of Journalism",
        slug = "journalism",
        description = """
<table>
	<tr>
		<td width="63%">
			<img class="floatleft" src="/static/images/composite.jpg" width="150" height="136"/>
			<p>The rapid technological advances of the 20th and 21st centuries have transformed
			industries large and small, and the world of journalism is no exception.  The way that
			media and news is generated, collected, and consumed is radically different than it was
			fifty years ago.</p>
			<div class="clear"></div>
		</td>
		<td width="2%">&nbsp;</td>
		<td width="35%" valign="top">
			<p><b>Links:</b></p>
			<p><a href="http://futureofjournalism.net/">FutureOfJournalism.net</a></p>
			<p><a href="http://www.cf.ac.uk/jomec/conference/futureofjournalism/">Future of Journalism Conference 2011</a></p>
			<p><a href="http://www.washingtonpost.com/opinions/five-myths-about-the-future-of-journalism/2011/04/05/AF5UxiuC_story.html">Five myths about the future of journalism</a></p>
			<p><a href="http://blogs.reuters.com/mediafile/2011/09/26/the-future-of-journalism-in-the-uk/">The future of journalism in the UK</a></p>
			<p><a href="http://www.guardian.co.uk/media/future-of-journalism">The Guardian's Future of Journalism Conference</a></p>
		</td>
	</tr>
</table>
""",
        discover = now - timedelta(hours=10),
        discuss = now - timedelta(hours=8),
        resolve = now - timedelta(hours=2),
        vote = now - timedelta(hours=1),
        )

@fixture_generator(issues.Solution, requires=['issues.test_users', 'issues.test_issues', ])
def test_solutions():
    issue1, issue2, issue3 = issues.Issue.objects.all()
    mod, user1, user2, user3, user4 = issues.User.objects.all()
    solutions = issues.Solution.objects

    solutions.create(
        issue = issue1, 
        author = user2, 
        title = 'More sad clowns.', 
        body = 'Coincidentally, the solution to everything.',
        )

@fixture_generator(issues.Rating, requires=['issues.test_solutions', ])
def test_ratings():
    solution = issues.Solution.objects.all()[0]
    mod, user1, user2, user3, user4 = issues.User.objects.all()
    ratings = issues.Rating.objects
    
    ratings.create(
        user = user3,
        solution = solution,
        score = 3,
        )

@fixture_generator(comments.Comment, requires=['issues.test_issues', 'issues.test_solutions', 'issues.test_users', ])
def test_comments():
    _comments = comments.Comment.objects
    solution1 = issues.Solution.objects.all()[0]
    issue1, issue2, issue3 = issues.Issue.objects.all()
    mod, user1, user2, user3, user4 = issues.User.objects.all()
        
    _comments.create(content_object=issue1, user=user1, site_id=1, comment="Hullo")
    _comments.create(content_object=solution1, user=user1, site_id=1, comment="You are totally right. More clowns, especially sad ones, are what is required.")
    _comments.create(content_object=solution1, user=user2, site_id=1, comment="James, I totally get what you're saying, but I guess I'm just not sure.")
    

@fixture_generator(requires=['issues.test_users', 'issues.test_issues', 'issues.test_solutions', 'issues.test_comments', 'issues.test_ratings', ])
def __all__():
    pass
