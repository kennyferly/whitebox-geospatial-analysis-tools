# Isaac Wismer
# idw.wismer@gmail.com
# Build script for Whitebox-GAT
# September 2017

import subprocess
import platform

def normalBuild(folder):
    compileNormal(folder)
    copyMetaInf(folder)
    makejar(folder)
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
    print("Deleting Files")
    #subprocess.call(rm + ' release/lib/groovy-all-2.4.1.jar', shell=True)
    #subprocess.call(rm + ' release/lib/javax.mail.jar', shell=True)
    #subprocess.call(rm + ' release/lib/proj4j-0.1.0.jar', shell=True)
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
    #if (windows):
    subprocess.call('javac -sourcepath ' +folder+ ' -cp "lib/*" -d bin/' +folder+ ' ' + apiWin, shell=True)
    #else:
    #    subprocess.call('javac -sourcepath ' +folder+ ' -cp "lib/*" -d bin/' +folder+ ' ' +folder+ '/whitebox/*/*.java ' +folder+ '/whitebox/*/*/*.java ' +folder+ '/whitebox/*/*/*/*.java', shell=True)
    print("Making jar: " + folder)
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
    subprocess.call('javac -sourcepath ' + folder + ' -cp "lib/*" -d bin/' + folder + ' ' + folder + '/photogrammetry/*.java ' + folder + '/photogrammetry/util/*.java ' + folder + '/photogrammetry/util/model/*.java ' + folder + '/photogrammetry/util/model/linalg/*.java ' + folder + '/photogrammetry/util/model/models/*.java ' + folder + '/photogrammetry/util/model/project/*.java ', shell=True)
    copyMetaInf(folder)
    makejar(folder)
    print("Copying Source Files: " + folder)
    subprocess.call(copyTree  + ' ' + folder + '/photogrammetry/*.java ' + folder + '/photogrammetry/util/*.java ' + folder + '/photogrammetry/util/model/*.java ' + folder + '/photogrammetry/util/model/linalg/*.java ' + folder + '/photogrammetry/util/model/models/*.java ' + folder + '/photogrammetry/util/model/project/*.java ' + ' resources' + slash + 'plugins' + slash + 'source_files' + slash, shell=True)

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
    print("Copying Source Files: " + folder)
    subprocess.call(copyTree  + ' ' + folder + '/rastercalculator/*.java' + ' resources' + slash + 'plugins' + slash + 'source_files' + slash, shell=True)

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
    makeTest()
    release()

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

apiWin = "WhiteboxAPI/whitebox/algorithms/*.java WhiteboxAPI/whitebox/cartographic/*.java WhiteboxAPI/whitebox/georeference/*.java WhiteboxAPI/whitebox/geospatialfiles/*.java WhiteboxAPI/whitebox/geospatialfiles/shapefile/*.java WhiteboxAPI/whitebox/geospatialfiles/shapefile/attributes/*.java WhiteboxAPI/whitebox/interfaces/*.java WhiteboxAPI/whitebox/internationalization/*.java WhiteboxAPI/whitebox/parallel/*.java WhiteboxAPI/whitebox/plugins/*.java WhiteboxAPI/whitebox/projections/*.java WhiteboxAPI/whitebox/serialization/*.java WhiteboxAPI/whitebox/stats/*.java WhiteboxAPI/whitebox/structures/*.java WhiteboxAPI/whitebox/ui/*.java WhiteboxAPI/whitebox/ui/carto_properties/*.java WhiteboxAPI/whitebox/ui/plugin_dialog/*.java WhiteboxAPI/whitebox/utilities/*.java"

#build
makeRelease()
