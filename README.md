# CamTech E-Certificate Generator

This automated script reads a list of student names from a CSV file and stamps them onto specific PDF certificate templates based on the workshop they attended. It also automatically covers up existing placeholder text (like "NAME") on the template.

## 📂 Project Structure

Ensure your folder structure looks exactly like this before running the script:

create-e-certificate/
│
├── main.py                # The main Python script
├── requirements.txt       # Python dependencies
├── student.csv            # List of students and their assigned workshops
├── YourCustomFont.ttf     # (Optional) A custom cursive font file for the names
│
├── pdf/                   # Directory containing blank certificate templates
│   ├── AI_Workshop.pdf
│   ├── Architecture_workshop.pdf
│   └── ...
│
└── output/                # Generated certificates will be saved here automatically

```

## ⚙️ Step 1: Initial Setup

1. **Install Python:** Ensure you have Python 3 installed on your machine.
2. **Open Terminal/Command Prompt:** Navigate to the `create-e-certificate` folder.
3. **(Optional but Recommended) Activate your virtual environment:**
```bash
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

```


4. **Install Dependencies:** Run the following command to install the required PDF library (`PyMuPDF`):
```bash
pip install -r requirements.txt

```



## 📝 Step 2: Prepare Your Data

1. **Add PDF Templates:** Place your blank certificate PDFs inside the `pdf/` folder.
2. **Update the CSV:** Open `student.csv` and add your student data.
* **Crucial:** The spelling of the `workshopsession` column must perfectly match the filename of the PDF template (without the `.pdf` extension).
* *Example:* If the workshop is `AI_Workshop`, you must have a file named `AI_Workshop.pdf` inside the `pdf/` folder.



## 🎨 Step 3: (Optional) Custom Fonts

If you want the names written in a cursive font instead of the standard font:

1. Download a `.ttf` font file (e.g., from Google Fonts).
2. Place the `.ttf` file in the same folder as `main.py`.
3. Open `main.py` and update line 17 with the exact filename:
```python
CUSTOM_FONT_NAME = "GreatVibes-Regular.ttf" 

```



## 🚀 Step 4: Run the Generator

Once your data is ready, simply run the script:

```bash
python3 main.py

```

Check the `output/` folder! You will see customized PDFs named like `Alice_Smith_AI_Workshop_Certificate.pdf`.

---

## 🔧 Configuration & Tweaking

If the name is printing in the wrong location or the white box isn't fully covering the placeholder text, you can adjust the coordinates at the top of `main.py`:

* `TEXT_X` and `TEXT_Y`: Controls where the student's name is printed.
* Decrease X to move left; Increase X to move right.
* Decrease Y to move up; Increase Y to move down.


* `PATCH_RECT`: Controls the white box that hides the original "NAME" text. The format is `(top-left X, top-left Y, bottom-right X, bottom-right Y)`. Adjust these numbers slightly if the box is too small or covers too much.
* `FONT_SIZE` & `FONT_COLOR`: Change the size and RGB color of the text.

## ⚠️ Troubleshooting

* **`Error: Could not find student.csv`**: Make sure your CSV file is in the exact same folder as `main.py` and is named exactly `student.csv`.
* **`Warning: Template not found`**: A workshop name in your CSV doesn't match any PDF in your `pdf/` folder. Check for typos or extra spaces in your CSV.
* **The font looks plain/basic**: The script couldn't find your custom `.ttf` file, so it fell back to a default font. Double-check that `CUSTOM_FONT_NAME` in `main.py` matches your downloaded font file exactly.
