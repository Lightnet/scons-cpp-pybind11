#!python 
import platform
import os
import sys
import glob
from build_support import *
from build_config import *

print("Scons Script Build!")
projectmode = ARGUMENTS.get('mode', 'release')   #holds current mode
projecttool = 'window'

#check if the user has been naughty: only 'debug' or 'release' allowed
if not (projectmode in ['debug','release']):
	print("Error: expected 'debug' or 'release', found: " + projectmode)

#tell the user what we're doing
print('**** Compiling in ' + projectmode + ' mode...')

#--------
# application folder dir and output folder
#--------
buildroot = './bin/' + projectmode + '/'	#holds the root of the build directory tree
targetpath = buildroot + '/' + projectname	#holds the path to the executable in the build directory
#-------

#http://scons.org/doc/0.97/HTML/scons-man.html
#need to lanuch vcvars32.bat script so it can be add to os.environ else it will display 'cl' is not recognized as an internal or external command
#this will deal with the Visual Studio 
env = Environment(ENV = os.environ) #this load user complete external environment

system = platform.system()

#--------
# Operating System Checks and Tools
#--------
if system=='Windows':
	print("**** Window Tool")
	# Something to do with link error
	#https://msdn.microsoft.com/en-us/library/y0zzbyt4.aspx
	#env.Append(LINKFLAGS=['/SUBSYSTEM:CONSOLE'])
	#env.Append(LINKFLAGS=['PYBIND11_MODULE'])
	env.AppendUnique(CXXFLAGS=["/MD","/EHsc"])
	include_packages.append('libs\\include')
	#include_packages.append('libs\\include\\pybind11')
	include_packages.append('C:\\Python27\\include')
	env.Append(CPPPATH=include_packages) #include files
	env.Library(buildroot + 'python27' , ['C:\\Python27\\libs\\python27.lib'])
	env.SharedLibrary(buildroot + 'example' , Glob('src' + '\\*.cpp'),LIBS=['C:\\Python27\\libs\\python27.lib']) #dll
	#copy dll and name as .pyd
	env.InstallAs(target = buildroot + 'example.pyd',source = buildroot + 'example.dll')
	#copy test script .py for import test
	env.InstallAs(target = buildroot + 'test.py',source = 'src/test.py')

	#env.Library(buildroot + 'example' , Glob('src' + '\\*.cpp'))
	#lib_packages.append('pybind11')
	#lib_packages.append('python')
	#env.Program(targetpath, Glob(builddir + '\\*.cpp'), LIBS=lib_packages, LIBPATH=['.','src', buildroot])
print("**** Scons Script End!")
