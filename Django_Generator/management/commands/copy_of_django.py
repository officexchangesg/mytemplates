# from django.core.management.base import BaseCommand
import subprocess
from pathlib import Path
from subprocess import *
import os
from os.path import abspath
import sqlite3
# from django.contrib.auth.hashers import make_password

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# class Command(BaseCommand):
class Command():
    # subprocess.run(["python3", "-m", "venv", "my_env"], cwd=PyCharm_DIR)
    returnCode = None
    root = Path(__file__).resolve().parent.parent.parent.parent.parent
    project_root = ''

    def __int__(self):
        pass

    def create_superuser_by_SQL(self, sqlfile, name, password,email):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            # hased_pwd = make_password(password)
            hased_pwd = 'pbkdf2_sha256$390000$SfAuFWKnsR5X4U7rGcspMV$xOEXvAK12w5hdo3oPuigW08SHY7fP+QWqrPducvFr7k='
            print(hased_pwd)
            sqlite_select_Query = "insert into auth_user (username,password,email,date_joined,is_superuser,is_staff,is_active,last_name,first_name) values ('" + name + "','" + hased_pwd + "','" + email + "',CURRENT_TIMESTAMP,1,1,1,'','');"
            cursor.execute(sqlite_select_Query)
            sqliteConnection.commit()
            # record = cursor.fetchall()

            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def add_arguments(self, parser):
        parser.add_argument('project_name')

    def setup_env(self, projectName):

        self.returnCode = subprocess.run(['python3', '-m', 'venv', '%s_env' % projectName], cwd=self.root).returncode

        if self.returnCode == 0:
            print("The env " + '%s_env' % projectName + " has been created successfully")
        else:
            print("The env " + '%s_env' % projectName + " was NOT created successfully")

    def setup_project(self,projectName):
        subprocess.run(['django-admin', 'startproject', projectName], cwd=self.root).returncode
        if self.returnCode == 0:
            print("The project '" + '%s_env' % projectName + "' has been created successfully")
            self.project_root = str(self.root) + "/" + projectName
        else:
            print("The project '" + '%s_env' % projectName + "' was NOT created successfully")

    def activate_env(self, project):

        activate_path = '%s/%s_env/bin' % (str(self.root), project)

        project_root = '%s/%s' % (self.root, project)
        print("project root is " + project_root)

        self.returnCode = subprocess.run(['%s/pip' % activate_path, 'install', 'django'])
        # self.returnCode = subprocess.run(['%s/pip' % activate_path, 'install', 'django-debug-toolbar'])
        #self.returnCode = subprocess.run(['%s/pip' % activate_path, 'install', 'pynput'])
        self.returnCode = subprocess.call('%s/python3' % activate_path +  ' %s/manage.py' % project_root +  ' makemigrations', shell=True)
        self.returnCode = subprocess.call('%s/python3' % activate_path +  ' %s/manage.py' % project_root + ' migrate',shell = True)
        #
        # self.returnCode = subprocess.call(
        #     '%s/python3' % activate_path + ' %s/manage.py' % project_root + ' createsuperuser --username patrickeu --email officexchangesg@gmail.com',
        #      shell=True)
        self.create_superuser_by_SQL('%s/db.sqlite3' % self.project_root, 'patrick', 'Yu20120909$', 'jerry@gmail.com')

        self.returnCode = subprocess.call(
            '%s/python3' % activate_path + ' %s/manage.py' % project_root + ' runserver',shell=True)


        if self.returnCode == 0:
            print("The env '" + '%s_env' % project + "' has been activated successfully")

        else:
            print("The env '" + '%s_env' % project + "' was NOT activated successfully")

    def setup_apps(self, project, apps):
        # project_root = abspath(self.project_root).join(project)
        # print(project_root)
        # subprocess.run(['python', 'startproject', projectName], cwd=self.root).returncode
        pass

    def handle(self,  **options):
        # setup environment
        # print(options['project_name'])
        self.setup_env(options['project_name'])
        self.setup_project(options['project_name'])
        self.activate_env(options['project_name'])
        # self.create_superuser_by_SQL('%s/db.sqlite3' % self.project_root, 'patrick', 'Yu20120909$', 'jerry@gmail.com')


        # ate_superuser_by_SQL(self, sqlfile, name, password, email):



cmd = Command()
cmd.handle(project_name='testing18')
