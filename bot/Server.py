import logging
import requests


class Server:
	def __init__(self, host, project):
		self.base_url = 'http://{0}/{1}/'.format(host, project)

	def get(self, url):
		logging.info('GET from %s', self.base_url + url)
		r = requests.get(self.base_url + url)
		if r.status_code != requests.codes.ok:		# pylint: disable=no-member
			logging.error('Response http status code: %u', r.status_code)
			raise RuntimeError('Request was failed')
		return r.text

	def post(self, url, data):
		logging.info('POST to %s %u bytes', self.base_url + url, len(data))
		r = requests.post(self.base_url + url, data=data)
		if r.status_code != requests.codes.ok:		# pylint: disable=no-member
			logging.error('Response http status code: %u', r.status_code)
			raise RuntimeError('Request was failed')
		return r.text
