import prediction
import gray
import mask

from PIL import Image
import cv2


def CutOut(model_path, uploaded_file):
    # load model
    model = prediction.DeepLabModel(model_path)

    # read image
    original_im = Image.open(uploaded_file)

    # inferences DeepLab model
    resized_im, seg_map = model.run(original_im)

    # show inference result
    prediction_image = prediction.vis_segmentation(resized_im, seg_map)
    
    # return input image
    input_image = prediction.input_return(resized_im)

    # input image to grayscale
    gray_image = gray.gray("./processed/prediction.jpg")

    # input image cut out
    mask_image = mask.mask("./processed/input.jpg", "./processed/gray.jpg")
    
    download_image = "./processed/mask.jpg"
    
    return download_image