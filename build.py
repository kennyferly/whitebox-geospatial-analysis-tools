# Isaac Wismer
# idw.wismer@gmail.com
# Build script for Whitebox-GAT
# Originally written:
# September 2017
# Updated Oct 2017

# Copyright (C) 2017 Isaac Wismer <idw.wismer@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import platform
import sys

isRelease = False;

def normalBuild(folder):
    compileNormal(folder)
    copyMetaInf(folder)
    makejar(folder)
    if (isRelease):
        copySourceFiles(folder)

#compiles the .java files into bin/
def compileNormal(folder):
    print("Compiling: " + folder)
    subprocess.call(mkdir + ' bin' + slash + folder, shell=True)
    subprocess.call('javac -sourcepath ' + folder + ' -cp "lib/*" -d bin/' + folder + ' ' + folder + '/plugins/*.java', shell=True)

#copies the meta-inf data to bin/
def copyMetaInf(folder):
    print("Copying META-INF: " + folder)
    subprocess.call(mkdir + ' bin' + slash + folder + slash + 'META-INF', shell=True)
    subprocess.call(mkdir + ' bin' + slash + folder + slash + 'META-INF' + slash + 'services', shell=True)
    subprocess.call(copyFile + ' ' + folder + slash + 'META-INF' + slash + 'services' + slash + 'whitebox.interfaces.WhiteboxPlugin bin' + slash + folder + slash +'META-INF' + slash + 'services' + slash, shell=True)

#makes the jar
def makejar(folder):
    print("Making jar: " + folder)
    subprocess.call(cd  + ' bin/' + folder + '/ && jar -cf0 ../' + folder + '.jar *', shell=True)

def copySourceFiles(folder):
    subprocess.call(mkdir + ' resources' + slash + 'plugins' + slash + 'source_files' + slash, shell=True)
    print("Copying Source Files: " + folder)
    subprocess.call(copyTree  + ' ' + folder + slash + 'plugins' + slash + '*.java' + ' resources' + slash + 'plugins' + slash + 'source_files' + slash, shell=True)

def release():
    #copy all the extra files to the release folder
    print("Copying Files")
    subprocess.call(mkdir + ' release', shell=True)
    subprocess.call(mkdir + ' release' + slash + 'resources', shell=True)
    subprocess.call(copyTree + ' resources' + slash + '* release' + slash + 'resources' + slash, shell=True)
    subprocess.call(copyFile + ' bin' + slash + '*.jar release' + slash + 'resources' + slash + 'plugins', shell=True)
    subprocess.call(mkdir + ' release' + slash + 'lib', shell=True)
    subprocess.call(copyFile + ' lib' + slash + '* release' + slash + 'lib', shell=True)
    subprocess.call(copyFile + ' bin' + slash + 'WhiteboxGIS.jar release' + slash + 'WhiteboxGIS.jar', shell=True)
    subprocess.call(copyFile + ' release' + slash + 'resources' + slash + 'ReadMe.txt release' + slash + 'README.TXT', shell=True)
    subprocess.call(copyFile + ' release' + slash + 'resources' + slash + 'ReleaseNotes.txt release' + slash + 'ReleaseNotes.txt', shell=True)
    subprocess.call(copyFile + ' release' + slash + 'resources' + slash + 'Whitebox.bat release' + slash + 'Whitebox.bat', shell=True)
    subprocess.call(copyFile + ' whitebox_tools' + slash + 'target' + slash + 'release' + slash + 'whitebox_tools' + ext + ' release' + slash +'resources' + slash + 'plugins' + slash + 'NativePlugins' + slash, shell=True)
    print("Deleting Files")
    subprocess.call(rmFile + ' release' + slash + 'lib' + slash + 'MathTools.jar', shell=True)
    subprocess.call(rmFile + ' release' + slash + 'resources' + slash + 'plugins' + slash + 'WhiteboxAPI.jar', shell=True)
    subprocess.call(rmFile + ' release' + slash + 'resources' + slash + 'plugins' + slash + 'WhiteboxGIS.jar', shell=True)
    subprocess.call(rmFile + ' release' + slash + 'resources' + slash + 'plugins' + slash + 'FIleOperations.jar', shell=True)

#whiteboxAPI has a different structure so it can't be done with the regular build
def WhiteboxAPI():
    folder = 'WhiteboxAPI'
    print("Compiling: " + folder)
    #make folder in bin/ and compile
    subprocess.call(mkdir + ' bin' + slash + folder + '', shell=True)
    subprocess.call('javac -sourcepath ' +folder+ ' -cp "lib/*" -d bin/' +folder+ ' ' + apiWin, shell=True)
    #copy the internationalization files into bin/
    subprocess.call(copyTree + ' ' + folder + slash + 'whitebox' + slash + 'internationalization' + slash + '*.properties bin' + slash + folder + slash + 'whitebox' + slash + 'internationalization' + slash, shell=True)
    #make jar as usual
    makejar(folder)
    #copy to lib/
    subprocess.call(copyFile + ' bin' +slash +folder+ '.jar lib' + slash +folder+ '.jar', shell=True)

def ConversionTools():
    folder = 'ConversionTools'
    normalBuild(folder)

def FIleOperations():
    folder = 'FIleOperations'
    normalBuild(folder)

def GeasyTools():
    folder = 'GeasyTools'
    normalBuild(folder)

def GISTools():
    folder = 'GISTools'
    normalBuild(folder)

def HydroTools():
    folder = 'HydroTools'
    normalBuild(folder)

def ImageProcessingTools():
    folder = 'ImageProcessingTools'
    normalBuild(folder)

def ImportExport():
    folder = 'ImportExport'
    normalBuild(folder)

def LidarTools():
    folder = 'LidarTools'
    normalBuild(folder)

def MathTools():
    folder = 'MathTools'
    normalBuild(folder)

def Photogrammetry():
    folder = 'Photogrammetry'
    print("Compiling: " + folder)
    subprocess.call(mkdir + ' bin' + slash + folder, shell=True)
    subprocess.call('javac -sourcepath ' + folder + ' -cp "lib/*" -d bin/' + folder + ' ' + folder + '/jopensurf/*.java ' + folder + '/photogrammetry/*.java ' + folder + '/photogrammetry/util/*.java ' + folder + '/photogrammetry/util/model/*.java ' + folder + '/photogrammetry/util/model/linalg/*.java ' + folder + '/photogrammetry/util/model/models/*.java ' + folder + '/photogrammetry/util/model/project/*.java ', shell=True)
    copyMetaInf(folder)
    makejar(folder)
    # if (isRelease):
        # print("Copying Source Files: " + folder)
        # subprocess.call(copyTree  + ' ' + folder + '/photogrammetry/*.java ' + folder + '/photogrammetry/util/*.java ' + folder + '/photogrammetry/util/model/*.java ' + folder + '/photogrammetry/util/model/linalg/*.java ' + folder + '/photogrammetry/util/model/models/*.java ' + folder + '/photogrammetry/util/model/project/*.java ' + ' resources' + slash + 'plugins' + slash + 'source_files' + slash, shell=True)
    #copy to lib/
    subprocess.call(copyFile + ' bin' + slash + 'Photogrammetry.jar lib' + slash + 'Photogrammetry.jar', shell=True)

def RasterCalculator():
    folder = 'RasterCalculator'
    print("Compiling: " + folder)
    #raster calculator has a slightly different folder structure
    subprocess.call(mkdir + ' bin' + slash + folder, shell=True)
    subprocess.call('javac -sourcepath ' + folder + ' -cp "lib/*" -d bin/' + folder + ' ' + folder + '/rastercalculator/*.java', shell=True)
    subprocess.call(copyFile + ' ' + folder + slash + 'rastercalculator' + slash + 'labels.properties bin' + slash + folder + slash + 'rastercalculator' + slash + 'labels.properties', shell=True)
    makejar(folder)
    #copy to lib/
    subprocess.call(copyFile + ' bin' + slash + 'RasterCalculator.jar lib' + slash + 'RasterCalculator.jar', shell=True)
    # if (isRelease):
        # print("Copying Source Files: " + folder)
        # subprocess.call(copyTree  + ' ' + folder + '/rastercalculator/*.java' + ' resources' + slash + 'plugins' + slash + 'source_files' + slash, shell=True)

def RasterCreation():
    folder = 'RasterCreation'
    normalBuild(folder)

def StatsTools():
    folder = 'StatsTools'
    normalBuild(folder)

def StreamNetworkAnalysisTools():
    folder = 'StreamNetworkAnalysisTools'
    normalBuild(folder)

def TerrainAnalysisTools():
    folder = 'TerrainAnalysisTools'
    normalBuild(folder)

def VectorTools():
    folder = 'VectorTools'
    normalBuild(folder)

def WhiteboxGIS():
    folder = 'WhiteboxGIS'
    print("Compiling: " + folder)
    #WhitebixGIS has a slightly different folder structure
    subprocess.call(mkdir + ' bin' + slash + 'WhiteboxGIS', shell=True)
    subprocess.call('javac -sourcepath WhiteboxGIS -cp "lib/*" -d bin/WhiteboxGIS WhiteboxGIS/whiteboxgis/*.java WhiteboxGIS/whiteboxgis/user_interfaces/*.java', shell=True)
    print("Making jar: " + folder)
    subprocess.call(cd + ' bin' + slash + 'WhiteboxGIS' + slash + ' && jar cmf0 ..' + slash + '..' + slash + 'WhiteboxGIS' + slash + 'MANIFEST.MF ..' + slash + 'WhiteboxGIS.jar *', shell=True)

def WhiteboxTools():
    print("Compiling: WhiteboxTools")
    print("This will take some time, especially on slower computers.\nGo make yourself a cup of coffee (or have a nap if your computer is slow).")
    subprocess.call(cd  + ' whitebox_tools' + slash + ' && cargo build --release', shell=True); 

def clean():
    print("Cleaning bin/ and release/")
    if (windows):
        subprocess.call(rm + ' bin\\', shell=True)
        subprocess.call(rm + ' release\\', shell=True)
        subprocess.call(rm + ' resources\\plugins\\source_files\\', shell=True)
        subprocess.call(mkdir + ' bin\\', shell=True)
        subprocess.call(mkdir + ' release\\', shell=True)
        subprocess.call(mkdir + ' resources\\plugins\\source_files\\', shell=True)
    else:
        subprocess.call(rm + ' bin/*', shell=True)
        subprocess.call(rm + ' release/*', shell=True)
        subprocess.call(rm + ' resources/plugins/source_files/*', shell=True)

def makeTest():
    clean()
    #make each library in order
    WhiteboxAPI()
    ConversionTools()
    FIleOperations()
    GeasyTools()
    GISTools()
    HydroTools()
    ImageProcessingTools()
    ImportExport()
    LidarTools()
    MathTools()
    Photogrammetry()
    RasterCalculator()
    RasterCreation()
    StatsTools()
    StreamNetworkAnalysisTools()
    TerrainAnalysisTools()
    VectorTools()
    WhiteboxGIS()

def makeRelease():
    global isRelease
    isRelease = True
    makeTest()
    WhiteboxTools()
    release()

def help():
    print("Arguments:")
    print("Make whole project:")
    print("[release][test]")
    print("Make individual packages")
    print("[clean][whiteboxapi][conversiontools][fileoperations][geasytools, gistools, hydrotools, imageprocessingtools, importexport, lidartools, mathtools, photogrammetry, rastercalculator, rastercreation, statstools, streamnetworkanalysistools, terrainanalysistools, vectortools][whiteboxgis]")
    print("If no argument is provided, the test argument is assumed")
    print("\nExamples:")
    print("python build.py release\npython build.py WhiteboxAPI GIStools\npython build.py clean GIStools vectorTools")
    print("Note: arguments are not case sensitive")
    print("\nclean must be the first argument, or you will delete the code that you have just compiled")

#figure out if it's windows or not
windows = False
if ("Windows" in platform.platform()):
    windows = True
#setting the commands based on the OS
prefix = ""
if (windows):
    prefix = "powershell.exe "
rm = 'rm -rfd'
rmFile = 'rm -rfd'
if (windows):
    rm = 'rd /S /Q'
    rmFile = 'del /S /Q'
cd = 'cd'
copyTree = 'cp -r'
copyFile = 'cp'
if (windows):
    copyTree = 'xcopy /Y /E /Q'
    copyFile = 'copy /Y'
mkdir = 'mkdir -p'
if(windows):
    mkdir = 'mkdir'
slash = "/"
if(windows):
    slash = "\\"
ext = ""
if (windows):
    ext = ".exe"

apiWin = "WhiteboxAPI/whitebox/algorithms/*.java WhiteboxAPI/whitebox/cartographic/*.java WhiteboxAPI/whitebox/georeference/*.java WhiteboxAPI/whitebox/geospatialfiles/*.java WhiteboxAPI/whitebox/geospatialfiles/shapefile/*.java WhiteboxAPI/whitebox/geospatialfiles/shapefile/attributes/*.java WhiteboxAPI/whitebox/interfaces/*.java WhiteboxAPI/whitebox/internationalization/*.java WhiteboxAPI/whitebox/parallel/*.java WhiteboxAPI/whitebox/plugins/*.java WhiteboxAPI/whitebox/projections/*.java WhiteboxAPI/whitebox/serialization/*.java WhiteboxAPI/whitebox/stats/*.java WhiteboxAPI/whitebox/structures/*.java WhiteboxAPI/whitebox/ui/*.java WhiteboxAPI/whitebox/ui/carto_properties/*.java WhiteboxAPI/whitebox/ui/plugin_dialog/*.java WhiteboxAPI/whitebox/utilities/*.java"

#dictionart of functions
functions = {"clean":clean, "whiteboxapi":WhiteboxAPI, "conversiontools":ConversionTools, "fileoperations":FIleOperations, "geasytools":GeasyTools, "gistools":GISTools, "hydrotools":HydroTools, "imageprocessingtools":ImageProcessingTools, "importexport":ImportExport, "lidartools":LidarTools, "mathtools":MathTools, "photogrammetry":Photogrammetry, "rastercalculator":RasterCalculator, "rastercreation":RasterCreation, "statstools":StatsTools, "streamnetworkanalysistools":StreamNetworkAnalysisTools, "terrainanalysistools":TerrainAnalysisTools, "vectortools":VectorTools, "whiteboxgis":WhiteboxGIS, "whiteboxtools":WhiteboxTools}

#no args
if (len(sys.argv) == 1):
    print("No arguments specified, assuming test")
    makeTest()
#help menu
elif len(sys.argv) == 2 and sys.argv[1] == "help":
    help()
#make test
elif (len(sys.argv) == 2 and sys.argv[1] == "test"):
    print("Make test")
    makeTest()
#make release
elif (len(sys.argv) == 2 and sys.argv[1] == "release"):
    print("Make release")
    makeRelease()
#make clean
elif (len(sys.argv) == 2 and sys.argv[1] == "clean"):
    print("Cleaning")
    functions["clean"]()
else:
    #loop through all the arguments
    for arg in sys.argv:
        #boolean flag for if its valid or not
        found = False
        #loop through all the functions to find match
        for func in functions:
            #if they match, run the function and mark valid
            if arg.lower() == func:
                found = True
                functions[func]()
            #case for argv[0]
            elif arg == "build.py":
                found = True
        #if it didn't find the arg, print help and stop the compile
        if found == False:
            print("Unrecognized argument: " + arg)
            help()
            break
