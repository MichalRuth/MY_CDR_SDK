# import os
# import pickle
# from modelscan import modelscan
# from Dill_CDR import DillCDR
# from Pickle_CDR import PickleCDR
# #import H5_CDR
# #import H5_tf_CDR


# import subprocess
# import os

# def unzip_file_with_7zip(file_path, output_dir):
#     try:
#         # Ensure the output directory exists
#         os.makedirs(output_dir, exist_ok=True)
        
#         # Define the 7-Zip executable path and command
#         # seven_zip_exe = '/home/michal20/Documents/third-year/final_project/AI_model_CDR_SDK-main/SDK_CDR/7z2407-x64.exe'  # Adjust the path to your 7z executable if necessary
#         seven_zip_exe = '7z'
#         command = [seven_zip_exe, 'x', file_path, f'-o{output_dir}']
        
#         # Run the command
#         subprocess.run(command, check=True)
#         print(f"Successfully unzipped {file_path} to {output_dir}")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while unzipping the file: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # # Example usage
# # file_path = '/mnt/data/806ca6c13b4abaec1755de209269d06735e4d71a9491c783651f48b0c38862d5'
# # output_dir = '/mnt/data/unzipped_files'
# # unzip_file_with_7zip(file_path, output_dir)

# def run_modelscan(file_path):
#     # Use the correct class name for modelscan
#     ms = modelscan.ModelScan()
#     scan_results = ms.scan(file_path)
#     return scan_results

# def run_custom_cdr(file_path):
#     # Instantiate the CDR based on file extension
#     extension = os.path.splitext(file_path)[1]
#     # if extension in ['.pickle', '.pkl']:
#     cdr = PickleCDR(file_path)

#     # elif extension in ['.dill']:
#         # cdr = DillCDR(file_path)

#     #elif extension in ['.h5', '.hdf5']:
#         #cdr = H5_CDR(file_path)

#     #elif extension in ['.tf']:
#     #    cdr = H5_tf_CDR(file_path)
#     # else:
#         # raise ValueError(f"Unsupported file extension: {extension}")

#     return cdr

# def save_scan_results(scan_results, model_name, type, folder=''):
#     file_name = f"modelscan_{model_name}_{type}.txt"
#     file_path = os.path.join(folder, file_name)
#     with open(file_path, 'w') as f:
#         for key, value in scan_results.items():
#             f.write(f"{key}: {value}\n")


# import os
# import zipfile

# def extract_zip(file_path, extract_to):
#     if not os.path.exists(extract_to):
#         os.makedirs(extract_to)

#     with zipfile.ZipFile(file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to)

#     for root, dirs, files in os.walk(extract_to):
#         for file in files:
#             full_path = os.path.join(root, file)
#             if is_zip(full_path):
#                 new_extract_to = os.path.join(root, os.path.splitext(file)[0])
#                 extract_zip(full_path, new_extract_to)

# def is_zip(file_path):
#     try:
#         with zipfile.ZipFile(file_path, 'r') as zip_ref:
#             return True
#     except zipfile.BadZipFile:
#         return False

    


# def process_models(folder):
#     for file_name in os.listdir(folder):
#         file_path = os.path.join(folder, file_name)

#         if is_zip(file_path):
#               extract_to= 'unzipped_files_new'
#               extract_zip(file_path, extract_to)
#         else:
#             print(f"The file {file_path} is not a valid ZIP archive.")

#         # Attempt to identify the file type and contents
#         # import pickle

#         # output_dir = '/home/michal20/Documents/third-year/final_project/AI_model_CDR_SDK-main/SDK_CDR/unzipped_files'
#         # unzip_file_with_7zip(file_path, output_dir)
       
        
#         # Run initial modelscan
#         initial_scan_results = run_modelscan(file_path)
#         save_scan_results(initial_scan_results, file_name, 'before', 'safe_models')
        
#         # Run custom CDR
#         cdr = run_custom_cdr(file_path)

#         # Scan the model
#         res = cdr.scan()

#         # Print the scan results
#         print(f"Scan results for {file_name}:")
#         print(cdr.analyze())

#         if res is False:
#             print(f"The model {file_name} is safe.")
#             continue

#         # Disarm the model
#         cdr.disarm()
        
#         # Save the "safe" model
#         safe_model_path = os.path.join('safe_models', file_name)
#         cdr.save_as_new_file(safe_model_path)
        
#         # Run modelscan on the "safe" model
#         safe_scan_results = run_modelscan(safe_model_path)
#         save_scan_results(safe_scan_results, file_name, 'after', 'safe_models')
        
#         # Compare scans
#         if initial_scan_results == safe_scan_results:
#             print(f"Model {file_name} is safe and unchanged after CDR.")
#         else:
#             print(f"Model {file_name} was modified during CDR.")



# # def unzip_files(directory):
# #     for filename in os.listdir(directory):
# #         if filename.endswith('.zip'):
# #             with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_ref:
# #                 zip_ref.extractall(directory)

# # unzip_files('to_scan')

# if __name__ == "__main__":
#     process_models('to_scan')

import os
import pickle
from modelscan import modelscan
from Dill_CDR import DillCDR
from Pickle_CDR import PickleCDR
import subprocess
import zipfile

def unzip_file_with_7zip(file_path, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        seven_zip_exe = '7z'
        command = [seven_zip_exe, 'x', file_path, f'-o{output_dir}']
        subprocess.run(command, check=True)
        print(f"Successfully unzipped {file_path} to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while unzipping the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def run_modelscan(file_path):
    ms = modelscan.ModelScan()
    scan_results = ms.scan(file_path)
    return scan_results

def run_custom_cdr(file_path):
    extension = os.path.splitext(file_path)[1]
    cdr = PickleCDR(file_path)
    return cdr

def save_scan_results(scan_results, model_name, type, folder=''):
    file_name = f"modelscan_{model_name}_{type}.txt"
    file_path = os.path.join(folder, file_name)
    with open(file_path, 'w') as f:
        for key, value in scan_results.items():
            f.write(f"{key}: {value}\n")

def extract_zip(file_path, extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Create a new folder for the current file being extracted
    file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]
    new_extract_to = os.path.join(extract_to, file_name_without_extension)
    if not os.path.exists(new_extract_to):
        os.makedirs(new_extract_to)

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(new_extract_to)

    for root, dirs, files in os.walk(new_extract_to):
        for file in files:
            full_path = os.path.join(root, file)
            if is_zip(full_path):
                nested_extract_to = os.path.join(root, os.path.splitext(file)[0])
                extract_zip(full_path, nested_extract_to)

def is_zip(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            return True
    except zipfile.BadZipFile:
        return False

def find_files_with_extension(folder, extension):
    matched_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                matched_files.append(os.path.join(root, file))
    return matched_files

def process_models(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        if is_zip(file_path):
            extract_to = 'unzipped_files_new'
            extract_zip(file_path, extract_to)

            pkl_files = find_files_with_extension(extract_to, '.pkl')
            for pkl_file in pkl_files:
                process_single_file(pkl_file)
        else:
            print(f"The file {file_path} is not a valid ZIP archive.")
            process_single_file(file_path)

def process_single_file(file_path):
    # Run initial modelscan
    initial_scan_results = run_modelscan(file_path)
    save_scan_results(initial_scan_results, os.path.basename(file_path), 'before', 'safe_models')
    
    # Run custom CDR
    cdr = run_custom_cdr(file_path)

    # Scan the model
    res = cdr.scan()

    # Print the scan results
    print(f"Scan results for {file_path}:")
    print(cdr.analyze())

    if res is False:
        print(f"The model {file_path} is safe.")
        return

    # Disarm the model
    cdr.disarm()
    
    # Save the "safe" model
    safe_model_path = os.path.join('safe_models', os.path.basename(file_path))
    cdr.save_as_new_file(safe_model_path)
    
    # Run modelscan on the "safe" model
    safe_scan_results = run_modelscan(safe_model_path)
    save_scan_results(safe_scan_results, os.path.basename(file_path), 'after', 'safe_models')
    
    # Compare scans
    if initial_scan_results == safe_scan_results:
        print(f"Model {file_path} is safe and unchanged after CDR.")
    else:
        print(f"Model {file_path} was modified during CDR.")

if __name__ == "__main__":
    # process_models('to_scan')
    process_models('to_scan/one')
