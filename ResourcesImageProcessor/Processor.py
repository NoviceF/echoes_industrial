import os
from collections import namedtuple
from pathlib import Path

import numpy as np
import cv2
import imutils

from ResourcesImageProcessor import PointsOperations
from ResourcesImageProcessor.NumbersDetection import NumberParser

resource = namedtuple('Resource', 'name, amount')


class ResourceImageProcessException(Exception):
    pass


class ResourceDuplication(ResourceImageProcessException):
    pass


def load_samples():
    samples = dict()

    directory = r'../samples'
    for entry in os.scandir(directory):
        if (entry.path.endswith(".png")) and entry.is_file():
            samples[Path(os.path.basename(entry.path)).stem] = cv2.imread(entry.path, 0)

    return samples


g_samples = load_samples()


def find_template_in_image_many(main_image, template):

    img_gray = main_image

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    points_collections = PointsOperations.PointsCollections()
    for pt in zip(*loc[::-1]):
        points_collections.add_point(pt[0], pt[1])
        # cv2.rectangle(main_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # cv2.imwrite('res.png', img_rgb)
    # cv2.imshow("main_image", main_image)
    # cv2.waitKey(0)

    return points_collections.count_points() > 1


def find_template_in_image(main_image, template, resouce_name):
    templateCanny = cv2.Canny(template, 50, 200)
    (tH, tW) = templateCanny.shape[:2]
    # cv2.imshow("Template", template)
    # cv2.waitKey(0)
    gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    found = None
    # loop over the scales of the image
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray_image,
                                 width=int(gray_image.shape[1] * scale))
        r = gray_image.shape[1] / float(resized.shape[1])
        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break

        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, templateCanny, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        # check to see if the iteration should be visualized
        # if args.get("visualize", False):
        # draw a bounding box around the detected region

        # clone = np.dstack([edged, edged, edged])
        # cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
        #               (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
        # cv2.imshow("Visualize", clone)
        # cv2.waitKey(0)

        # if we have found a new maximum correlation value, then update
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r, resized)

    if not found:
        return False, None

    # unpack the bookkeeping variable and compute the (x, y) coordinates
    # of the bounding box based on the resized ratio
    (maxVal, maxLoc, r, resized) = found

    if find_template_in_image_many(resized, template):
        raise ResourceDuplication(
            'More then one resource of type "{}"'.format(resouce_name))

    threshold = 0.9

    if maxVal <= threshold:
        return False, None

    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

    # cv2.rectangle(main_image, (startX, startY), (endX, endY), (0, 0, 255), 2)
    # cv2.imshow("Image", main_image)
    # cv2.waitKey(0)

    # find amount area
    # heightAmountRect = int((endY - startY) * 0.20)
    heightAmountRect = 38
    (startX, startY) = (startX, endY + 2)

    endY = startY + int(heightAmountRect)

    # draw a bounding box around the detected result and display the image
    # cv2.rectangle(main_image, (startX, startY), (endX, endY), (0, 0, 255), 2)
    # cv2.imshow("Image", main_image)
    # cv2.waitKey(0)

    # cv2.imshow("Image", main_image[startY:endY, startX:endX])
    # cv2.waitKey(0)

    # number = get_number(main_image[startY:endY, startX:endX])
    number = NumberParser.get_number(main_image[startY:endY, startX:endX])

    return found, number


# return file descriptor
def process_image(main_image):
    result = dict()

    for resource_name, template_image in g_samples.items():
        found, value = find_template_in_image(
            main_image, template_image, resource_name)

        if found:
            result[resource_name] = value

    return result
