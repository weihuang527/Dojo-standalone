#
#
#
import os
import numpy as np
import socket
import tempfile

class Params:
    def __init__(self):

        #
        # Environmental variables
        #

        desktop_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH")    + os.sep + "Desktop"
        mydocument_path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + os.sep + "Documents"
        user_path    = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH")

        ###
        user_path = "C:\\Users\\urakubo\\Desktop\\dojo180721"
        ###C:\Users\urakubo\Desktop\ffn\180620Laxmi
        ### C:\Users\urakubo\Desktop\dojo180721


        # Mojo unit image size for import
        self.tile_num_pixels_y  = 512
        self.tile_num_pixels_x  = 512
        self.ncolors            = 16000 ########## 65535
        self.tile_path_wz       = os.sep + 'w={0:08d}' + os.sep + 'z={1:08d}'
        self.tile_ids_filename_wzyx = os.sep + 'w={0:08d}' + os.sep + 'z={1:08d}' + os.sep + 'y={2:08d},x={3:08d}.hdf5'
        self.tile_images_filename_wzyx = os.sep + 'w={0:08d}' + os.sep + 'z={1:08d}' + os.sep + 'y={2:08d},x={3:08d}.tif'

        self.tile_ids_filename_yx = 'y={0:08d},x={1:08d}.hdf5'
        self.tile_images_filename_yx = 'y={0:08d},x={1:08d}.tif'

        self.tile_var_name      = 'IdMap'
        # self.dtype_tile         = np.uint32
        self.ids_dtype          = np.uint32
        self.images_dtype       = np.uint8
        self.hdf_color_name = 'idColorMap'

        self.backup_db_name = 'idTileIndex'
        self.image_extension = 'tif'
        self.id_extension    = 'hdf5'

        # Export
        self.export_col_name = 'colormap'
        self.export_db_name = 'segmentInfo'
        self.export_db_ids = ['id', 'name', 'size', 'confidence', 'type', 'subtype']

        # self.export_images_dir          = 'export_images'
        # self.export_ids_dir             = 'export_ids'
        # self.export_images_name         = 'z%08d'
        # self.export_ids_name            = 'z%08d'

        self.fname_plugins_menu = './Plugins/menu.json'


        # Mojo file paths
        self.files_found = False
        self.files_path  = user_path
        self.flag_undo   = 0
        self.flag_redo   = 0

    def SetUserInfo(self, user_path):

        #
        # User dependent variables
        #

        self.files_path                = user_path
        self.ids_path                  = self.files_path  + os.sep + 'ids'
        self.tile_ids_path             = self.ids_path    + os.sep + 'tiles'
        self.tile_ids_volume_file      = self.ids_path    + os.sep + 'tiledVolumeDescription.xml'
        self.color_map_file            = self.ids_path    + os.sep + 'colorMap.hdf5'
        self.segment_info_db_file      = self.ids_path    + os.sep + 'segmentInfo.db'
        self.segment_info_db_undo_file  = self.ids_path    + os.sep + 'segmentInfo_undo.pickle'
        self.segment_info_db_redo_file  = self.ids_path    + os.sep + 'segmentInfo_redo.pickle'

        self.images_path               = self.files_path  + os.sep + 'images'
        self.tile_images_path          = self.images_path + os.sep + 'tiles'
        self.tile_images_volume_file   = self.images_path + os.sep + 'tiledVolumeDescription.xml'

        self.ids_files_undo             = []
        self.ids_files_redo             = []
        self.flag_undo                  = 0
        self.flag_redo                  = 0

        self.ip = socket.gethostbyname(socket.gethostname())
        self.configured = True
        self.port = 8888
        self.url  = 'http://' + self.ip + ':' + str(self.port) + '/dojo/'
        self.tmpdir = tempfile.mkdtemp()
        self.merge_table = []

        self.tmp_ids_path = self.tmpdir + os.sep + 'ids'
        self.tmp_tile_ids_path = self.tmpdir + os.sep + 'ids' + os.sep + 'tiles'

        self.dojo_thread = None
