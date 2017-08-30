set -e

if [ "$1" == "prod" ]; then
	echo "======================================================"
	echo "=                     PRODUCTION                     ="
	echo "======================================================"
	if [[ $needs_countdown -ne 0 ]]; then
		for (( i = 5 ; i >= 0; i-- )); do
			printf -- "-> Will continue in %d seconds\r" $i
			sleep 1
		done
	fi
	extra_args="--prod"
else
	echo "======================================================"
	echo "=                      SANDBOX                       ="
	echo "======================================================"
	echo "-> Running in SANDBOX mode"
	file_ending="_SANDBOX"
fi
