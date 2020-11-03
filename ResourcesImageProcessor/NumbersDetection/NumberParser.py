import os

import cv2
import numpy as np


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


#######   training part    ###############
samples = np.loadtxt(os.path.join(__location__, 'generalsamples.data'), np.float32)
responses = np.loadtxt(os.path.join(__location__, 'generalresponses.data'), np.float32)
responses = responses.reshape((responses.size, 1))

model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

############################# testing part  #########################


def get_number(number_image):
    im = cv2.bitwise_not(number_image)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 2)

    # cv2.imshow('thresh', thresh)
    # cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    number = ''

    for cnt in contours:
        if cv2.contourArea(cnt) > 50:
            [x, y, w, h] = cv2.boundingRect(cnt)
            if h > 22 and h < 30:
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi = thresh[y:y + h, x:x + w]

                roismall = cv2.resize(roi, (10, 10))

                # cv2.imshow('out', roismall)
                # cv2.waitKey(0)

                roismall = roismall.reshape((1, 100))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k=1)
                string = str(int((results[0][0])))
                number = string + number
    #             cv2.putText(out, string, (x, y + h), 0, 1, (0, 255, 0))
    #
    # cv2.imshow('im', im)
    # cv2.imshow('out', out)
    # cv2.waitKey(0)

    return int(number)
