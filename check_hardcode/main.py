import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    # get sentences hardcode
    with open('sentences.json') as f:
        sentences_hardcode = json.load(f)
        
    errors      = []
    count_lines = 0
    for filename in args.filenames:
        with open(filename, 'rb') as fb:  
            for line in fb:
                sens = line.decode()
                for word in sentences_hardcode['data']:
                    if sens in word:
                        errors.append(TypeError(f"{filename} have hardcode ({word}%) line:{count_lines}"))
                count_lines += 1
       
    return errors

if __name__ == "__main__":
    main()