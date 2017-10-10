set -e

if [ "$#" -lt 1 ]; then
    echo "ERROR: Illegal number of parameters"
		exit 1
fi

class=$1

if [ "$2" == "prod" ]; then
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
	file_ending="_${class}"
else
	echo "======================================================"
	echo "=                      SANDBOX                       ="
	echo "======================================================"
	echo "-> Running in SANDBOX mode"
	file_ending="_${class}_SANDBOX"
fi
