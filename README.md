A small Python script that generates bar plots from Canvas Gradebook exports. 
- The user chooses a CSV file in the current directory, then selects a column to plot. 
- Specify the range for the bars, e.g., 2pts, 5pts, 10pts
- The plot is displayed and saved to a PNG file.

# PyCharm Setup

1. Clone or download+unzip project into a directory
2. Open the folder as a PyCharm Project
3. Go to Settings -> Project: <project-name> -> Python Interpreter
4. Select the Gear icon in the top right -> Add...
5. New environment -> Okay. Close out Settings once "Creating a Virtual Environment" completes
6. Click the Terminal at the bottom and run `pip install -r requirements.txt`. This may take a minute.

# Running

1. Go to Canvas Gradebook and Export. Download the gradebook's CSV file to your project directory.
2. Run `hist.py` in PyCharm

![Example plot](https://raw.githubusercontent.com/llayman/hist/master/examples/Assignment%203%20-%20Classes%20and%20Objects.png)
