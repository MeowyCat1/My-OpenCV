# Homework - 15/11/25

1. We use `os.chdir()` to change the directory to the directory of the images so that the code can access the images
2. We use `f.lower().endswith(('.jpg','.jpeg','.png'))` to make sure that the files the program tries to add are images and not other files, causing issues with the videp.
3. So it can find the average of the images and resize them to be the same
4. Because `cv2.VideoWriter()` requires all images to be the same size, or it won't work
5. So the resized images don't get mixed up with the original images
6. `Image.LANCZOS` is an algorithm that helps resize images in high quality
7. `os.path.splitext(f)[0]` splits the file path into path and extension, and outputs the path. If `cv2.imread()` fails, it returns a `NoneType` object.
8. In this code, we do not sort the images, and there is no obvious reason to.
9. `cv2.VideoWriter_fourcc(*'mp4v')` sets the _fourcc_ value to `mp4v`, which defines the video codec used to compress the video.
