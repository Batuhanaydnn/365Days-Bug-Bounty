import re
import argparse
import json
import xml.etree.ElementTree as ET
import os
from colorama import init, Fore, Style


def generate_regex_from_inputs(input_list, similarity_threshold=0.8):
    common_prefix = os.path.commonprefix(input_list)
    common_suffix = os.path.commonsuffix(input_list)

    regex = ""

    if common_prefix:
        regex += re.escape(common_prefix)

    if len(input_list) > 1:
        variable_inputs = [input_string[len(
            common_prefix): -len(common_suffix)] for input_string in input_list]
        regex += "(" + "|".join([generate_similar_regex(input,
                                                        similarity_threshold) for input in variable_inputs]) + ")"
    else:
        regex += generate_similar_regex(
            input_list[0][len(common_prefix): -len(common_suffix)], similarity_threshold)

    if common_suffix:
        regex += re.escape(common_suffix)

    return regex


def generate_similar_regex(input_string, similarity_threshold):
    similar_chars = []

    for char in input_string:
        if char not in similar_chars:
            similar_chars.append(char)

    if len(similar_chars) > 1:
        return "[" + "".join(similar_chars) + "]"
    else:
        return re.escape(input_string)


def parse_input_file(file_path, file_format):
    if file_format == "txt":
        with open(file_path, "r") as file:
            return file.read().splitlines()
    elif file_format == "json":
        with open(file_path, "r") as file:
            data = json.load(file)
            return data["inputs"]
    elif file_format == "xml":
        tree = ET.parse(file_path)
        root = tree.getroot()
        return [element.text for element in root.findall("input")]
    else:
        raise ValueError(
            "Invalid file format. Supported formats: txt, json, xml")


parser = argparse.ArgumentParser(
    description='Regex ifadesi oluşturma aracı.')
parser.add_argument('-r', '--regex', type=str,
                    help='Kullanılacak düzenli ifade.')
parser.add_argument('-i', '--input', type=str,
                    help='Test girişlerinin bulunduğu dosya.')
parser.add_argument('-f', '--format', choices=[
                    'txt', 'json', 'xml'], default='txt', help='Dosya formatı (varsayılan: txt)')
parser.add_argument('-s', '--similarity', type=float, default=0.8,
                    help='Benzerlik eşik değeri (varsayılan: 0.8)')
parser.add_argument('-m', '--man', action='store_true',
                    help='Kullanım klavuzunu görüntüler.')
args = parser.parse_args()


init(autoreset=True)

print(Fore.GREEN + """
.__..  ..___..__.  .__ .___.__ .___\  /
[__]|  |  |  |  |  [__)[__ [ __[__  >< 
|  ||__|  |  |__|  |  \[___[_./[___/  \
                                       
                        Creator: Muhammed Batuhan Aydın
""" + Style.RESET_ALL)

regex = args.regex
input_file = args.input
file_format = args.format
similarity_threshold = args.similarity

input_list = parse_input_file(input_file, file_format)

generated_regex = generate_regex_from_inputs(input_list, similarity_threshold)

print("Generated Regex expression:", generated_regex)
