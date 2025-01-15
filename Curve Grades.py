# Function to read scores from a file
def readScoresFile(file_name):
    scores = []
    with open(file_name, "r") as file:
        for line in file:
            # Read and convert each score to an integer
            score = int(line.strip())
            scores.append(score)
    return scores

# Function to calculate the mean of a list of scores
def calculateMean(scores):
    total = sum(scores)
    mean = total / len(scores)
    return mean

# Function to calculate the standard deviation of a list of scores
def calculateStandardDeviation(scores, mean):
    n = len(scores)
    squaredDiff = sum((x - mean) ** 2 for x in scores)
    variance = squaredDiff / n
    stdDeviation = variance ** 0.5
    return stdDeviation

# Function to calculate descriptive statistics such as mean, stdDeviation, count, max, and min
def calculateDescriptiveStatistics(scores):
    mean = calculateMean(scores)
    stdDeviation = calculateStandardDeviation(scores, mean)
    count = len(scores)
    maxScore = max(scores)
    minScore = min(scores)
    return mean, stdDeviation, count, maxScore, minScore

# Function to calculate the letter grade for a given score based on cutoffs
def calculateLetterGrade(score, mean, stdDeviation):
    # Define the cutoff points for each grade
    cutoffs = {
        'A': round(mean + 1.5 * stdDeviation, 1),
        'B': round(mean + 0.5 * stdDeviation, 1),
        'C': round(mean - 0.5 * stdDeviation, 1),
        'D': round(mean - 1.5 * stdDeviation, 1)
    }
    # Determine the letter grade based on the score
    if score >= cutoffs['A']:
        return 'A'
    elif score >= cutoffs['B']:
        return 'B'
    elif score >= cutoffs['C']:
        return 'C'
    elif score >= cutoffs['D']:
        return 'D'
    else:
        return 'F'

# Function to generate a list of letter grades for a list of scores
def generateLetterGradeTable(scores, mean, stdDeviation):
    letterGrades = [calculateLetterGrade(score, mean, stdDeviation) for score in scores]
    return letterGrades

# Function to count the distribution of letter grades
def countGradeDistribution(letterGrades):
    gradeCounts = {}
    for grade in letterGrades:
        # Count the number of each grade using a dictionary
        gradeCounts[grade] = gradeCounts.get(grade, 0) + 1
    return gradeCounts

# Function to write scores and letter grades to a file
def writeScoresAndLetterGrades(file_name, scores, letterGrades):
    with open(file_name, "w") as file:
        for score, grade in zip(scores, letterGrades):
            # Write each score and its corresponding letter grade to the file
            file.write(f"{score},{grade}\n")

# Function to display the descriptive statistics and grade distribution
def displayResults(mean, stdDeviation, count, maxScore, minScore, gradeCounts):
    print("Descriptive Statistics")
    print("Mean Score: {:.1f}".format(mean))
    print("Standard Deviation: {:.1f}".format(stdDeviation))
    print("Number of Scores: {}".format(count))
    print("Highest Score: {}".format(maxScore))
    print("Lowest Score: {}".format(minScore))
    print("\nGrade Distribution After Curving Grades")
    for grade, count in gradeCounts.items():
        print("{}: {}".format(grade, count))

# Main function to control the program flow
def main():
    scores = readScoresFile("Scores.txt")
    mean, stdDeviation, count, maxScore, minScore = calculateDescriptiveStatistics(scores)
    letterGrades = generateLetterGradeTable(scores, mean, stdDeviation)
    gradeCounts = countGradeDistribution(letterGrades)
    writeScoresAndLetterGrades("Scores-and-Letter-Grades.txt", scores, letterGrades)

    # Define the cutoff points for each grade
    cutoffs = {
        'A': round(mean + 1.5 * stdDeviation, 1),
        'B': round(mean + 0.5 * stdDeviation, 1),
        'C': round(mean - 0.5 * stdDeviation, 1),
        'D': round(mean - 1.5 * stdDeviation, 1)
    }

    # Display the cutoff points for each grade
    print("Curved Grade - Cut Off Points (to 1 decimal place)")
    for grade, cutoff in cutoffs.items():
        print(f"{grade}: {cutoff}")

    # Display the results including descriptive statistics and grade distribution
    displayResults(mean, stdDeviation, count, maxScore, minScore, gradeCounts)

if __name__ == "__main__":
    main()
