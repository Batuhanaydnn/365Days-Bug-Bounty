import re
import time
import argparse
from colorama import init, Fore, Style


class RedosDetector:
    def __init__(self, threshold=1.0):
        self.threshold = threshold

    def fuzzing(self, regex, input_string):
        start_time = time.time()
        result = re.match(regex, input_string)
        elapsed_time = time.time() - start_time
        return elapsed_time, result

    def detect_redos_vulnerabilities(self, regex, input_strings):
        detected_vulnerable_inputs = []
        for input_string in input_strings:
            elapsed_time, result = self.fuzzing(regex, input_string)
            if elapsed_time > self.threshold:
                detected_vulnerable_inputs.append((input_string, elapsed_time))
        return detected_vulnerable_inputs


parser = argparse.ArgumentParser(description='Redos zafiyeti tespit aracı.')
parser.add_argument('-r', '--regex', type=str,
                    help='Kullanılacak düzenli ifade.')
parser.add_argument('-i', '--inputs', nargs='+',
                    type=str, help='Test girişleri.')
parser.add_argument('-t', '--threshold', type=float, default=1.0,
                    help='Zaman sınırlaması (varsayılan: 1.0 saniye)')
parser.add_argument('-m', '--man', action='store_true',
                    help='Kullanım klavuzunu görüntüler.')
args = parser.parse_args()


init(autoreset=True)

print(Fore.GREEN + """
.__ .___.__ .__. __.  .__ .___.___..___ __ .___..__..__ 
[__)[__ |  \|  |(__   |  \[__   |  [__ /  `  |  |  |[__)
|  \[___|__/|__|.__)  |__/[___  |  [___\__.  |  |__||  \
                                                        
                        Creator: Muhammed Batuhan Aydın
""" + Style.RESET_ALL)
regex = args.regex
input_strings = args.inputs
threshold = args.threshold

# Redos zafiyeti tespit aracını oluştur
detector = RedosDetector(threshold)

# Redos zafiyeti tespiti yap
detected_vulnerabilities = detector.detect_redos_vulnerabilities(
    regex, input_strings)

# Tespit edilen zafiyetli girişleri raporla
if detected_vulnerabilities:
    print("Potansiyel Redos zafiyeti tespit edildi:")
    for input_string, elapsed_time in detected_vulnerabilities:
        print(f"Input: {input_string} / Elapsed Time: {elapsed_time:.5f}s")
else:
    print("Redos zafiyeti tespit edilmedi.")
