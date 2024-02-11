import os
import PyPDF2
import json
import traceback
import io

def read_file(filename):
    file = filename.name
    if file.endswith('.pdf'):
        try:
            file_contents = io.BytesIO(filename.read())
            # pdfFileObj = open(filename, 'rb')

            pdfReader = PyPDF2.PdfFileReader(file_contents)
            numPages = pdfReader.numPages
            pageObj = pdfReader.getPage(0)
            text = pageObj.extractText()
            return text
        except Exception as e:
            raise Exception('Error reading pdf file ', e)

    elif filename.endswith('.txt'):
        return filename.read().decode('utf-8')

    else:
        raise Exception('Unsupported file format')


def get_table_data(quiz_str):
    try:
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value['mcq']
            options = " | ".join(
                [
                    f"{option}->{option_value}" for option, option_value in value['options'].items()
                ]
            )

            correct = value['correct']
            quiz_table_data.append(
                {"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data
    except Exception as e:
        raise Exception('Error parsing json ', e)
