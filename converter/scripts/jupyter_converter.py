"""Script to watch and convert jupyter notebooks (.ipynb files) to python scripts (.py files).

Adapted from sync.py
"""
import subprocess
import os
import hashlib
import time

WATCHED_EXTS = [".ipynb"]
IGNORE_DIRS = [".git", ".ipynb_checkpoints", "site-packages", "bin"]


class Watcher:
    def __init__(self, updaters, watched_exts, base_path='.'):
        self.updaters = updaters
        self.base_path = base_path
        self._file_hashes = {}
        # Tracks whether this is the first pass of the directory tree. If not,
        # then any new file encountered will be treated as an update.
        self._first_pass = True
        self.watched_exts = watched_exts

    @staticmethod
    def get_file_hash(path):
        """Return a hash digest of the file located at path"""
        with open(path, "rb") as f:
            contents = f.read()
            return hashlib.md5(contents).hexdigest()

    def _post_file_if_changed(self, path):
        _, extension = os.path.splitext(path)
        if extension not in self.watched_exts:
            return

        hashed = self.get_file_hash(path)
        if not self._first_pass:
            old_hash = self._file_hashes.get(path)
            if old_hash != hashed:
                try:
                    for updater in self.updaters:
                        updater.send_file_update(path)
                except Exception as err:
                    # This has to be fairly generic to handle any updater
                    print("Unexpected error in updater class:", err)
        self._file_hashes[path] = hashed

    def _check_dir_for_changes(self, dir_path):
        if os.path.basename(dir_path) in IGNORE_DIRS:
            return

        for filename in os.listdir(dir_path):
            new_path = os.path.join(dir_path, filename)
            if os.path.isdir(new_path):
                # Recursively check subdirectories
                self._check_dir_for_changes(new_path)
            else:
                self._post_file_if_changed(new_path)

    def poll_for_changes(self, wait_time=1):
        while True:
            try:
                self._check_dir_for_changes(self.base_path)
            except Exception as err:
                # This should not be reached except in exceptional circumstances
                # We want to continue looping even if we hit an unexpected error
                print("Unexpected error in file watcher:", err)
            else:
                self._first_pass = False

            # Poll for changes every `wait_time` seconds, whether or not the
            # previous call succeeded.
            time.sleep(wait_time)


class JupyterUpdater:
    @classmethod
    def convert_jupyter_notebook_to_python_file(cls, jupyter_notebook_path):
        """Convert jupyter notebook to .py file for upload."""
        subprocess.run([
            'jupyter', 'nbconvert', '--to', 'script', jupyter_notebook_path,
            '--output-dir', '.exercises'
        ], check=False)


    def send_file_update(self, path):
        print('Converting jupyter notebook to .py file.', path)
        _, extension = os.path.splitext(path)
        if extension != '.ipynb':
            return

        try:
            self.convert_jupyter_notebook_to_python_file(path)
        except Exception:
            print(f"Unable to convert notebook at '{path}' to .py file for upload.")


def watch_and_convert_jupyter_files():
    print("Watching and converting Jupyter notebooks to .py files.")
    print("Hit Ctrl+C to stop.")

    jupyter_updater = JupyterUpdater()
    watcher = Watcher(updaters=[jupyter_updater], watched_exts=['.ipynb'])
    watcher.poll_for_changes()


if __name__ == "__main__":
    watch_and_convert_jupyter_files()
