import argparse
import csv

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('files', nargs = '+')
	parser.add_argument('-n','--number', type=int, default=10)

	return parser.parse_args()

def read_month(path):
	month_results = dict()
	with open(path) as f:
		month_reader = csv.reader(f)
		for row in month_reader:
			medium_name = row[0]
			real_users = int(row[1])
			month_results[medium_name] = real_users
	return month_results

def read_all_months(paths):
	complete_months_results = dict()
	for path in paths:
		results = read_month(path)
		for medium, users in results.items():
			if medium in complete_months_results:
				complete_months_results[medium] += users
			else:
				complete_months_results[medium] = users
	return complete_months_results 


args = get_args()
statistics = read_all_months(args.files)
media_sorted = sorted(statistics, key=statistics.get, reverse=True)

for i, m in enumerate(media_sorted[:args.number], start=1):
	print i, m.split(' | ')[2], ':', statistics[m]