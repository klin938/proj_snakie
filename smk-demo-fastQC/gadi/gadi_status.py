#!/usr/bin/env python3

import sys
import subprocess
import json

jobid = sys.argv[1]

try:
    res = subprocess.run(
        "qstat -f -F json -x {}".format(jobid),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    jsondoc = json.loads(res.stdout.decode())

    try:
        exit_status = jsondoc["Jobs"][jobid]["Exit_status"]

        if (exit_status == 0):
            print("success")
        else:
            print("failed")
    except KeyError as e:
        # maybe do further checking against job_state if needed
        #job_state = jsondoc["Jobs"][jobid]["job_state"]
        print("running")

except (subprocess.CalledProcessError, IndexError, KeyboardInterrupt) as e:
    print("failed")
