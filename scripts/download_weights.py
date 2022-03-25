import gdown
import os
import pathlib

ROOT_DIR = os.getcwd()
assert ROOT_DIR.endswith('AlphaPose')

def download_weights(drive_id, output_name, path):
    """
    Download a google drive file and save to path
    """
    dest_path = ROOT_DIR + path
    pathlib.Path(dest_path).mkdir(parents=True, exist_ok=True)
    os.chdir(dest_path)
    print(os.getcwd())
    if not pathlib.Path(dest_path + '/' + output_name).is_file():
        gdown.download(id=drive_id, output=output_name)
    else:
        print(f'{output_name} already exists')

if __name__ == '__main__':
    path_yolo = '/detector/yolo/data/'
    path_tracker = '/detector/tracker/data/'
    path_pretrained = '/pretrained_models/'

    file_id_yolo = '1D47msNOOiJKvPOXlnpyzdKA3k6E97NTC'
    file_id_tracker = '1nlnuYfGNuHWZztQHXwVZSL_FvfE551pA'
    file_id_fast_resnet = '1kQhnMRURFiy7NsdS8EFL-8vtqEXOgECn'
    
    download_weights(file_id_yolo, 'yolov3-spp.weights', path_yolo)
    download_weights(file_id_tracker, 'JDE-1088x608-uncertainty', path_tracker)
    download_weights(file_id_tracker, 'fast_res50_256x192.pth', path_pretrained)
