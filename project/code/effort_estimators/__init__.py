from cross_validation import cross_validation
from reports import Reports

import config
def run() :
	for dataset in config.datasets :
		print dataset
		cross_validation.run_cross_validation(dataset)

		Reports.generate_reports(dataset)
		if config.display_output :
		    Reports.print_output(dataset)

if __name__ == "__main__":
	run()
	Reports.generate_charts(config.datasets)
