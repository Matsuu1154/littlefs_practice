from littlefs import LittleFS
import json

_INPUT_FOLDER = "input_data"
_OUTPUT_FOLDER = "output_data"
_JSON_FILE_NAME = "file_info.json"

# Initialize the File System according to your specifications

json_file = open(_JSON_FILE_NAME, 'r')
json_list = json.load(json_file)

for data_list in json_list:
    fs = LittleFS(block_size=512, block_count=256)
    for file_list in data_list["File"]:
        if file_list["Directory"] == "":
            inputdata_path = _INPUT_FOLDER + "/" + data_list["Partition"] + "/" + file_list["FName"]
        else :
            fs.mkdir(file_list["Directory"])
            inputdata_path = _INPUT_FOLDER + "/" + data_list["Partition"] + "/" + file_list["Directory"] + "/" + file_list["FName"] 
        with open(inputdata_path, 'r') as wr_file:
            print("write file: " + file_list["FName"])
            wr_data = wr_file.read()
            # Open a file and write some content
            with fs.open(file_list["FName"], 'w') as fh:
                fh.write(wr_data)

    outputdata_path = _OUTPUT_FOLDER + "/" + data_list["Partition"] + ".bin"
    # Dump the filesystem content to a file
    with open(outputdata_path, 'wb') as fh:
        fh.write(fs.context.buffer)
    