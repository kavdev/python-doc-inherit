#!/usr/bin/env python

from pathlib import Path
import sys
from unittest import TestLoader, TextTestRunner

from coverage import Coverage
from termcolor import colored


TESTS_THRESHOLD = 84.09


def run_test_suite():

    cov = Coverage(config_file=True)
    cov.erase()
    cov.start()

    # Announce the test suite
    sys.stdout.write(colored(text="\nWelcome to the ", color="magenta", attrs=["bold"]))
    sys.stdout.write(colored(text="python-doc-inherit", color="green", attrs=["bold"]))
    sys.stdout.write(colored(text=" test suite.\n\n", color="magenta", attrs=["bold"]))

    # Announce test run
    print(colored(text="Step 1: Running unit tests.\n", color="yellow", attrs=["bold"]))

    test_suite = TestLoader().discover(str(Path("tests").absolute()))
    result = TextTestRunner(verbosity=1).run(test_suite)

    if not result.wasSuccessful():
        sys.exit(len(result.failures) + len(result.errors))

    # Announce coverage run
    print(colored(text="\nStep 2: Generating coverage results.\n", color="yellow", attrs=["bold"]))

    cov.stop()
    percentage = round(cov.report(show_missing=True), 2)
    cov.html_report(directory='cover')
    cov.save()

    if percentage < TESTS_THRESHOLD:
        print(colored(text="YOUR CHANGES HAVE CAUSED TEST COVERAGE TO DROP. " +
                           "WAS {old}%, IS NOW {new}%.\n".format(old=TESTS_THRESHOLD, new=percentage),
                           color="red", attrs=["bold"]))
        sys.exit(1)

    # Announce flake8 run
    sys.stdout.write(colored(text="\nStep 3: Checking for pep8 errors.\n\n", color="yellow", attrs=["bold"]))

    print("pep8 errors:")
    print("----------------------------------------------------------------------")

    from subprocess import call
    flake_result = call(["flake8", ".", "--count"])
    if flake_result != 0:
        print("pep8 errors detected.")
        print(colored(text="\nYOUR CHANGES HAVE INTRODUCED PEP8 ERRORS!\n", color="red", attrs=["bold"]))
        sys.exit(flake_result)
    else:
        print("None")

    # Announce success
    print(colored(text="\nTests completed successfully with no errors. Congrats!", color="green", attrs=["bold"]))

if __name__ == "__main__":
    run_test_suite()
