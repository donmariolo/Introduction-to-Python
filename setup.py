from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

includeFiles = ['conversortemperatura.ui']

buildOptions = dict(packages = [], excludes = [], include_files = includeFiles)

base = 'Console'

executables = [
    Executable('conversortemperatura.py', base=base)
]

setup(name='conversor',
      version = '1.0',
      description = 'Conversor de temperatura C F',
      options = dict(build_exe = buildOptions),
      executables = executables)