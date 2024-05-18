import argparse
import os
import glob

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process item data and apply to templates.')
    parser.add_argument('data_directory', type=str, help='Directory containing item data files.')
    parser.add_argument('template_file', type=str, help='Template file path.')
    parser.add_argument('date', type=str, help='Date in MM/DD/YYYY format.')
    parser.add_argument('output_directory', type=str, help='Output directory for processed templates.')
    return parser.parse_args()

def should_process_item(current_quantity, max_quantity):
    return current_quantity < max_quantity * 0.1

def read_item_files(directory):
    item_details = {}
    for item_file in glob.glob(os.path.join(directory, '*.item')):
        with open(item_file, 'r') as file:
            lines = file.read().splitlines()
            simple_name, item_name = lines[0].split(' ', 1)
            current_quantity, max_quantity = map(int, lines[1].split())
            body = lines[2]
            if should_process_item(current_quantity, max_quantity):
                item_number = os.path.splitext(os.path.basename(item_file))[0]
                item_details[item_number] = {
                    'simple_name': simple_name,
                    'item_name': item_name,
                    'current_quantity': current_quantity,
                    'max_quantity': max_quantity,
                    'body': body
            }
    return item_details

def process_template(template_path, date, item_details):
    with open(template_path, 'r') as file:
        template = file.read()
    outputs = {}
    for item_number, details in item_details.items():
        filled_template = template.replace('<<date>>', date)
        filled_template = filled_template.replace('<<simple_name>>', details['simple_name'])
        filled_template = filled_template.replace('<<item_name>>', details['item_name'])
        filled_template = filled_template.replace('<<current_quantity>>', str(details['current_quantity']))
        filled_template = filled_template.replace('<<max_quantity>>', str(details['max_quantity']))
        filled_template = filled_template.replace('<<body>>', details['body'])

        outputs[item_number] = filled_template
    return outputs

def write_output(output_dir, item_outputs):
    os.makedirs(output_dir, exist_ok=True)
    for item_number, content in item_outputs.items():
        with open(os.path.join(output_dir, '{}.out'.format(item_number)), 'w') as file:
            file.write(content)

def main():
    args = parse_arguments()
    item_details = read_item_files(args.data_directory)
    item_outputs = process_template(args.template_file, args.date, item_details)
    write_output(args.output_directory, item_outputs)

if __name__ == "__main__":
        main()
