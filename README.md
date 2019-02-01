Japanese version here
<https://github.com/urakubo/Dojo-standalone/blob/main0.3/README.ja.md>

This software is under development!

# A unified environment for DNN-based automated segmentation of neuronal EM images

- [Introduction](#Introduction)
- [System requirements](#System-requirements)
- [Installation](#Installation)
- [How to use: Dojo proofreader](#Dojo-proofreader)
- [How to use: 3D Annotator](#3D-Annotator)
- [How to use: 2D DNN](#2D-DNN)


## Introduction
Recent years have seen a rapid expansion in the field of micro-connectomics, which targets 3D reconstruction of neuronal networks from a stack of 2D electron microscopic (EM). The spatial scale of the 3D reconstruction grows rapidly over 1 mm3, thank to deep neural networks (DNN) that enable automated neuronal segmentation. Advanced research teams have developed their own pipelines for DNN-based large-scale segmentation (Informatics 2017, 4:3, 29). Those pipelines are typically a series of client-server software for alignment, segmentation, proofreading, etc., each of which requires specific PC configuration. Because of such complexity, it is difficult even for computer experts to use them, and impossible for experimentalists. This makes a serious divide between the advanced and general experimental laboratories.
   To bridge this divide, we are now trying to unify pieces of software for automated EM segmentation.

1.	We built a desktop version of the proofreading software Dojo (IEEE Trans. Vis. Comput. Graph. 20, 2466–2475) on Microsoft Windows 10, 64 bit.
2.	We merged it with a DNN framework: Google Tensorflow/tensorboard. 
3.	We then incorporated two types of DNN-based segmentation programs: 2D U-net/Resnet (https://github.com/tbullmann/imagetranslation-tensorflow) and the flood filling network (https://github.com/google/ffn).
4.	A 3D annotator was equipped for visual inspection and annotation (based on Three .js).
5.	2D/3D filtration functions were incorporated for the manipulation of DNN-filtered segmentation images (based on skimage and opencv3).

Multiple users can simultaneously use it through web browsers. The goal is to develop a unified software environment for DNN-based segmentation, postprocessing, proofreading, annotation, and visualization of EM images. The VAST Lite is recommended for ground truth generation for DNNs (https://software.rc.fas.harvard.edu/lichtman/vast/ ).

## System requirements
Operating system: Microsoft Windows 10 (64 bit). Linux and macOS versions will be built in future.
Recommendation: High-performance NVIDIA graphics card such as GeForce GTX 1080ti.

## Installation
We provide standalone versions (pyinstaller version) and Python source codes.

### Pyinstaller version 
1.	Download one of the following two versions, and unzip it:
	- CPU version (Ver0.59: 498 MB): https://www.dropbox.com/s/l1hogvujp1x6wiw/Dojo_Standalone0.59_cpu_pyinstaller.zip?dl=0
   	- GPU version (Ver0.XX: XXX MB): Under construction.

2.	Download sample EM/segmentation data from the following website, and unzip it:
   	- https://www.dropbox.com/s/pxds28wdckmnpe8/ac3x75.zip?dl=0
	- https://www.dropbox.com/s/6nvu8o6she6rx9v/ISBI_Dojo.zip?dl=0

3.	Please click the link "main.exe" in Dojo_StandaloneX.XX to launch the control panel.


### Python version 
1. Install Python 3.5 or 3.6 in a Microsoft Windows PC, 64 bit.
2. Install cuda 9.0 and cuDNN v7 for Tensorflow 1.12 (latest combination on 2018/12/20) if your PC has a NVIDIA-GPU.
3. Download the source codes from the github site:
   	- git clone https://github.com/urakubo/Dojo-standalone
4. Install the following modules of Python: Tensorflow-gpu, PyQt5, openCV3, pypng, tornado, pillow, libtiff, mahotas, h5py, lxml, numpy, scipy, scikit-image, pypiwin32, numpy-stl. Check also "requirements.txt". 
5. Copy Dojo_StandaloneX.XX/Marching_cube/marching_cubes.cp3X-win_amd64.pyd and paste it to {$INSTALL_PYTHON}\Lib\site-packages.

	- This marching cube program is obtained from the ilastik: https://github.com/ilastik/marching_cubes

6. Execute "python main.py" in the Dojo_StandaloneX.XX/ folder. The control panel will appear.

7. Download sample EM/segmentation data from the following website, and unzip it:
   	- https://www.dropbox.com/s/pxds28wdckmnpe8/ac3x75.zip?dl=0
	- https://www.dropbox.com/s/6nvu8o6she6rx9v/ISBI_Dojo.zip?dl=0


## How to use
### Dojo proofreader
This is a proofreading software as a part of Rhoana pipeline (Copyright, Lichtman/Pfister lab, Harvard, USA).

	- https://www.rhoana.org/dojo/

1. Select Dojo -> Open Dojo Folder from a dropdown menu, and specify the folder of the sample EM/segmentation dojo files. Dojo will be launched as a web application.
2. Please push the "Reload" button first if the Dojo seems to be in trouble. The Dojo can also be seen in the other web browser if you copy and paste the URL [ http://X.X.X.X:8888/dojo/ ] . You can use Dojo through in the web browsers in other PCs within the same LAN.
3.	The usage of Dojo is described in the original web page [ https://www.rhoana.org/dojo/ ] . For example, you can move the layers by pressing w/s keys, and change the opacity of segmentation by pressing c/d keys.
4.	You can import pairs of new EM images and segmentation by selecting Dojo -> Import EM Stack/Segmentation. Through the dialog, please specify the folders containing stacks of EM images and segmentation images (sequentially numbered, gray-scale png/tiff files). 
5.	The edited segmentation images can be exported as sequentially numbered, gray-scale png/tiff files, by selecting Dojo -> Export EM Stack / Export. 


### 3D Annotator
In the dropdown menu, select Annotator -> Open. The 3D Annotator will be launched.

1.	Check red crosses in the visible lane of the object table (right side). The checked objects will appear in the left side. Objects in the object table can be re-ordered by size, and you can see visible big objects by clicking the red crosses of large size objects.
2.	The appeared objects can be rotated, panned, zoomed in/out with the mouse, and their names and colors (RGB) can be changed though the object table.
3.	Also, you can control the background color, bounding box, and light projection to the objects.
4.	The edited contents of the object table can be saved by clicking the button under the object table (JSON/CSV).

Turn on the toggle switch in the accordion menu 'Marker label' (right side), then click any appeared objects. You will see red markers at the clicked surface location. 

1.	The appeared markers are registered in the marker table. Their colors (RGB), names, radiuses, and deletion can be controlled through the marker table.
2.	You can also define the colors, names, and numbers of next makers through the accordion menu 'Marker label' (right side).
3.	The edited contents of the marker table can be saved by clicking the download button under the marker table (JSON/CSV).

Click the "Save image" button at the right side. A screenshot of the scene will be saved as "Screechot.png".


### 2D DNN
We implemented 2D CNN (Resnet/U-net/Highwaynet/Densenet)-based segmentation programs on Tensorflow V1.12. Programmed by Dr. Torsten Bullmann.

	- https://github.com/tbullmann/imagetranslation-tensorflow

1.	In the pulldown menu, select Segmentation -> 2D DNN. You will see a dialog that has the two tabs: training and inference.
2.	Select the training tab and specify parameters:
	- Image Folder:	Folder containing EM images (tiff/png images).
	- Segmentation Folder: Folder containing ground truth segmentation (tiff/png images).
	- Checkpoint:	DNN connectivity will be stored.
	- X loss:	"hinge", "square", "softmax", "approx", "dice", "logistic"
	- Y loss:	"hinge", "square", "softmax", "approx", "dice", "logistic"
	- Model:	"pix2pix", "pix2pix2", "CycleGAN"
	- Generator:	"unet", "resnet", "highwaynet", "densenet"
	- Augmentation:	{fliplr  ,flipud, transpose} 
	- Maximal epochs
	- Display Frequency
	- Save Parameters
	- Load Parameters
3. Execute training. The default parameters target a sample EM image "Dojo_Standalone/data/_2DNN_ground_truth/0049.png" and segmentation image "Dojo_Standalone/data/_2DNN_training_images/49_memb.png".
4. Select Segmentation -> Tensorboard to inspect the progression of training. It took 5 min for the training of sample data by use of NVIDIA GeForce GTX 1070.
5. We know the end of training if "Saving model" appears.
6. Confirm the connectivity file "model-XXXXX.data-XXXXX-of-XXXXX" (800 MB) in the checkpoint folder. 
9. Select Segmentation -> 2D DNN, and set the parameters of the inference tab.
	- Image Folder:	Folder containing EM images (tiff/png images).
   	- Output Segmentation Folder 
	- Checkpoint 
10. Execute inference.
11. You will soon see the inference results in the Output Segmentation Folder (Dojo_Standalone/data/_2DNN_inference by default).

Hidetoshi Urakubo
209/2/1
