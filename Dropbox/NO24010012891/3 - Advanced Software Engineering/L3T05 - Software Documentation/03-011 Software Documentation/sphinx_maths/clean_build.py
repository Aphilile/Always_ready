import shutil
import os

build_dir = 'docs/_build'
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
print(f"Cleaned build directory: {build_dir}")
