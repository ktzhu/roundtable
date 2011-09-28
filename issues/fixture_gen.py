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
        first_name='Miss', last_name='Moderator', is_superuser=True)
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
        name = 'Something',
        description = 'Yes, something.',
        discover = now - timedelta(hours=10),
        discuss = now + timedelta(hours=4),
        resolve = now + timedelta(hours=12),
        vote = now + timedelta(hours=24),
        )

    _issues.create(
        name = 'Something else',
        description = 'Yes, something.',
        discover = now - timedelta(hours=10),
        discuss = now - timedelta(hours=8),
        resolve = now - timedelta(hours=2),
        vote = now - timedelta(hours=1),
        )

@fixture_generator(issues.Solution, requires=['issues.test_users', 'issues.test_issues', ])
def test_solutions():
    issue1, issue2 = issues.Issue.objects.all()
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
    issue1, issue2 = issues.Issue.objects.all()
    mod, user1, user2, user3, user4 = issues.User.objects.all()
        
    _comments.create(content_object=issue1, user=user1, site_id=1, comment='Hullo')
    _comments.create(content_object=issue2, user=user1, site_id=1, comment='Hullo')

@fixture_generator(requires=['issues.test_users', 'issues.test_issues', 'issues.test_solutions', 'issues.test_comments', 'issues.test_ratings', ])
def __all__():
    pass