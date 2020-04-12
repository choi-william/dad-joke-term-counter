
import grequests # for sending requests asynchronously
from flask import Flask

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import re # regex 

app = Flask(__name__)

@app.route('/jokes')
def getDadJokes():
	url = 'https://icanhazdadjoke.com/'
	headers = {
		'Accept':'application/json',
		'User-Agent':'DadJokeTermCounter (https://github.com/choi-william/repo)'
	}
	# Hard-coded number of requests
	# TODO: change up the code so that we maintain asynchronousity while continuing to send requests
	# until at least 10 jokes have been received (status 200).
	NUM_REQUESTS = 10
	NUM_SESSIONS = min(NUM_REQUESTS, 20) # 
	
	# Each grequests.get call creates a session
	# We limit the total number of sessions to prevent the connections being overloaded
	# In the event that requests are being sent sequentially, using the same session has 
	# a large run-time benefit due to HTTP persistent connection. Also same parameters can be persisted.
	sessions = [requests_retry_session() for i in range(NUM_SESSIONS)]
	requests = [grequests.get(url,session=sessions[i % NUM_SESSIONS], headers=headers) for i in range(NUM_REQUESTS)]

	# TODO: Handle exceptions
	responses = grequests.map(requests, size=NUM_SESSIONS)
	term_count = count_terms(responses)

	for response in responses:
		print(response.json()['joke'])

	for key, value in term_count.items():
		print(key+': ', value)

	return term_count

# Counts the number of occurrences of each term from a list of dad joke responses
def count_terms(responses):
	count = {}

	for response in responses:
		joke = response.json()['joke']

		# Maybe this in regex? (?<![a-zA-Z])'|'(?![a-zA-Z])
		terms = re.split('[\s"!?,.&-]+', joke.lower())
		for term in terms:
			if term in count:
				count[term] += 1
			elif term != '':
				count[term] = 1

	return count


# To retry sending the request in the event of an error
def requests_retry_session(
    	retries=3,
   		backoff_factor=0.3,
    	status_forcelist=(500, 502, 503, 504),
    	session=None):
    session = session or Session()
    retry = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)