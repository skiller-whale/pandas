import os
import shutil
from pathlib import Path
import subprocess
import time

def test_jupyter_converter(tmpdir):
    """Integration test for jupyter_converter.py"""
    converter_src = Path(__file__).parent.parent / 'scripts' / 'jupyter_converter.py'
    notebook_src = Path(__file__).parent / 'fixtures' / 'empty.ipynb'
    py_src =  Path(__file__).parent / 'fixtures' / 'empty.py'

    tmp_dir = tmpdir.mkdir('test_jupyter_converter')

    try:
        # Create target directory structure
        exercises_dest = tmp_dir.mkdir('.exercises')
        converter_dest = tmp_dir.join('jupyter_converter.py')
        notebook_dest = tmp_dir.join('empty.ipynb')
        py_dest = exercises_dest.join('empty.py')

        shutil.copyfile(converter_src, converter_dest)

        print(tmp_dir)
        print(tmp_dir.listdir())

        # Start running `jupyter_converter.py` in a separate process.`
        converter_process = subprocess.Popen(['python', converter_dest], cwd=tmp_dir)
        try:
            # Wait for the process to start-up.
            time.sleep(1)

            # Copy file to destination.
            shutil.copyfile(notebook_src, notebook_dest)

            # Sleep to avoid race conditions here.
            time.sleep(2.5)

            assert os.path.exists(py_dest), 'jupyter_converter.py does not detect/convert files.'
            with open(py_src) as py_file:
                py_expected = py_file.read()

            with open(py_dest) as py_dest_file:
                py_actual = py_dest_file.read()

            assert py_expected == py_actual, (
                'jupyter_converter.py converted file differes from expected.'
            )
        finally:
            converter_process.kill()
    finally:
        tmp_dir.remove(rec=1)
