
from rarfile import RarFile, BadRarFile
import os

print("Hey Welcome to Winrar (Python Edition)")

def extract_rar():
    rar_path = input("paste your rar file path here : ")

    slices = rar_path.split("/")
    new_path = slices[:-1] + ["Extracted Here  "]
    extracted_here = "/".join(new_path)

    # this is my code before creating a new file :
    #   ectracted_here = rar_path[:-4] : /Users/mac/Downloads/revslider-package.rar

    

    try:
        # open rar File :3
        rf = RarFile(rar_path)

        # Creating the file "Extracted Here" 
        os.makedirs(extracted_here)
       
        
        # extract the Content
        rf.extractall(extracted_here)
        
        print(f"\nExtracted successfully to:\n>  {extracted_here}")

    except BadRarFile:
        print("Error: The file is not a valid RAR archive.")

    except FileExistsError: 
        print("Opss we need to change the file's name \n")     
        i = 2
        while True:
            try:
                extracted_here = extracted_here[:-1] + f"{i}"
                os.makedirs(extracted_here)
                print(f"\nExtracted successfully to:\n>  {extracted_here}")
                break
            except:
                i += 1
        rf.extractall(extracted_here)
        print(f"\nAfter Error : Extracted successfully to:\n>  {extracted_here}")


            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally: 
        print("\nthank you for using our script :3\n")

extract_rar()