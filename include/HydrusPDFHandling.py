from . import HydrusConstants as HC
from . import HydrusData
import os
import subprocess
import time
import traceback

if HC.PLATFORM_LINUX:

    GS_PATH = os.path.join( HC.BIN_DIR, 'gswin64c.exe' )

elif HC.PLATFORM_MACOS:

    GS_PATH = os.path.join( HC.BIN_DIR, 'gswin64c.exe' )

elif HC.PLATFORM_WINDOWS:

    GS_PATH = os.path.join( HC.BIN_DIR, 'gswin64c.exe' )


def RenderPageToFile(path, temp_path, page_index):

    cmd = [GS_PATH,
           '-dBATCH',
           '-dNOPAUSE',
           '-sDEVICE=jpeg',
           '-dPDFFitPage=true',
           '-dDEVICEWIDTHPOINTS=150',
           '-dDEVICEHEIGHTPOINTS=125',
           '-dFirstPage=' + str(page_index),
           '-dLastPage=' + str(page_index),
           '-sOutputFile=' + temp_path,
           path]

    timeout = HydrusData.GetNow() + 60

    sbp_kwargs = HydrusData.GetSubprocessKWArgs()

    p = subprocess.Popen(cmd, **sbp_kwargs)

    while p.poll() is None:

        if HydrusData.TimeHasPassed(timeout):

            p.terminate()

            raise Exception('Could not render the pdf page within 60 seconds!')

        time.sleep(0.5)

    p.communicate()
