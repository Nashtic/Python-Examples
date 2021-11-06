#source: https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
#I made little changes for image sources at encode_text() and decode_text() functions. 
#Install the libaries with "pip install opencv-python" and "pip install google-colab"

import cv2
import numpy as np
import types 
from google.colab.patches import cv2_imshow

def messageToBinary(message):

  if type(message) == str:
    return ''.join([format(ord(i), "08b") for i in message])

  elif type(message) == bytes or type(message) == np.ndarray:   
    return [format(i, "08b") for i in message]

  elif type (message) == int or type(message) == np.uint8:
    return format(message, "08b")

  else:
    raise TypeError("This input method is not supported.")

def hideDataInImage(image, secret_message):

  n_bytes = image.shape[0] * image.shape[1] * 3
  print("Maximum bytes to encode: ", n_bytes)

  if len(secret_message) > n_bytes:
    raise ValueError("Error encountered insufficient bytes, need bigger image or less data!")

  secret_message += "#####" 

  data_index = 0

  binary_secret_message = messageToBinary(secret_message)

  data_len = len(binary_secret_message)

  for values in image:
    for pixel in values:

      r, g, b = messageToBinary(pixel)

      if data_index < data_len:

        pixel[0] = int (r[:-1] + binary_secret_message[data_index], 2)
        data_index += 1
      
      if data_index < data_len:
        pixel[0] = int (g[:-1] + binary_secret_message[data_index], 2)
        data_index += 1
      
      if data_index < data_len:
        pixel[0] = int (b[:-1] + binary_secret_message[data_index], 2)
        data_index += 1

      if data_index >= data_len:
              break

  return image

def showData(image):

  binary_data = ""
  for values in image:
    for pixel in values:

      r, g, b = messageToBinary(pixel)

      binary_data += r[-1] #extracting data from the least significant bit of red pixel
      binary_data += g[-1] #extracting data from the least significant bit of green pixel
      binary_data += b[-1] #extracting data from the least significant bit of blue pixel

  all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

  decoded_data = ""

  for byte in all_bytes:
      decoded_data += chr(int(byte, 2))
      if decoded_data[-5:] == "#####":
        break

  return decoded_data[:-5]


def encode_text():
  path = r'C:\\Users\\Selahattin\\Desktop\\cyberpunk.png'
  image = cv2.imread(path)

  print("The shape of this image is: ", image.shape)
  print("The original image is shown as below: ")
  resized_image = cv2.resize(image, (500, 500))
  cv2.imshow(resized_image)

  data = input("Enter data to be encoded: ")
  
  if (len(data) == 0):
    raise ValueError('Data is empty.')

  file_name = input("Enter the name of new encoded image with extension: ") 
  encoded_image = hideDataInImage(image, data)
  cv2.imwrite(file_name, encoded_image)

def decode_text():
  
  path = r'C:\\Users\\Selahattin\\Desktop\\cyberpunk.png'
  image = cv2.imread(path)

  print("The Steganographed image is as shown below: ")
  resized_image = cv2.resize(image, (500, 500))
  cv2.imshow(resized_image)

  text = showData(image)
  return text

def Steganography(): 
    a = input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
    userinput = int(a)
    if (userinput == 1):
      print("\nEncoding....")
      encode_text() 
          
    elif (userinput == 2):
      print("\nDecoding....") 
      print("Decoded message is " + decode_text()) 
    else: 
        raise Exception("Enter correct input") 
          
Steganography()
