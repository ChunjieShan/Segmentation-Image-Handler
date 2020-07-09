# Image Segmentation Images Handler
It is the next work after completing Classification Images Handler. It can make a training text with src images and masks like this:
```
Baidu_0006.jpg Baidu_0006_Mask0.png
Baidu_0007.jpg Baidu_0007_Mask0.png
Baidu_0008.jpg Baidu_0008_Mask0.png
Baidu_0010.jpg Baidu_0010_Mask0.png
Baidu_0012.jpg Baidu_0012_Mask0.png
Baidu_0013.jpg Baidu_0013_Mask0.png
Baidu_0014.jpg Baidu_0014_Mask0.png
Baidu_0018.jpg Baidu_0018_Mask0.png
Baidu_0019.jpg Baidu_0019_Mask0.png
Baidu_0022.jpg Baidu_0022_Mask0.png
Baidu_0024.jpg Baidu_0024_Mask0.png
Baidu_0025.jpg Baidu_0025_Mask0.png
Baidu_0026.jpg Baidu_0026_Mask0.png
Baidu_0028.jpg Baidu_0028_Mask0.png
Baidu_0029.jpg Baidu_0029_Mask0.png
Baidu_0031.jpg Baidu_0031_Mask0.png
Baidu_0032.jpg Baidu_0032_Mask0.png
Baidu_0033.jpg Baidu_0033_Mask0.png
Baidu_0037.jpg Baidu_0037_Mask0.png
Baidu_0039.jpg Baidu_0039_Mask0.png
Baidu_0041.jpg Baidu_0041_Mask0.png
Baidu_0043.jpg Baidu_0043_Mask0.png
Baidu_0044.jpg Baidu_0044_Mask0.png
Baidu_0045.jpg Baidu_0045_Mask0.png
Baidu_0048.jpg Baidu_0048_Mask0.png
Baidu_0049.jpg Baidu_0049_Mask0.png
Baidu_0061.jpg Baidu_0061_Mask0.png
Baidu_0062.jpg Baidu_0062_Mask0.png
Baidu_0063.jpg Baidu_0063_Mask0.png
Baidu_0066.jpg Baidu_0066_Mask0.png
Baidu_0075.jpg Baidu_0075_Mask0.png
Baidu_0078.jpg Baidu_0078_Mask0.png
Baidu_0081.jpg Baidu_0081_Mask0.png
Baidu_0087.jpg Baidu_0087_Mask0.png
Baidu_0089.jpg Baidu_0089_Mask0.png
Baidu_0090.jpg Baidu_0090_Mask0.png
Baidu_0091.jpg Baidu_0091_Mask0.png
Baidu_0100.jpg Baidu_0100_Mask0.png
...
```

## Contents
1. generate_list.py: The main script.
2. run_handler.sh: The shell script.

## Usage
You need to change the content of the shell script. You need to specify the images directory and masks directory.
```
python3 ./generate_list.py Image Masks
```
