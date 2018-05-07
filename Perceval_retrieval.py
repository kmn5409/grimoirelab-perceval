#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is a guide as to how to send Perceval to retrieve
# information about data sources for example git repositories
# This is also assuming you have installed perceval onto your computer

import datetime
import pytz
from perceval.backends.core.git import Git
from perceval.backends.core.pipermail import PipermailList
from grimoirelab.toolkit.datetime import datetime_utcnow
from grimoirelab.toolkit.datetime import str_to_datetime
from grimoirelab.toolkit.datetime import datetime_to_utc

# Url for the git repo to analyze
git_repo_url = 'https://github.com/mozilla/labs-vcap-tests.git'
# Directory for letting Perceval clone the git repo
git_repo_dir = '/tmp/perceval.git'
# Create a Git object, pointing to repo_url, using repo_dir for cloning
repo = Git(uri=git_repo_url, gitpath=git_repo_dir)
print("Starting 1")

'''
Uses the git object to print information about the repository,
this will then create the directory /tmp/perceval.git
other parameters you can use are:
	commit: aaa7a9209f096aaaadccaaa7089aaaa3f758a703
	Author:     John Smith <jsmith@example.com>
	AuthorDate: Tue Aug 14 14:30:13 2012 -0300
	Commit:     John Smith <jsmith@example.com>
	CommitDate: Tue Aug 14 14:30:13 2012 -0300
'''

for commit in repo.fetch():
	#print("ugh")
	print(commit['data']['Author'])
print("Starting 2")


# Url for the mailing list to analyze
mail_repo_url = 'https://mail-archives.apache.org/mod_mbox/httpd-dev/'
# Directory for letting Perceval clone the mailing list
mail_repo_dir = '/tmp/perceval/'
repo = PipermailList(url=mail_repo_url, dirpath=mail_repo_dir)
#Does not seem to affect what repositories are printed
k = str_to_datetime("1996-04")
k = datetime_to_utc(k)
print(k)
for message in repo.fetch(from_date=k):
	print(message[0])
print("Done")


'''
p2o.py --enrich --index git_raw --index-enrich git \
  -e http://localhost:9200 --no_inc --debug \
  git https://github.com/mozilla/addons-server.git

'''

