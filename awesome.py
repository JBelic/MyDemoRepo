import requests


def awesome_fun():
	print ("blah")
	return 42

def download_text_from_web():
	r = requests.get('https://python-mock-tutorial.readthedocs.io/en/latest/mock.html')
	r.text()
	return r

def countWords(text):
	return len(text)

def do_text_analysis():
	text = download_text_from_web()
	word_count = countWords(text)
	return word_count
