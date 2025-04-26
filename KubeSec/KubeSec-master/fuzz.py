# TODO: import 5 python methods we want to fuzz
# from scanner import isValidUserName

# from parserFuzzer import userNameFuzzer
import os
import random
import string
from parser import checkIfValidK8SYaml, checkIfWeirdYAML

from graphtaintFuzzer import constructHelmStringFuzzer
from myLogger import giveMeLoggingObject
from scanner import scanForDefaultNamespace, scanUserName


def fuzzer():
    # create logger
    logger = giveMeLoggingObject()
    try:
        logger.info("Running scanUserNameFuzzer()")
        logger.info("%s", scanUserNameFuzzer())

        logger.info("Running checkIfValidK8SYamlFuzzer()")
        logger.info("%s", checkIfValidK8SYamlFuzzer())

        logger.info("Logging constructHelmStringFuzzer() from graphtaint.py:")
        logger.info("Result %s", constructHelmStringFuzzer())

    except Exception:
        logger.error("An error occurred:\n", exc_info=True)
    return 0


# Youssef's Methods
def fuzzCheckIfWeirdYAML():
    for i in range(10):
        fuzz_input = random.choice(
            [
                123,
                3.14,
                None,
                True,
                [],
                {},
                set(),
                "".join(random.choices(string.printable, k=20)),
            ]
        )
        try:
            checkIfWeirdYAML(fuzz_input)
        except Exception as e:
            print(f"[{i}] Exception Caught in checkIfWeirdYAML:\n\t EXCEPTION: {e}")


def fuzzScanForDefaultNamespace():
    for i in range(10):
        fuzz_input = "".join(random.choices(string.printable, k=15))
        try:
            scanForDefaultNamespace(fuzz_input)
        except Exception as e:
            print(
                f"[{i}] Exception Caught in scanForDefaultNamespace:\n\t EXCEPTION: {e}"
            )


def formatException(eText):
    print(
        f"Exception Caught in function checkIfWeirdYAML from parser.py:\n\t EXCEPTION: {eText}"
    )


def scanUserNameFuzzer():
    test_cases = [
        (123, ["admin", "root"]),
        ("user_name", "not_a_list"),
        (None, ["test"]),
        ("gooduser", None),
        (["list_as_key"], ["val1", "val2"]),
        ("", []),
        ("admin", ["admin123", "rootadmin", "safeuser"]),
    ]

    for k_, val_lis in test_cases:
        try:
            print(f"Trying input: k_={k_}, val_lis={val_lis}")
            result = scanUserName(k_, val_lis)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Caught exception for inputs k_={k_}, val_lis={val_lis}: {e}")


def checkIfValidK8SYamlFuzzer():
    test_cases = [
        None,
        123,
        True,
        "/tmp/nonexistentfile.yaml",
        "not_a_real_file",
        "/etc/hosts",  # a real file but not YAML
    ]

    for path in test_cases:
        try:
            print(f"Trying path: {path}")
            if not isinstance(path, (str, bytes, os.PathLike)):
                print(f"Skipping invalid path input type: {type(path)}")
                continue
            result = checkIfValidK8SYaml(path)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Caught exception for path={path}: {e}")


if __name__ == "__main__":
    fuzzer()
    fuzzCheckIfWeirdYAML()
    fuzzScanForDefaultNamespace()
