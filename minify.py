import os
import python_minifier

SOURCE_DIRECTORY = "src"
EXCLUDED_DIRECTORIES = ["src/visual/examples"]


# Iterate through every file in our source directory
for subdirs, dirs, files in os.walk(SOURCE_DIRECTORY):
    canContinue = True
    for excluded in EXCLUDED_DIRECTORIES:
        # If subdir is inside of one of the excluded directories, skip it
        if os.path.commonpath([subdirs, excluded]) == excluded:
            canContinue = False
            break

    if not canContinue:
        continue

    for file in files:
        # We only care about minifying .py files that aren't already minified
        if file.split(".")[-1] == "py" and not file.endswith(".min.py"):
            outputFilename = file.split(".")
            outputFilename.insert(len(outputFilename) - 1, "min")
            outputFilename = ".".join(outputFilename)
            inputFp = open(os.path.join(subdirs, file))
            outputFp = open(os.path.join(subdirs, outputFilename), "w")
            outputFp.write(python_minifier.minify(inputFp.read()))
