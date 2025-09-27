# PDF Page Remover

A simple, user-friendly desktop application built with Python and Tkinter to remove a selected page from a PDF file. This tool prioritizes user privacy by processing files locally without any internet connection or data collection.

## Features

*   **Secure & Private**: All PDF processing is done locally on your computer. No data is ever sent to external servers.
*   **Intuitive GUI**: Easy-to-use graphical interface for selecting files and page numbers.
*   **Page Removal**: Quickly remove a specific page from any PDF document.
*   **Output Control**: Save the modified PDF to a location of your choice.

## Privacy Policy

This application is designed with your privacy in mind:

*   **No Data Collection**: This application does not collect, store, or transmit any personal data or document content.
*   **Local Processing**: All PDF operations are performed entirely on your local machine.
*   **No Internet Connection Required**: The application functions completely offline, ensuring your documents remain private.
*   **File Access Control**: The application only accesses PDF files that you explicitly select through the file dialog. It does not scan your file system or access other files without your permission.

## Installation

### From Executable (Windows)

1.  Go to the `dist` folder in the repository.
2.  Download the `pdf.exe` file.
3.  Run `pdf.exe`.

### From Source

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Dean988/Pdfremovewithprivacy.git
    cd Pdfremovewithprivacy
    ```
2.  **Install dependencies**:
    ```bash
    pip install PyPDF2 Pillow
    ```
3.  **Run the application**:
    ```bash
    python pdf.py
    ```

## How to Build the Executable (for Developers)

If you wish to build the executable yourself (e.g., for other operating systems or to ensure transparency), follow these steps:

1.  **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```
2.  **Navigate to the project directory** (where `pdf.py` and the `images` folder are located).
3.  **Build the executable**:
    ```bash
    pyinstaller --onefile --windowed --add-data "images;images" pdf.py
    ```
    *   `--onefile`: Creates a single executable file.
    *   `--windowed` or `--noconsole`: Prevents the console window from appearing (for GUI applications).
    *   `--add-data "images;images"`: Ensures the `images` folder and its contents are included in the executable.

4.  The executable `pdf.exe` will be found in the `dist` folder.
5.  **Clean up build artifacts**: After building, you can safely delete the `build/` directory, `pdf.spec` file, and `__pycache__/` folder as they are temporary build files and not needed for distribution.

## Usage

1.  **Select PDF File**: Click the "Browse" button and choose the PDF file from which you want to remove a page.
2.  **Enter Page Number**: In the "Page Number to Remove" field, enter the 1-based index of the page you wish to delete. For example, enter `1` for the first page, `2` for the second, and so on.
3.  **Remove Page**: Click the "Remove Page" button.
4.  **Save Modified PDF**: A "Save As" dialog will appear. Choose a location and name for your new PDF file (the one with the page removed).
5.  **Exit**: Click the "Exit" button to close the application.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.
