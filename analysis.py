# 22f3001135@ds.study.iitm.ac.in
# Marimo interactive data analysis notebook

import marimo as mo

app = mo.App()

# --- Cell 1: Input widget ---
# This slider lets the user control the sample size
@app.cell
def slider_cell():
    slider = mo.ui.slider(10, 200, value=50)  # range: 10–200, default=50
    return slider

# --- Cell 2: Generate data based on slider value ---
# This cell depends on the slider's state
@app.cell
def data_cell(slider):
    import numpy as np
    x = np.linspace(0, 10, slider.value)
    y = np.sin(x)
    return x, y

# --- Cell 3: Plot data ---
# This cell depends on x and y
@app.cell
def plot_cell(x, y):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.set_title("Interactive Sine Curve")
    ax.legend()
    return fig

# --- Cell 4: Dynamic Markdown output ---
# This cell shows the current slider value with emojis
@app.cell
def markdown_cell(slider):
    return mo.md(f"### Sample Size: {slider.value}  \n{'🟢' * (slider.value // 20)}")

if __name__ == "__main__":
    app.run()
