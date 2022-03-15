from src import script
import PIL.Image
from os.path import abspath
def main(new_width=100):

    path = input("Enter a Valid path to an image: ")
    path_save = input("Enter a Path to Save the ASCII image: ")
    file_name = input("Enter the name of File to save: ")
    full_fileName = path_save+'/'+file_name+'.txt'
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return
    
    new_image_data = script.pixels_to_ascii(script.grayify(script.resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    # print(ascii_image)

    #save the result
    with open(full_fileName,"w") as f:
        f.write(ascii_image)

    print(f'File has Been processed and saved at {abspath(f.name)}')


    
 
main()
