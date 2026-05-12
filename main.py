import csv
import os
import fitz  # PyMuPDF

# Define exact directory paths based on script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'student.csv')
PDF_DIR = os.path.join(BASE_DIR, 'pdf')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# --- CONFIGURATION ---
TEXT_X = 50
TEXT_Y = 265
FONT_SIZE = 48
FONT_COLOR = (0.95, 0.48, 0.12) # Orange

# --- NEW: WHITE PATCH CONFIGURATION ---
# Define the bounding box to cover the original "NAME" text.
# Format: (top-left X, top-left Y, bottom-right X, bottom-right Y)
# I have estimated the size based on your image. You can adjust these numbers 
# if the box is too small (leaves parts of "NAME" visible) or too big (cuts into the blue line).
PATCH_RECT = (40, 200, 300, 260)

# Change this if you download a custom font file
CUSTOM_FONT_NAME = "YourCustomFont.ttf" 

def generate_certificates():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    try:
        with open(CSV_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                name = row['name'].strip()
                workshop = row['workshopsession'].strip()
                
                template_filename = f"{workshop}.pdf"
                template_path = os.path.join(PDF_DIR, template_filename)
                
                if not os.path.exists(template_path):
                    print(f"⚠️ Warning: Template '{template_filename}' not found for {name}. Skipping.")
                    continue
                    
                doc = fitz.open(template_path)
                page = doc[0] 
                
                # --- 1. DRAW THE WHITE PATCH ---
                # Create the rectangle and fill it with white (color and fill are set to RGB 1,1,1)
                rect = fitz.Rect(PATCH_RECT)
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
                
                # --- 2. INSERT THE NEW TEXT ---
                point = fitz.Point(TEXT_X, TEXT_Y)
                font_path = os.path.join(BASE_DIR, CUSTOM_FONT_NAME)
                
                if os.path.exists(font_path):
                    page.insert_text(
                        point, 
                        name, 
                        fontsize=FONT_SIZE, 
                        color=FONT_COLOR,
                        fontfile=font_path
                    )
                else:
                    page.insert_text(
                        point, 
                        name, 
                        fontsize=FONT_SIZE, 
                        color=FONT_COLOR,
                        fontname="times-italic" 
                    )
                
                safe_name = name.replace(" ", "_")
                output_filename = f"{safe_name}_{workshop}_Certificate.pdf"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                
                doc.save(output_path)
                doc.close()
                print(f"✅ Generated: {output_filename}")
                
    except FileNotFoundError:
        print(f"❌ Error: Could not find {CSV_PATH}. Ensure the file exists.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == '__main__':
    print("Starting e-certificate generation...")
    generate_certificates()
    print("Process complete!")