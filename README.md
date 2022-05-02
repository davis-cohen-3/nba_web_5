# nba_web_5
nba analytics website


nba analytics website Final submission:

What I said I was going to do: Have the website fully working Have fantasy site working Include a leaderboard Implement some type of inheritance Deploy the website via heroku or some other framework Add unit testing

What I actually did: The website is working nearly perfectly. There are few errors I ge when I do queries on the analytics page. The fantasy page is working how I wanted it to. However, I would like to continue working on the player ratings so the game is more competitive The leaderboard is also working and sorting based on the best overall team I didn’t implement inheritance, rather I just made a new csv file with new columns based on player ratings for specific statistics. The coding for that took place in a jupyter notebook. The website is only able to run currently through a local host. I would like to continue editing the website and the fantasy page for me to deploy the website. I didn’t do any unit testing. All my testing followed a waterfall approach where I made sure each component of the website worked as I did everything. Most of the testing was just doing print statements to the backend

Screenshots:

Home page (very basic) and just describes the components of the site:

Analytics Page:

Select form and directs to next page.

Enter query for a rendered page with table>

Enter form based on team:

Example: (top assist leader on the lakers)

Second Form:

Top players in points per game who also average at least 8 rebounds per game:

Fantasy page:

→

Submitting team for report:

Leaderboard:

Coding in jupyter notebook for creating the new csv:

How to use/test:

Go to the within nba_web_5 directory .

Then run “source bin/activate” to activate venv.

Then go to src directory within nba_web_5 directory .

Run “python3 manage.py runserver 8000”.

To start server.

Copy the link and try out website.

To see database and its tables you need to install db.sqlite3 and it will show you tables if press the play button.

That covers up everything.
