#!python
import os

projectname = 'pybind11_scene'				#holds the project name
projectpackage = 'src'						#holds the project folder
#buildroot = './bin/' + projectmode			#holds the root of the build directory tree
builddir = './' + projectpackage  			#holds the build directory for this project
#targetpath = buildroot + '/' + projectname	#holds the path to the executable in the build directory
#-------

#--include files
include_packages = []

#--engine node packages
core_packages = []

#--lib
lib_packages = []
#lib_packages.append('opengl32')


dll_packages = []
#--release

#--add list
lib_packages += core_packages
include_packages +=core_packages

lib_files = []
#lib_files.append("SFML-2.4.2\\lib\\sfml-graphics-s.lib")
