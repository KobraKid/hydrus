from preview_generator.manager import PreviewManager
from . import HydrusConstants as HC
from . import HydrusData
import os
import subprocess
import time
import traceback


def RenderPageToFile(path, temp_path, page_index):

    print(path)
    print(temp_path)
    print(page_index)

    # cmd = [SWFRENDER_PATH, path,  '-o', temp_path, '-p', str(page_index)]
    #
    # timeout = HydrusData.GetNow() + 60
    #
    # sbp_kwargs = HydrusData.GetSubprocessKWArgs()
    #
    # p = subprocess.Popen(cmd, **sbp_kwargs)
    #
    # while p.poll() is None:
    #
    #     if HydrusData.TimeHasPassed(timeout):
    #
    #         p.terminate()
    #
    #         raise Exception('Could not render the swf page within 60 seconds!')
    #
    #     time.sleep(0.5)
    #
    # p.communicate()
