Sorting Visualizer 🎨🔢

A Pygame-based Sorting Algorithm Visualizer that helps you understand how different sorting algorithms work step by step.
It provides an interactive graphical representation of array elements as bars, which rearrange themselves in real-time while the algorithm executes.

✨ Features

Visualization of multiple sorting algorithms:

🫧 Bubble Sort

🎯 Selection Sort

📝 Insertion Sort

🔀 Merge Sort

⚡ Quick Sort

Adjustable number of elements (n) through an input box.

Dynamic bar visualization with color intensity mapped to value.

Smooth step-by-step animation with user control.

📸 Demo

(Add a GIF or screenshot of your visualizer here, e.g., running Bubble Sort)

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/sorting-visualizer.git
cd sorting-visualizer

2. Install dependencies

Make sure you have Python 3.8+ installed. Then install Pygame:

pip install pygame

3. Run the project
python main.py

🎮 Controls

Keyboard Inputs:

b → Run Bubble Sort

s → Run Selection Sort

i → Run Insertion Sort

m → Run Merge Sort

q → Run Quick Sort

Mouse & Input:

Click on the input box (top-left) to enter the number of elements (n).

Press Enter after typing the number to generate a new random list.

⚙️ Customization

Change default number of elements:

n = 100  # in main.py


Adjust speed of visualization by modifying:

speed = 1000  # frames per second


Modify screen size:

width = 1000
height = 700

📚 Concepts Covered

Sorting algorithms (with step-by-step visualization).

Stability of sorting algorithms (Insertion & Selection are stable here).

Pygame rendering basics.

Handling keyboard and mouse events.

🛠️ Tech Stack

Python 3.8+

Pygame (for visualization)

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this project and submit a pull request.

📜 License

This project is licensed under the MIT License
