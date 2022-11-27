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

    def setup_project(self, projectName):
        # path_to_project_name = '%s/%s' % (self.root, 'project_name')
        path_to_project_name = self.root
        print("path to project: current root is %s\n" % self.root)

        path_to_template = '--template %s %s' % (path_to_project_name, projectName)
        print("path to template %s\n" % path_to_template)

        self.returnCode = subprocess.run('django-admin startproject %s' % path_to_template, cwt=shell=True)
        if self.returnCode == 0:

            print('The project %s has been created successfully\n' % projectName)
            self.project_root = str(self.root) + "/" + projectName
        else:
            print('The project %s was NOT created successfully\n' % projectName)

    def activate_env(self, project):

        activate_path = '%s/%s_env/bin' % (str(self.root), project)

        project_path = '%s/%s' % (self.root, project)


        self.returnCode = subprocess.run(['%s/pip' % activate_path, 'install', 'django'])

        self.returnCode = subprocess.call('%s/python3' % activate_path + ' %s/manage.py' % project_path +  ' makemigrations', shell=True)
        if self.returnCode == 0:
            print('The migrations of project %s has been migrated successfully\n' % project)
        else:
            print('The migrations of project %s was NOT activated successfully\n' % project)

        self.returnCode = subprocess.call('%s/python3' % activate_path + ' %s/manage.py' % project_path + ' migrate', shell = True)

        if self.returnCode == 0:
            print('The project of %s has been migrated successfully\n' % project)
        else:
            print('The project of %s was NOT activated successfully\n' % project)

        self.create_superuser_by_SQL('%s/db.sqlite3' % self.project_root, 'patrick', 'Yu20120909$', 'jerry@gmail.com')

        self.returnCode = subprocess.call('%s/python3' % activate_path + ' %s/manage.py' % project_root + ' runserver', shell=True)

        if self.returnCode == 0:
            print('The env %s_env has been activated successfully\n' % project)
        else:
            print('The env %s_env was NOT activated successfully\n' % project)

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

cmd = Command()
cmd.handle(project_name='testing18')
