import csv
import glob

import matplotlib.pyplot as plt

plt.style.use('ggplot')


def plot_file(filename):
    with open(filename, newline='') as infile:
        reader = csv.DictReader(infile)
        # Skip the "Manual Posting" Line
        next(reader)
        # Read the "Points Possible" line
        points = next(reader)
        gradesheet = [row for row in reader]
        # Remove "Test Student"
        del gradesheet[-1]

        another = 'y'
        while another == 'y':
            for i, col in enumerate(reader.fieldnames):
                print(f"{i}) {col}")
            print("Select a column to plot or hit Enter to go back:")
            choice = input()
            if not choice:
                return
            column = reader.fieldnames[int(choice)]
            grades = [float(v[column]) for v in gradesheet]

            high_score = max(grades)
            points_possible = float(points[column])
            upper_limit = high_score if high_score > points_possible else points_possible
            print(f"{column}, Points Possible: {points_possible}")

            bin_width = int(input("Enter the bin width as an integer: "))
            num_bins = int(upper_limit // bin_width) + 1
            bins = [i * bin_width for i in range(int(upper_limit // bin_width) + 2)]

            plt.hist(grades, bins=bins, rwidth=0.95)
            plt.ylabel("Count")
            plt.xlabel("Score")
            plt.xticks(range(0, (num_bins + 1) * bin_width, bin_width))

            title = column[:column.rindex(' ')]
            plt.title(f"{title}\nOut of {points_possible} points")
            plt.savefig(title + '.png', bbox_inches='tight')
            print(f"File saved: {column + '.png'}")
            plt.show()

            another = input("Would you like to do another? y/n ")


def main():
    csvs = glob.glob("*.csv")
    print("Select a Canvas gradebook export file (CSV):")
    for i, name in enumerate(csvs):
        print(f"{i}) {name}")
    choice = input()
    if not choice:
        exit()
    plot_file(csvs[int(choice)])


if __name__ == "__main__":
    main()
