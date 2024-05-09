from os import path
from os import walk
from setuptools import setup, find_packages
import shutil

var_strCaminhoResources = ''

here = path.abspath(path.dirname(__file__))

for var_strCaminhoRaiz, var_listSubDiretorio, var_listFile in walk(here):
    for sub in var_listSubDiretorio:
        for var_strCaminhoRaiz_nvl2, var_listSubDiretorio_nvl2, var_listFile_nvl2 in walk(path.join(var_strCaminhoRaiz,sub)):
            if 'resources' in var_listSubDiretorio_nvl2:
                var_strCaminhoResources = path.join(var_strCaminhoRaiz_nvl2,'resources\\.locator')

var_strCaminhoLocator = path.join(here,'.locator')

if path.exists(var_strCaminhoResources):
    shutil.rmtree(var_strCaminhoResources)

shutil.copytree(var_strCaminhoLocator,var_strCaminhoResources)


with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()


with open(path.join(here, 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

setup(
    name="ExemploWorkshop",
    version=version,
    description="Exemplo workshop vs code",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    package_data={
        "ExemploWorkshop": [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
            'classes_t2c/T2CCloseAllApplications.py',
            'classes_t2c/T2CInitAllApplications.py',
            'classes_t2c/T2CInitAllSettings.py',
            'classes_t2c/T2CKillAllProcesses.py',
            'classes_t2c/T2CProcess.py',
            'classes_t2c/email/T2CSendEmail.py',
            'classes_t2c/email/T2CSendEmailOutlook.py',
            'classes_t2c/sqlite/T2CSqliteQueue.py',
            'classes_t2c/sqlserver/T2CSqlAnaliticoSintetico.py',
            'classes_t2c/relatorios/T2CRelatorios.py',
            'classes_t2c/utils/T2CExceptions.py',
            'classes_t2c/utils/T2CMaestro.py',
            'classes_t2c/utils/T2CScreenRecorder.py',
            'resources'
        ]
    },
    install_requires=requirements,
)
