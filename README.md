
# CamTech E-Certificate Generator

This automated script reads a list of student names from a CSV file and stamps them onto specific PDF certificate templates based on the workshop they attended. It automatically covers up existing placeholder text (like "NAME") on the template and generates a customized PDF for each student.

---

## 📋 Prerequisites
Before you begin, ensure you have the following installed on your machine:
* **Python 3.x**
* **pip** (Python package installer)

## 📂 Project Structure
Ensure your project folder looks exactly like this before running the script:

```text
create-e-certificate/
├── main.py                # The core Python script
├── requirements.txt       # Python dependencies
├── student.csv            # Data: Students and their assigned workshops
├── YourCustomFont.ttf     # (Optional) Cursive font file
├── pdf/                   # Directory containing blank templates
│   ├── AI_Workshop.pdf
│   └── Architecture_workshop.pdf
└── output/                # Generated certificates will appear here

```

---

## 🚀 Step-by-Step Guide

### Step 1: Initial Setup

1. **Open your Terminal or Command Prompt** and navigate to the `create-e-certificate` folder.
2. **(Optional but Recommended) Create and activate a virtual environment:**
* **Mac/Linux:** `python3 -m venv venv && source venv/bin/activate`
* **Windows:** `python -m venv venv` then `venv\Scripts\activate`


3. **Install Dependencies:**
Run the following command to install the required PDF library (`PyMuPDF`):
```bash
pip install -r requirements.txt
```

### Step 2: Prepare Your Templates and Data
1. **Add PDF Templates:** Place your blank certificate PDFs inside the `pdf/` folder.
2. **Update the CSV:** Open `student.csv` and add your student data.
   
   > ⚠️ **CRUCIAL MAPPING RULE:** 
   > The exact text in the `workshopsession` column **must match** the filename of your PDF template (excluding the `.pdf` extension).

   **Example Mapping:**
   If your `student.csv` looks like this:
   | name | school | email | workshopsession |
   | :--- | :--- | :--- | :--- |
   | Alice Smith | Tech High | alice@example.com | **AI_Workshop** |

   You **must** have a corresponding file in the `pdf/` folder named:
   📄 `pdf/`**`AI_Workshop`**`.pdf`

### Step 3: (Optional) Custom Fonts
By default, the script will use standard fonts. To use a cursive or custom font for the student names:
1. Download a `.ttf` font file (e.g., from Google Fonts).
2. Place the `.ttf` file inside the `create-e-certificate` folder (next to `main.py`).
3. Open `main.py` and update line 17 with your exact filename:
   ```python
   CUSTOM_FONT_NAME = "GreatVibes-Regular.ttf" 
    ```

### Step 4: Run the Generator

Once your data is ready, run the script:

```bash
python main.py
```

🎉 **Done!** Check the `output/` folder. You will see customized PDFs named automatically, such as `Alice_Smith_AI_Workshop_Certificate.pdf`.

---

## 🔧 Configuration & Tweaking

If the name is printing in the wrong location or the white box isn't fully covering the placeholder text, open `main.py` and adjust the variables at the top of the file:

* **Text Placement (`TEXT_X`, `TEXT_Y`):** Controls where the student's name begins.
* Decrease `X` to move left; Increase `X` to move right.
* Decrease `Y` to move up; Increase `Y` to move down.


* **White Box Coverage (`PATCH_RECT`):** Controls the white box that hides the original "NAME" text.
* Format: `(top-left X, top-left Y, bottom-right X, bottom-right Y)`. Adjust these if the box is too small or cuts into the border.


* **Text Style (`FONT_SIZE`, `FONT_COLOR`):** Change the size and RGB color of the text.

---

## ⚠️ Troubleshooting

| Error / Issue | Solution |
| --- | --- |
| **`Error: Could not find student.csv`** | Make sure your CSV file is in the exact same folder as `main.py` and is named exactly `student.csv`. |
| **`Warning: Template not found`** | A workshop name in your CSV doesn't match any PDF in your `pdf/` folder. Check for typos or extra spaces in your CSV `workshopsession` column. |
| **The font looks plain/basic** | The script couldn't find your custom `.ttf` file and fell back to the default font. Double-check that `CUSTOM_FONT_NAME` in `main.py` perfectly matches your downloaded font file. |
