#!python
import os
import sys

def SelectBuildDir(build_dir, platform=None):

    # if no platform is specified, then default to sys.platform
    if not(platform):
        platform = sys.platform

    print "Looking for build directory for platform '%s'" % platform

    # setup where we start looking at first
    test_dir = build_dir + os.sep + platform
    default_dir = build_dir + os.sep + 'default'


    # we look for a directory named exactly after the
    # platform so that very specific builds can be done
    if os.path.exists(test_dir):
        # make sure it is a directory
        target_dir = test_dir
    else:
        print "Exact match not found, finding closest guess"

        # looks like there isn't an exact match
        # find the closest matching directory
        dirs = os.listdir(build_dir)
        found_match = 0
        for dir in dirs:
            if platform.find(dir) != -1:
                 # found a match (hopefully the right one)
                 target_dir = build_dir + os.sep + dir
                 found_match = 1
                 break
        if not(found_match):
            print "No match found, looking for 'default' directory"
            # looks like this platform isn't available
            # try the default target
            if os.path.exists(default_dir):
                target_dir = default_dir
            else:
                # bad, nothing is available, tell the user
                print "No build directories found for your platform '%s'" % platform
                return None

    print "Found directory %s, will build there" % target_dir
    return target_dir

def ParseConfig(env,command,options):
    env_dict = env.Dictionary()
    static_libs = []

    # setup all the dictionary options
    if not env_dict.has_key('CPPPATH'):
        env_dict['CPPPATH'] = []

    if not env_dict.has_key('LIBPATH'):
        env_dict['LIBPATH'] = []

    if not env_dict.has_key('LIBS'):
        env_dict['LIBS'] = []

    if not env_dict.has_key('CXXFLAGS'):
        env_dict['CXXFLAGS'] = []

    if not env_dict.has_key('LINKFLAGS'):
        env_dict['LINKFLAGS'] = []

    # run the config program to get the options we need
    full_cmd = "%s %s" %  (WhereIs(command), join(options))

    params = split(os.popen(full_cmd).read())

    i = 0
    while i < len(params):
        arg = params[i]
        switch = arg[0:1]
        opt = arg[1:2]
        if switch == '-':
            if opt == 'L':
                env_dict['LIBPATH'].append(arg[2:])
            elif opt == 'l':
                env_dict['LIBS'].append(arg[2:])
            elif opt == 'I':
                env_dict['CPPPATH'].append(arg[2:])
            elif arg[1:] == 'framework':
                flags = [env_dict['LINKFLAGS']]
                flags.append(join(params[i:i+2]))
                env_dict['LINKFLAGS'] = join(flags)
                i = i + 1
            else:
                env_dict['CXXFLAGS'].append(arg)
        else:
            static_libs.append(arg)
        i = i + 1
    return static_libs

def SelectBuildDir(build_dir, platform=None):

    # if no platform is specified, then default to sys.platform
    if not(platform):
        platform = sys.platform

    print "Looking for build directory for platform '%s'" % platform

    # setup where we start looking at first
    test_dir = build_dir + os.sep + platform
    default_dir = build_dir + os.sep + 'default'


    # we look for a directory named exactly after the
    # platform so that very specific builds can be done
    if os.path.exists(test_dir):
        # make sure it is a directory
        target_dir = test_dir
    else:
        print "Exact match not found, finding closest guess"

        # looks like there isn't an exact match
        # find the closest matching directory
        dirs = os.listdir(build_dir)
        found_match = 0
        for dir in dirs:
            if platform.find(dir) != -1:
                 # found a match (hopefully the right one)
                 target_dir = build_dir + os.sep + dir
                 found_match = 1
                 break
        if not(found_match):
            print "No match found, looking for 'default' directory"
            # looks like this platform isn't available
            # try the default target
            if os.path.exists(default_dir):
                target_dir = default_dir
            else:
                # bad, nothing is available, tell the user
                print "No build directories found for your platform '%s'" % platform
                return None

    print "Found directory %s, will build there" % target_dir
    return target_dir

def RequireFiles(files, found_files, search_path):
    i = 0
    for file in found_files:
        if not(file):
            print "ERROR:  Could not find the %s file in:" % files[i]
            print "ERROR:  \t%s" % search_path
            print "ERROR:  Edit the build_config.py file and add"
            print "ERROR:  the location of this file to the appropriate variable."

            sys.exit(1)

        else:
            i = i + 1