import unittest
import json
import requests

APP_KEY = 'app_key'
APP_SECRET = 'app_secret'

USER_NAME = 'username'
REPO_NAME = 'GithubApi'
COMMIT_ENDPOINT = 'https://api.github.com/repos/%s/%s/commit' % (USER_NAME, REPO_NAME)

AUTHOR_NAME = 'Ivan Kostiuk'
AUTHOR_EMAIL = "email@users.noreply.github.com"


class GithubCommitsTest(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(GithubCommitsTest, self).__init__(*a, **kw)
        self.commits = []
        self.last_commit = {}

    @classmethod
    def setUpClass(cls):
        requests.get("https://api.github.com/users/whatever?client_id=%s&client_secret=%s" % (APP_KEY, APP_SECRET))

    def setUp(self):
        response = requests.get("https://api.github.com/repos/%s/%s/commits" % (USER_NAME, REPO_NAME))
        self.commits = json.loads(response.text)
        self.last_commit = self.commits[0]

    def test_gets_number_of_commits(self):
        print('\nTotal number of commits: %d' % len(self.commits))

    def test_verifies_url_commit_fields(self):
        print('\nVerifying url fields info')
        sha_value = self.last_commit['sha']
        self.assertEqual(self.last_commit['url'], COMMIT_ENDPOINT + "s/" + sha_value)
        self.assertIn(sha_value, self.last_commit['html_url'])
        self.assertEqual(self.last_commit['comments_url'], COMMIT_ENDPOINT + "s/" + sha_value + "/comments")

    def test_verifies_commit_author_info(self):
        print('\nVerifying commit author info')
        self.assertEqual(self.last_commit['commit']['author']['name'], AUTHOR_NAME)
        self.assertEqual(self.last_commit['commit']['author']['email'], AUTHOR_EMAIL)
        self.assertTrue(self.last_commit['commit']['author']['date'])

    def test_verifies_commit_committer_info(self):
        print('\nVerifying commit committer info')
        self.assertEqual(self.last_commit['commit']['committer']['name'], "GitHub")
        self.assertEqual(self.last_commit['commit']['committer']['email'], "noreply@github.com")
        self.assertTrue(self.last_commit['commit']['committer']['date'])

    def test_verifies_commit_child_fields_info(self):
        print('\nVerifying commit child fields info')
        self.assertTrue(self.last_commit['commit']['message'])
        self.assertTrue(self.last_commit['commit']['tree']['sha'])
        self.assertIn(self.last_commit['commit']['tree']['sha'], self.last_commit['commit']['tree']['url'])
        self.assertTrue(self.last_commit['commit']['url'])

    def test_verifies_author_fields_info(self):
        print('\nVerifying author fields info')
        # Ideally need to check each of the fields, but skipping due to time limit
        self.assertEqual(self.last_commit['author']['login'], USER_NAME)
        self.assertTrue(self.last_commit['author']['id'])
        self.assertIn(str(self.last_commit['author']['id']), self.last_commit['author']['avatar_url'])
        self.assertEqual(self.last_commit['author']['gravatar_id'], '')
        self.assertTrue(self.last_commit['author']['url'])
        self.assertTrue(self.last_commit['author']['html_url'])
        self.assertTrue(self.last_commit['author']['followers_url'])
        self.assertTrue(self.last_commit['author']['following_url'])
        self.assertTrue(self.last_commit['author']['gists_url'])
        self.assertTrue(self.last_commit['author']['starred_url'])
        self.assertTrue(self.last_commit['author']['subscriptions_url'])
        self.assertTrue(self.last_commit['author']['organizations_url'])
        self.assertTrue(self.last_commit['author']['repos_url'])
        self.assertTrue(self.last_commit['author']['events_url'])
        self.assertTrue(self.last_commit['author']['received_events_url'])
        self.assertTrue(self.last_commit['author']['type'])
        self.assertFalse(self.last_commit['author']['site_admin'])

    def test_verifies_committer_fields_info(self):
        print('\nVerifying committer fields info')
        # Another bunch of assertions for committer fields

    def test_verifies_parents_fields_info(self):
        print('\nVerifying commit parents fields info')
        # Another bunch of assertions for parents fields

if __name__ == '__main__':
    unittest.main(verbosity=2)
